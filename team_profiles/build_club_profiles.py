"""Build 2024-25 club style profiles for the Big Five leagues.

Run from the repo root:  python3 team_profiles/build_club_profiles.py

Inputs (read-only):
  top5_match_results_2024_25/*.csv                      Football-Data match results
  big5_player_performance/big5_player_stats_2024_2025.csv FBref/Understat player-season stats
  team_profiles/club_name_map.csv                       Football-Data name <-> FBref squad name

Outputs:
  team_profiles/output/club_match_averages_2024_25.csv  per-club match averages (step 1)
  team_profiles/output/club_profiles_2024_25.csv        all features, within-league z-scores, style tags

Formulas and tag rules are documented in team_profiles/README.md.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
MATCH_DIR = ROOT / "top5_match_results_2024_25"
PLAYER_FILE = ROOT / "big5_player_performance" / "big5_player_stats_2024_2025.csv"
NAME_MAP = ROOT / "team_profiles" / "club_name_map.csv"
OUT_DIR = ROOT / "team_profiles" / "output"

# Match columns kept; everything after AR (bookmaker odds) is dropped.
MATCH_COLS = ["Div", "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HTHG", "HTAG",
              "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"]
# Per-match stats that can be blank (e.g. an abandoned/awarded match).
STAT_COLS = ["ht_gf", "ht_ga", "sf", "sa", "sotf", "sota", "fouls", "fouls_drawn",
             "cf", "ca", "yellows", "reds"]

EXPECTED_CLUBS = {"EPL": 20, "ESP": 20, "ITA": 20, "GER": 18, "FRA": 18}
EXPECTED_GAMES = {"EPL": 38, "ESP": 38, "ITA": 38, "GER": 34, "FRA": 34}

TAG_Z = 0.75  # threshold for a feature to count as "high" (or "low" when negated)


def load_matches(name_map):
    frames = [pd.read_csv(f, encoding="utf-8-sig", usecols=MATCH_COLS)
              for f in sorted(MATCH_DIR.glob("*.csv"))]
    m = pd.concat(frames, ignore_index=True)
    div_to_league = dict(zip(name_map.football_data_div, name_map.league))
    m["league"] = m.Div.map(div_to_league)
    assert m.league.notna().all(), "unknown Div code in match files"
    return m


def club_match_rows(m):
    """One row per club per match, from that club's point of view."""
    def side(team, opp, gf, ga, htgf, htga, sf, sa, sotf, sota, fouls, fouls_drawn,
             cf, ca, yel, red, is_home):
        return pd.DataFrame({
            "league": m.league, "date": m.Date, "team": m[team], "opponent": m[opp],
            "is_home": is_home,
            "gf": m[gf], "ga": m[ga], "ht_gf": m[htgf], "ht_ga": m[htga],
            "sf": m[sf], "sa": m[sa], "sotf": m[sotf], "sota": m[sota],
            "fouls": m[fouls], "fouls_drawn": m[fouls_drawn],
            "cf": m[cf], "ca": m[ca], "yellows": m[yel], "reds": m[red],
        })

    home = side("HomeTeam", "AwayTeam", "FTHG", "FTAG", "HTHG", "HTAG", "HS", "AS", "HST", "AST",
                "HF", "AF", "HC", "AC", "HY", "HR", True)
    away = side("AwayTeam", "HomeTeam", "FTAG", "FTHG", "HTAG", "HTHG", "AS", "HS", "AST", "HST",
                "AF", "HF", "AC", "HC", "AY", "AR", False)
    r = pd.concat([home, away], ignore_index=True)
    r["points"] = np.select([r.gf > r.ga, r.gf == r.ga], [3, 1], 0)
    # A match counts toward per-game stats only if all its stat cells are present.
    r["has_stats"] = r[STAT_COLS].notna().all(axis=1)
    return r


