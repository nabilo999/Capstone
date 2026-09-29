# 2024–25 club profiles

Per-club averages and style tags for all 96 Big Five clubs, built from the full 2024–25 season.

```bash
python3 team_profiles/build_club_profiles.py   # from the repo root; needs pandas
```

| File | Contents |
|---|---|
| `club_name_map.csv` | Football-Data name ↔ FBref squad name ↔ display name, for all 96 clubs (checked by hand) |
| `output/club_match_averages_2024_25.csv` | Per-club match averages (match files only) |
| `output/club_profiles_2024_25.csv` | Match averages + player-file aggregates + `z_*` within-league z-scores + `style_tags` |

## Data limits
- **The player files have no passing, possession, tackles-by-third, clearance, block or cross data.** Those columns are blank in all 10 seasons. From the player file, only `tackles_won`, `interceptions`, goals, assists, minutes and age are usable at team level. The profiles therefore can't describe build-up style (short vs long, possession).
- Bookmaker odds are dropped, following PROJECT_PLAN.md.
- One match has no stats: Union Berlin v Bochum on 14/12/2024, which was abandoned and awarded 0–2. It counts toward results and points but is left out of the per-game stats, so Union Berlin and Bochum have 33 matches with stats.

## Features
Rates and shares come from season sums (Σnumerator / Σdenominator), not from averaging per-match percentages. "pg" means per game.

| Feature | Formula |
|---|---|
| `points_per_game`, `home_ppg`, `away_ppg` | points / games (3 for a win, 1 for a draw) |
| `goals_for_pg`, `goals_against_pg`, `goal_diff_pg` | goals / games |
| `clean_sheet_pct`, `failed_to_score_pct` | share of games with 0 conceded / 0 scored |
| `shots_for_pg`, `shots_against_pg`, `sot_for_pg`, `sot_against_pg` | shots (on target) / games with stats |
| `shot_share`, `sot_share`, `corner_share` | club's ÷ (club's + opponents'). Share of the game's shots/corners. |
| `corners_for_pg`, `corners_against_pg` | corners / games with stats |
| `shot_accuracy` | Σshots on target / Σshots |
| `goals_per_shot`, `goals_per_sot` | Σgoals / Σshots, Σgoals / Σshots on target |
| `opp_goals_per_sot` | Σconceded / Σshots on target faced (lower = the goalkeeper/defence stops more) |
| `fouls_pg`, `fouls_drawn_pg`, `yellows_pg`, `reds_pg` | count / games with stats |
| `first_half_goal_share`, `first_half_conceded_share` | Σhalf-time goals / Σfull-time goals |
| `points_rescued_when_trailing_ht_pg` | points per game in games where the club trailed at half-time (see `games_trailing_ht` for the sample size) |
| `tackles_won_per90`, `interceptions_per90` | Σplayer count / (Σplayer minutes / 990) |
| `assisted_goal_share` | Σassists / Σplayer goals |
| `avg_age_minutes_weighted` | Σ(age × minutes) / Σminutes |
| `top11_minutes_share` | minutes of the 11 most-used players / all minutes (higher = less rotation) |
| `top_scorer_goal_share` | top scorer's goals / Σplayer goals |
| `players_used` | distinct players who appeared for the club |

## Within-league scaling
Every feature above also has a `z_` column: `(club value − league mean) / league std`, computed separately for each league. For example, `z_shots_for_pg = 1.5` means the club took 1.5 standard deviations more shots than the average club in its own league. This stops league-wide differences (e.g. more shots in the Bundesliga) from dominating the comparison.

## Style tags
A club gets a tag when **every** condition is met. "High" means z ≥ 0.75 and "low" means z ≤ −0.75, both within the club's league. A club can have any number of tags, including none. Rules and thresholds are in `TAG_RULES` / `TAG_Z` in the script, so the team can change them.

| Tag | Condition |
|---|---|
| `territorially_dominant` | high shot share and high corner share |
| `high_shot_volume` | high shots pg and high shots on target pg |
| `clinical_finishing` / `wasteful_finishing` | high / low goals per shot on target |
| `restricts_chances` | low shots against pg and low shots on target against pg |
| `concedes_many_chances` | high shots against pg |
| `active_ball_winning` | high tackles won per 90 and high interceptions per 90 (not labelled "pressing"; there's no pressure data) |
| `corner_heavy` | high corners pg |
| `physical_combative` | high fouls pg and high yellows pg |
| `fast_starters` | high first-half share of goals |
| `strong_home_side` | high home points per game |
| `young_squad` / `experienced_squad` | low / high minutes-weighted age |
| `settled_eleven` / `heavy_rotation` | high / low top-11 minutes share |
| `reliant_on_top_scorer` / `goals_spread_out` | high / low top scorer's goal share |

Territorial dominance (out-shooting opponents and winning more corners) usually goes with teams that keep the ball, but it isn't a possession measure and shouldn't be reported as one.
