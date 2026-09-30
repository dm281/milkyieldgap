# Data folder

Nothing that identifies a farm belongs here.

| Path | What belongs | What does not |
|---|---|---|
| `raw/` | A `.gitkeep` only | The 4.80 million-row extract, `AccountName`, `HerdCode` |
| `processed/` | A `.gitkeep` only | `lactations_with_farmid`, stacked test-day tables |
| this file | Rules | Crosswalk of HerdCode → FarmID |

The working analysis table is a local JMP/CSV copy named `lactations_with_farmid`. `AccountName` and `HerdCode` were removed from that copy. The 320-row `herd_crosswalk` stays in the Elanco workspace with the original extract.

Raw → code → processed. The original extract is never overwritten.