def aggregate_matches(r):
    g = r.groupby(["league", "team"])
    s = r[r.has_stats].groupby(["league", "team"])  # matches with full stats only
    st = s[STAT_COLS + ["gf", "ga"]].sum()
    n_stat = s.size()

    out = pd.DataFrame({
        "games": g.size(),
        "games_with_stats": n_stat,
        "wins": g.points.apply(lambda p: (p == 3).sum()),
        "draws": g.points.apply(lambda p: (p == 1).sum()),
        "losses": g.points.apply(lambda p: (p == 0).sum()),
        "points": g.points.sum(),
        "goals_for": g.gf.sum(),
        "goals_against": g.ga.sum(),
    })
    out["points_per_game"] = out.points / out.games
    out["goals_for_pg"] = out.goals_for / out.games
    out["goals_against_pg"] = out.goals_against / out.games
    out["goal_diff_pg"] = out.goals_for_pg - out.goals_against_pg
    out["clean_sheet_pct"] = g.ga.apply(lambda x: (x == 0).mean())
    out["failed_to_score_pct"] = g.gf.apply(lambda x: (x == 0).mean())
    out["home_ppg"] = r[r.is_home].groupby(["league", "team"]).points.mean()
    out["away_ppg"] = r[~r.is_home].groupby(["league", "team"]).points.mean()

    # Per-game stats use only matches with stats; ratios use sums from the same matches.
    out["shots_for_pg"] = st.sf / n_stat
    out["shots_against_pg"] = st.sa / n_stat
    out["sot_for_pg"] = st.sotf / n_stat
    out["sot_against_pg"] = st.sota / n_stat
    out["corners_for_pg"] = st.cf / n_stat
    out["corners_against_pg"] = st.ca / n_stat
    out["fouls_pg"] = st.fouls / n_stat
    out["fouls_drawn_pg"] = st.fouls_drawn / n_stat
    out["yellows_pg"] = st.yellows / n_stat
    out["reds_pg"] = st.reds / n_stat
    out["shot_share"] = st.sf / (st.sf + st.sa)
    out["sot_share"] = st.sotf / (st.sotf + st.sota)
    out["corner_share"] = st.cf / (st.cf + st.ca)
    out["shot_accuracy"] = st.sotf / st.sf
    out["goals_per_shot"] = st.gf / st.sf
    out["goals_per_sot"] = st.gf / st.sotf
    out["opp_goals_per_sot"] = st.ga / st.sota
    out["first_half_goal_share"] = st.ht_gf / st.gf
    out["first_half_conceded_share"] = st.ht_ga / st.ga

    trailing = r[r.has_stats & (r.ht_gf < r.ht_ga)]
    tg = trailing.groupby(["league", "team"])
    out["games_trailing_ht"] = tg.size().reindex(out.index, fill_value=0)
    out["points_rescued_when_trailing_ht_pg"] = (
        tg.points.mean().reindex(out.index))  # NaN if never trailed at half-time
    return out.reset_index()


def aggregate_players(name_map):
    p = pd.read_csv(PLAYER_FILE)
    tot = p.groupby(["league", "squad"]).agg(
        players_used=("player_id", "nunique"),
        minutes=("minutes", "sum"),
        tackles_won=("tackles_won", "sum"),
        interceptions=("interceptions", "sum"),
        assists=("assists", "sum"),
        player_goals=("goals", "sum"),
    )
    team_90s = tot.minutes / 990  # 11 players x 90 minutes
    out = pd.DataFrame(index=tot.index)
    out["players_used"] = tot.players_used
    out["tackles_won_per90"] = tot.tackles_won / team_90s
    out["interceptions_per90"] = tot.interceptions / team_90s
    out["assisted_goal_share"] = tot.assists / tot.player_goals

    # Minutes-weighted squad age.
    p["age_x_min"] = p.age * p.minutes
    out["avg_age_minutes_weighted"] = (p.groupby(["league", "squad"]).age_x_min.sum()
                                       / tot.minutes)
    # Share of minutes played by the 11 most-used players (higher = less rotation).
    top11 = (p.sort_values("minutes", ascending=False)
              .groupby(["league", "squad"]).head(11)
              .groupby(["league", "squad"]).minutes.sum())
    out["top11_minutes_share"] = top11 / tot.minutes
    # Share of the team's player goals scored by its top scorer (higher = more reliant on one player).
    out["top_scorer_goal_share"] = (p.groupby(["league", "squad"]).goals.max()
                                    / tot.player_goals)
    out = out.reset_index().rename(columns={"squad": "fbref_squad"})
    return out


# Features z-scored within league. Every one of these is a rate/share, not a season total.
PROFILE_FEATURES = [
    "points_per_game", "goals_for_pg", "goals_against_pg", "clean_sheet_pct",
    "shots_for_pg", "shots_against_pg", "sot_for_pg", "sot_against_pg",
    "shot_share", "sot_share", "corners_for_pg", "corner_share",
    "shot_accuracy", "goals_per_shot", "goals_per_sot", "opp_goals_per_sot",
    "fouls_pg", "fouls_drawn_pg", "yellows_pg", "reds_pg",
    "first_half_goal_share", "home_ppg", "away_ppg",
    "tackles_won_per90", "interceptions_per90", "assisted_goal_share",
    "avg_age_minutes_weighted", "top11_minutes_share", "top_scorer_goal_share",
]

