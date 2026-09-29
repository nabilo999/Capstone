# Column Explanations

Quick reference for the raw headers in `big5_player_stats_2024_2025.csv` and `football_data_premier_league_2024_25.csv`.

## Player performance — 2024–25 (88 columns)

| Column | Meaning |
| --- | --- |
| `player` | Player name. |
| `player_id` | Source player identifier. |
| `ranker` | Source-table row rank. |
| `nationality` | Player nationality code. |
| `position` | Listed playing position. |
| `squad` | Club/team name. |
| `age` | Player age during the season. |
| `birth_year` | Player birth year. |
| `games` | Appearances. |
| `games_starts` | Starts. |
| `minutes` | Minutes played. |
| `minutes_90s` | Minutes played expressed as 90-minute units. |
| `goals` | Non-goalkeeper goals scored. |
| `assists` | Assists. |
| `goals_assists` | Goals plus assists. |
| `goals_pens` | Non-penalty goals. |
| `pens_made` | Penalty kicks scored. |
| `pens_att` | Penalty kicks attempted. |
| `cards_yellow` | Yellow cards. |
| `cards_red` | Red cards. |
| `goals_per90` | Goals per 90 minutes. |
| `assists_per90` | Assists per 90 minutes. |
| `goals_assists_per90` | Goals plus assists per 90 minutes. |
| `goals_pens_per90` | Non-penalty goals per 90 minutes. |
| `goals_assists_pens_per90` | Non-penalty goals plus assists per 90 minutes. |
| `matches` | Source match-link field. |
| `season` | Season label. |
| `league` | League code. |
| `tackles` | Total tackles. |
| `tackles_won` | Tackles won. |
| `tackles_def_3rd` | Tackles in the defensive third. |
| `tackles_mid_3rd` | Tackles in the middle third. |
| `tackles_att_3rd` | Tackles in the attacking third. |
| `challenge_tackles` | Dribblers tackled. |
| `challenges` | Dribbles challenged. |
| `challenge_tackles_pct` | Percentage of dribblers tackled. |
| `challenges_lost` | Dribbles not tackled. |
| `blocks` | Total blocks. |
| `blocked_shots` | Shots blocked. |
| `blocked_passes` | Passes blocked. |
| `interceptions` | Interceptions. |
| `tackles_interceptions` | Tackles plus interceptions. |
| `clearances` | Clearances. |
| `errors` | Errors leading to an opponent shot. |
| `passes_completed` | Completed passes. |
| `passes` | Passes attempted. |
| `passes_pct` | Pass-completion percentage. |
| `passes_total_distance` | Total passing distance. |
| `passes_progressive_distance` | Progressive passing distance. |
| `passes_completed_short` | Completed short passes. |
| `passes_short` | Short passes attempted. |
| `passes_pct_short` | Short pass-completion percentage. |
| `passes_completed_medium` | Completed medium passes. |
| `passes_medium` | Medium passes attempted. |
| `passes_pct_medium` | Medium pass-completion percentage. |
| `passes_completed_long` | Completed long passes. |
| `passes_long` | Long passes attempted. |
| `passes_pct_long` | Long pass-completion percentage. |
| `xg_assist_net` | Expected assisted-goals contribution. |
| `assisted_shots` | Key passes / shots assisted. |
| `passes_into_final_third` | Completed passes into the final third. |
| `passes_into_penalty_area` | Completed passes into the penalty area. |
| `crosses_into_penalty_area` | Completed crosses into the penalty area. |
| `shots` | Shots taken. |
| `shots_on_target` | Shots on target. |
| `shots_on_target_pct` | Percentage of shots on target. |
| `shots_per90` | Shots per 90 minutes. |
| `shots_on_target_per90` | Shots on target per 90 minutes. |
| `goals_per_shot` | Goals per shot. |
| `goals_per_shot_on_target` | Goals per shot on target. |
| `gk_games` | Goalkeeper appearances. |
| `gk_games_starts` | Goalkeeper starts. |
| `gk_minutes` | Goalkeeper minutes played. |
| `gk_goals_against` | Goals conceded while goalkeeping. |
| `gk_goals_against_per90` | Goals conceded per 90 goalkeeper minutes. |
| `gk_shots_on_target_against` | Shots on target faced. |
| `gk_saves` | Saves made. |
| `gk_save_pct` | Save percentage. |
| `gk_wins` | Goalkeeper match wins. |
| `gk_ties` | Goalkeeper match draws. |
| `gk_losses` | Goalkeeper match losses. |
| `gk_clean_sheets` | Goalkeeper clean sheets. |
| `gk_clean_sheets_pct` | Clean-sheet percentage. |
| `gk_pens_att` | Penalty kicks faced. |
| `gk_pens_allowed` | Penalty kicks conceded. |
| `gk_pens_saved` | Penalty kicks saved. |
| `gk_pens_missed` | Penalty kicks missed by opponents. |
| `gk_pens_save_pct` | Penalty-save percentage. |

