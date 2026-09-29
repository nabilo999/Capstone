# ScoutIQ build plan

## Phase 1 — Agree the MVP and data contract [done]

## Phase 2 — Audit and prepare the source data

Review all ten performance files and five match files. Confirm season and league coverage, row counts, column consistency, blank rates, duplicate records, impossible values, repeated player IDs, club-name spelling and whether player IDs remain stable across seasons. Check source notes and document retrieval dates and dataset versions.

Create a reproducible import step that reads the original CSVs and writes validated prepared tables separately. Keep the raw files untouched. Create a data dictionary for fields the model will use. Explicitly list unavailable inputs such as height, full date of birth, pressing counts and team possession percentage.

**Done when:** import can be rerun from the raw folder; coverage checks pass or known exceptions are documented; and player-season records can be traced to their source file and row.

## Phase 3 — Build shared player features

Select only fields needed for the MVP. Create playing-time measures and per-90 rates, such as goals plus assists per 90, key passes per 90, passing completion, progressive actions per 90 and defensive actions per 90. Separate goalkeepers from outfield roles and compare players within useful position groups. Apply a minutes threshold and make low-minute cases visible instead of treating small samples like full seasons.

Scale or rank features only after the comparison population is defined. Keep source totals alongside derived values, and write the formula, direction, units and missing-data handling for each new feature.

**Done when:** a reproducible feature table exists for all seasons and leagues, with unit checks and examples manually checked against source rows.

## Phase 4 — Create the current-ability baseline

Use 2024–25 player features to build a transparent baseline for current ability. Define role-specific feature groups and weights with the team. Show component scores, minutes/sample context and the underlying statistics so users can understand why a player ranks where they do. Keep the first version interpretable; do not tune weights to produce a preferred ranking.

Compare rankings with basic football sanity checks: position, minutes, standout contributions and known role differences. Ask project teammates or football-aware reviewers to inspect samples and record disagreements.

**Done when:** the team can select a player and explain the baseline score from displayed components. Document the weighting and known blind spots.

## Phase 5 — Build historical similarity and evaluate it over time

Use player-season features from earlier seasons to find similar historical profiles. Choose a distance or nearest-neighbor method, specify role/age/league handling, and test several examples with human review. Similarity should identify comparable profiles, not claim that two players are identical.

Run a temporal backtest: pretend a historical season is the present, build comparisons using only data available up to that season, and compare against later seasons. Use seasons with a complete follow-up period. Check that the comparison logic never uses future data when identifying neighbors.

**Done when:** the similarity output shows comparable historical players, why they matched and a retrospective report of how useful those comparisons were.

## Phase 6 — Define and build the potential estimate

Define “potential” as an observable future outcome before training a model. A practical first option is improvement in a position-aware feature profile over the following season or seasons, with minutes and continued league coverage reported separately. Decide how to treat players who leave the Big Five, do not play, or have incomplete follow-up data.

Use historical similar-player outcomes to estimate a range or distribution, not just a single deterministic number. Evaluate by holding out later seasons, compare with a simple baseline, check calibration and inspect cases where the estimate is misleading. For current 2024–25 players, present the result as an estimate based on earlier analogues; their later outcomes are not present in the current source snapshot.

**Done when:** a user can see the outcome definition, historical comparison group, follow-up window, uncertainty/coverage and backtest performance alongside a potential estimate.

## Phase 7 — Build 2024–25 team profiles and team fit

Aggregate the Big Five player features by league and club to create club profiles. Use correct denominators: calculate completion rates from summed completed and attempted passes, and calculate per-90 rates from the relevant minutes. Bring in Football-Data results for matches, wins, draws, losses, goals, shots, cards and other available match context. Exclude bookmaker odds from ScoutIQ features.

Compare a player's role-specific features with the team profile. Design the fit output to show matching strengths and mismatches, and test it with several clubs and players. Do not infer pressing or possession from proxy fields. Decide whether the available team profile is useful enough for an MVP, and record where better tactical data would improve it.

**Done when:** every team profile can be traced to source rows and formulas, has the right league/season, and fit results include an understandable breakdown.

## Phase 8 — Integrate the user experience

Build the simplest interface that supports the agreed demo: search/select a player, review current ability, open historical comparisons and potential evidence, then select a team to inspect fit. Include league, season, position and minutes context. Add clear empty states where data is missing and a source/method view for important fields.

Connect the screen to the prepared data and model outputs rather than embedding hand-entered rankings. Keep the player and team workflows visually distinct while allowing a user to move from one to the other.

**Done when:** a teammate can run the prototype and complete the full player-to-team-fit workflow without manually editing data or code.

## Phase 9 — Validate, revise and prepare the capstone demo

Test the pipeline from raw CSVs through displayed results. Check missing values, duplicate players, transferred players, low minutes, goalkeepers, league changes and records with no later season. Have teammates review explanations and score behavior. Fix issues found and keep a short record of decisions and revisions.

Prepare a demo with a small set of players and teams, show how each score is built, report retrospective evaluation honestly, and describe limitations. Package setup instructions, source links, data definitions, model assumptions and a reproducible run path.

**Done when:** a fresh team member can follow the setup instructions, rerun the app or notebook, reproduce the demo outputs and explain what the prototype can and cannot conclude.