# Each tag: every condition must hold. ("feature", +1) means z >= TAG_Z; ("feature", -1) means z <= -TAG_Z.
TAG_RULES = {
    "territorially_dominant": [("shot_share", +1), ("corner_share", +1)],
    "high_shot_volume": [("shots_for_pg", +1), ("sot_for_pg", +1)],
    "clinical_finishing": [("goals_per_sot", +1)],
    "wasteful_finishing": [("goals_per_sot", -1)],
    "restricts_chances": [("shots_against_pg", -1), ("sot_against_pg", -1)],
    "concedes_many_chances": [("shots_against_pg", +1)],
    "active_ball_winning": [("tackles_won_per90", +1), ("interceptions_per90", +1)],
    "corner_heavy": [("corners_for_pg", +1)],
    "physical_combative": [("fouls_pg", +1), ("yellows_pg", +1)],
    "fast_starters": [("first_half_goal_share", +1)],
    "strong_home_side": [("home_ppg", +1)],
    "young_squad": [("avg_age_minutes_weighted", -1)],
    "experienced_squad": [("avg_age_minutes_weighted", +1)],
    "settled_eleven": [("top11_minutes_share", +1)],
    "heavy_rotation": [("top11_minutes_share", -1)],
    "reliant_on_top_scorer": [("top_scorer_goal_share", +1)],
    "goals_spread_out": [("top_scorer_goal_share", -1)],
}


def add_league_z(df):
    for f in PROFILE_FEATURES:
        grp = df.groupby("league")[f]
        df[f"z_{f}"] = (df[f] - grp.transform("mean")) / grp.transform("std", ddof=0)
    return df


def add_tags(df):
    def tags_for(row):
        hits = []
        for tag, conds in TAG_RULES.items():
            if all(pd.notna(row[f"z_{f}"]) and sign * row[f"z_{f}"] >= TAG_Z
                   for f, sign in conds):
                hits.append(tag)
        return ";".join(hits)
    df["style_tags"] = df.apply(tags_for, axis=1)
    return df


def validate(matches, club_rows, clubs):
    counts = clubs.groupby("league").size().to_dict()
    assert counts == EXPECTED_CLUBS, f"club counts {counts}"
    bad = clubs[clubs.games != clubs.league.map(EXPECTED_GAMES)]
    assert bad.empty, f"unexpected games played:\n{bad[['league', 'team', 'games']]}"
    by_league = clubs.groupby("league")[["goals_for", "goals_against"]].sum()
    assert (by_league.goals_for == by_league.goals_against).all(), "goals for != against"
    missing = club_rows[~club_rows.has_stats]
    if not missing.empty:
        print("Matches left out of per-game stats (result/points still counted):")
        for _, x in missing[missing.is_home].iterrows():
            print(f"  {x.league} {x.date} {x.team} v {x.opponent} ({x.gf}-{x.ga})")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    name_map = pd.read_csv(NAME_MAP)
    assert len(name_map) == 96 and not name_map.duplicated(["league", "football_data_name"]).any()

    matches = load_matches(name_map)
    rows = club_match_rows(matches)
    clubs = aggregate_matches(rows)
    validate(matches, rows, clubs)

    clubs = clubs.rename(columns={"team": "football_data_name"}).merge(
        name_map[["league", "football_data_name", "fbref_squad", "club"]],
        on=["league", "football_data_name"], how="left", validate="one_to_one")
    assert clubs.club.notna().all(), "match-file club missing from name map"
    front = ["league", "club", "football_data_name", "fbref_squad"]
    clubs = clubs[front + [c for c in clubs.columns if c not in front]]
    clubs.round(4).to_csv(OUT_DIR / "club_match_averages_2024_25.csv", index=False)

    players = aggregate_players(name_map)
    profiles = clubs.merge(players, on=["league", "fbref_squad"], how="outer",
                           validate="one_to_one", indicator=True)
    unmatched = profiles[profiles._merge != "both"]
    assert unmatched.empty, f"name-map join failed:\n{unmatched[['league', 'club', 'fbref_squad']]}"
    profiles = add_tags(add_league_z(profiles.drop(columns="_merge")))
    profiles = profiles.sort_values(["league", "points_per_game"], ascending=[True, False])
    profiles.round(4).to_csv(OUT_DIR / "club_profiles_2024_25.csv", index=False)

    print(f"Wrote {len(clubs)} clubs -> {OUT_DIR.relative_to(ROOT)}/")
    print(profiles[["league", "club", "points_per_game", "style_tags"]].to_string(index=False))


if __name__ == "__main__":
    main()