## Match results — Premier League 2024–25 (120 columns)

### Match details and match statistics

| Column | Meaning |
| --- | --- |
| `Div` | League division code. |
| `Date` | Match date. |
| `Time` | Kickoff time. |
| `HomeTeam` | Home-team name. |
| `AwayTeam` | Away-team name. |
| `FTHG` | Full-time home goals. |
| `FTAG` | Full-time away goals. |
| `FTR` | Full-time result (`H`, `D`, or `A`). |
| `HTHG` | Half-time home goals. |
| `HTAG` | Half-time away goals. |
| `HTR` | Half-time result (`H`, `D`, or `A`). |
| `Referee` | Match referee. |
| `HS` | Home-team shots. |
| `AS` | Away-team shots. |
| `HST` | Home-team shots on target. |
| `AST` | Away-team shots on target. |
| `HF` | Home-team fouls committed. |
| `AF` | Away-team fouls committed. |
| `HC` | Home-team corners. |
| `AC` | Away-team corners. |
| `HY` | Home-team yellow cards. |
| `AY` | Away-team yellow cards. |
| `HR` | Home-team red cards. |
| `AR` | Away-team red cards. |

### Opening 1X2 odds

| Column | Meaning |
| --- | --- |
| `B365H` | Bet365 opening home-win odds. |
| `B365D` | Bet365 opening draw odds. |
| `B365A` | Bet365 opening away-win odds. |
| `BWH` | Bwin opening home-win odds. |
| `BWD` | Bwin opening draw odds. |
| `BWA` | Bwin opening away-win odds. |
| `BFH` | Betfair opening home-win odds. |
| `BFD` | Betfair opening draw odds. |
| `BFA` | Betfair opening away-win odds. |
| `PSH` | Pinnacle opening home-win odds. |
| `PSD` | Pinnacle opening draw odds. |
| `PSA` | Pinnacle opening away-win odds. |
| `WHH` | William Hill opening home-win odds. |
| `WHD` | William Hill opening draw odds. |
| `WHA` | William Hill opening away-win odds. |
| `1XBH` | 1xBet opening home-win odds. |
| `1XBD` | 1xBet opening draw odds. |
| `1XBA` | 1xBet opening away-win odds. |
| `MaxH` | Highest opening home-win odds. |
| `MaxD` | Highest opening draw odds. |
| `MaxA` | Highest opening away-win odds. |
| `AvgH` | Average opening home-win odds. |
| `AvgD` | Average opening draw odds. |
| `AvgA` | Average opening away-win odds. |
| `BFEH` | Betfair Exchange opening home-win odds. |
| `BFED` | Betfair Exchange opening draw odds. |
| `BFEA` | Betfair Exchange opening away-win odds. |

### Opening over/under and Asian-handicap odds

