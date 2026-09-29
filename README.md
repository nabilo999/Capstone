# ScoutIQ

ScoutIQ is a football scouting decision-support prototype. It helps a recruitment team answer three related questions about a player:

1. **Current ability:** What does the player contribute now, relative to players in the same role?
2. **Potential:** Which past players had similar profiles at a similar age, and how did those players develop afterward?
3. **Team fit:** How closely does the player's profile match the style and needs of a selected team?

The project turns season statistics into explainable comparisons and shortlists. It is intended to support scouts and analysts, not to make transfer decisions on their behalf. Scores should show the evidence and assumptions behind them.

## Product idea

A user selects or searches for a player. ScoutIQ presents a position-aware view of the player's recent production, usage and areas of strength. The user can then see historical player comparisons and select a club to review the player's fit with that club's profile.

The three parts share one player-performance foundation, but answer different questions:

| Part | Question | Main inputs | Intended output |
|---|---|---|---|
| Current ability | How strong is the player's recent on-field contribution? | Latest completed season's minutes, production, passing, creation, defending and role | A transparent, position-aware profile and baseline score |
| Historical similarity and potential | What happened to comparable players after a similar season? | Earlier player-seasons, age, position, minutes and performance features, followed by later seasons | Comparable historical players, their subsequent development and an evidence-based potential estimate |
| Team fit | Which clubs' playing profiles appear compatible with this player? | Big Five player-season data aggregated by club, plus 2024–25 match results and available match statistics | Team-style profiles, fit comparisons and a shortlist of clubs to investigate |

The shared sequence is:

```text
Season source data
       |
       v
Validated player-season records and features
       |----------------------|
       v                      v
Current ability       Historical similarity
                              |
                              v
                         Potential

Validated 2024–25 team inputs --> Team profiles --> Team fit
                                             player profile --^
```

## How the three parts work

### Current ability

The current-ability view describes performance in the latest completed season available in this data snapshot, 2024–25. It uses playing time and role-relevant measures such as goals, assists, expected goals, chance creation, passing, ball progression, tackles, interceptions, blocks and clearances.

Raw totals reward players who play more minutes, so the feature pipeline will include per-90 rates and playing-time context. Comparisons should be made within useful role groups and, when appropriate, within league-season groups. The first score will be a documented baseline with visible components, minimum-minute handling and missing-data rules. It will not be presented as an objective or universal measure of talent.

### Historical similarity and potential

Historical similarity starts from a player's season profile, age and position. It finds comparable player-seasons in the earlier seasons, then follows those players into later seasons to measure what happened after the comparison point.

Potential is a forward-looking estimate built from those historical outcomes. The team must define the outcome before training or scoring—for example, change in a role-specific per-90 profile, sustained playing time, or both. The model must only use information available at the historical comparison date. Later seasons must never leak into the similarity inputs for that comparison.

The 2024–25 players can be compared to earlier historical cases, but the current files do not contain their 2025–26 outcomes. Those outcomes cannot be claimed as observed evidence in this version.

### Team fit

Team fit builds a profile for each club in the five leagues using the completed 2024–25 season. Player-season statistics can be grouped by club to describe passing, chance creation, progression and defensive activity. Match records add wins, draws, losses, goals, shots and other available match statistics.

The team profile is compared with a player's role-specific profile. The result should explain which available dimensions match and where they differ. This is a statistical compatibility screen, not proof that a player will succeed in a coach's system. The current sources do not contain a consistent pressure count or verified possession percentage, so ScoutIQ must not label tackles as pressing or infer possession from touches.

## Current data sources

The files staged for the first build are stored in [`data/scoutiq_big5_10_season_sources/`](data/scoutiq_big5_10_season_sources/).

### Big Five player-season statistics, 2015–16 to 2024–25

The project currently uses ten season-specific CSVs from one consistent FBref/Understat combined player-stat dataset. Together they contain about 27,920 player-season rows and 88 fields. Each season file covers England (EPL), Spain (ESP), France (FRA), Germany (GER) and Italy (ITA).

Fields include player and club identifiers, league, season, position, age, birth year, games, starts, minutes, goals, assists, expected goals, passing totals and completion rates, progressive passing, tackles, interceptions, blocks, clearances, shooting and goalkeeper measures. The same source schema across seasons makes historical comparisons more consistent than mixing separate league archives.

Source: [FBref/Understat combined player statistics](https://huggingface.co/datasets/aloobun/fbref_understat_combined).

### Player bio extracts, 2015–16 to 2024–25

Ten matching CSVs hold selected fields from the same player-season source: player name, player ID, nationality, position, club, age, birth year, season and league. These are currently identity and basic biographical fields. They do **not** contain height, weight, preferred foot or full date of birth. The folder's existing `biometrics` name is retained for continuity, but it should not be interpreted as a physical-measurement dataset.

The player identifier must be audited for continuity across seasons before it is trusted as a join key. If the project later needs physical measurements, a real source with documented coverage and joinable identifiers must be selected; those fields are not assumed or fabricated in this version.

### Big Five match results, 2024–25

Five CSVs from Football-Data contain all 1,752 completed fixtures: 380 Premier League, 380 La Liga, 380 Serie A, 306 Bundesliga and 306 Ligue 1 matches. Results include home and away teams, full-time and half-time scores, result, shots, shots on target, fouls, corners and cards. The files also include bookmaker odds; odds are outside the current product scope and should be excluded from the team-fit feature set unless the project explicitly adds a separate outcome-prediction task.

Sources: [Football-Data downloads](https://www.football-data.co.uk/data.php) and [Football-Data column notes](https://www.football-data.co.uk/notes.txt).


## Build plan

The sequenced team plan is in [`PROJECT_PLAN.md`](PROJECT_PLAN.md). Start with the data audit and model definitions, then build the player and team outputs on shared, validated features. Keep the initial scores simple and test them against held-out seasons before presenting them as useful scouting signals.

## Current project files

```text
data/
└── scoutiq_big5_10_season_sources/
    ├── big5_player_performance/       # 10 season CSVs, 2015–16 to 2024–25
    ├── big5_player_biometrics/        # 10 identity/basic-bio extracts
    └── top5_match_results_2024_25/    # 5 league match CSVs
```

The earlier `data/scoutiq_week2_sources/` files remain from the first, narrower data plan. The current model plan uses `scoutiq_big5_10_season_sources/` as its starting point.