| Column | Meaning |
| --- | --- |
| `B365>2.5` | Bet365 opening over-2.5-goals odds. |
| `B365<2.5` | Bet365 opening under-2.5-goals odds. |
| `P>2.5` | Pinnacle opening over-2.5-goals odds. |
| `P<2.5` | Pinnacle opening under-2.5-goals odds. |
| `Max>2.5` | Highest opening over-2.5-goals odds. |
| `Max<2.5` | Highest opening under-2.5-goals odds. |
| `Avg>2.5` | Average opening over-2.5-goals odds. |
| `Avg<2.5` | Average opening under-2.5-goals odds. |
| `BFE>2.5` | Betfair Exchange opening over-2.5-goals odds. |
| `BFE<2.5` | Betfair Exchange opening under-2.5-goals odds. |
| `AHh` | Opening Asian handicap for the home team. |
| `B365AHH` | Bet365 opening Asian-handicap home odds. |
| `B365AHA` | Bet365 opening Asian-handicap away odds. |
| `PAHH` | Pinnacle opening Asian-handicap home odds. |
| `PAHA` | Pinnacle opening Asian-handicap away odds. |
| `MaxAHH` | Highest opening Asian-handicap home odds. |
| `MaxAHA` | Highest opening Asian-handicap away odds. |
| `AvgAHH` | Average opening Asian-handicap home odds. |
| `AvgAHA` | Average opening Asian-handicap away odds. |
| `BFEAHH` | Betfair Exchange opening Asian-handicap home odds. |
| `BFEAHA` | Betfair Exchange opening Asian-handicap away odds. |

### Closing 1X2 odds

| Column | Meaning |
| --- | --- |
| `B365CH` | Bet365 closing home-win odds. |
| `B365CD` | Bet365 closing draw odds. |
| `B365CA` | Bet365 closing away-win odds. |
| `BWCH` | Bwin closing home-win odds. |
| `BWCD` | Bwin closing draw odds. |
| `BWCA` | Bwin closing away-win odds. |
| `BFCH` | Betfair closing home-win odds. |
| `BFCD` | Betfair closing draw odds. |
| `BFCA` | Betfair closing away-win odds. |
| `PSCH` | Pinnacle closing home-win odds. |
| `PSCD` | Pinnacle closing draw odds. |
| `PSCA` | Pinnacle closing away-win odds. |
| `WHCH` | William Hill closing home-win odds. |
| `WHCD` | William Hill closing draw odds. |
| `WHCA` | William Hill closing away-win odds. |
| `1XBCH` | 1xBet closing home-win odds. |
| `1XBCD` | 1xBet closing draw odds. |
| `1XBCA` | 1xBet closing away-win odds. |
| `MaxCH` | Highest closing home-win odds. |
| `MaxCD` | Highest closing draw odds. |
| `MaxCA` | Highest closing away-win odds. |
| `AvgCH` | Average closing home-win odds. |
| `AvgCD` | Average closing draw odds. |
| `AvgCA` | Average closing away-win odds. |
| `BFECH` | Betfair Exchange closing home-win odds. |
| `BFECD` | Betfair Exchange closing draw odds. |
| `BFECA` | Betfair Exchange closing away-win odds. |

### Closing over/under and Asian-handicap odds

| Column | Meaning |
| --- | --- |
| `B365C>2.5` | Bet365 closing over-2.5-goals odds. |
| `B365C<2.5` | Bet365 closing under-2.5-goals odds. |
| `PC>2.5` | Pinnacle closing over-2.5-goals odds. |
| `PC<2.5` | Pinnacle closing under-2.5-goals odds. |
| `MaxC>2.5` | Highest closing over-2.5-goals odds. |
| `MaxC<2.5` | Highest closing under-2.5-goals odds. |
| `AvgC>2.5` | Average closing over-2.5-goals odds. |
| `AvgC<2.5` | Average closing under-2.5-goals odds. |
| `BFEC>2.5` | Betfair Exchange closing over-2.5-goals odds. |
| `BFEC<2.5` | Betfair Exchange closing under-2.5-goals odds. |
| `AHCh` | Closing Asian handicap for the home team. |
| `B365CAHH` | Bet365 closing Asian-handicap home odds. |
| `B365CAHA` | Bet365 closing Asian-handicap away odds. |
| `PCAHH` | Pinnacle closing Asian-handicap home odds. |
| `PCAHA` | Pinnacle closing Asian-handicap away odds. |
| `MaxCAHH` | Highest closing Asian-handicap home odds. |
| `MaxCAHA` | Highest closing Asian-handicap away odds. |
| `AvgCAHH` | Average closing Asian-handicap home odds. |
| `AvgCAHA` | Average closing Asian-handicap away odds. |
| `BFECAHH` | Betfair Exchange closing Asian-handicap home odds. |
| `BFECAHA` | Betfair Exchange closing Asian-handicap away odds. |
