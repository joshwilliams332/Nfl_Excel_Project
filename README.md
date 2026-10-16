# 2026 NFL Fantasy Data Pipeline

An Excel + Python workflow that pulls 2026 NFL data from [nflverse](https://github.com/nflverse/nflverse-data), loads it into an Excel data model with Power Query, and summarizes weekly fantasy points with Power Pivot. One button in Excel refreshes everything.

## How it works

1. **`update_nfl_data.py`** downloads the latest 2026 season files: weekly player stats, team stats, play-by-play, snap counts, depth charts, injuries, FTN charting, Next Gen Stats (passing, receiving, rushing), players, and teams. Most come straight from nflverse releases; Next Gen Stats, players and teams come through [`nflreadpy`](https://github.com/nflverse/nflreadpy).
2. **`2026 Fantasy Points Pivot.xlsm`** connects to those CSVs with Power Query and loads them into the Excel data model. A pivot table shows PPR fantasy points for every player by week.
3. The workbook's **`UpdateNFLData`** macro (VBA) runs the Python script, waits for it to finish, then refreshes every Power Query connection, so the pivot updates in one click.

## Files

| File | What it is |
| --- | --- |
| `update_nfl_data.py` | Downloads the raw data CSVs into this folder |
| `2026 Fantasy Points Pivot.xlsm` | Power Query + Power Pivot workbook with the one-click update macro |
| `2026 QB Stats.xlsx` | Weekly quarterback stat lines (completions, yards, TDs, INTs, sacks, and more) |
| `requirements.txt` | Python dependency |

The raw CSVs aren't committed because they're large (about 93 MB) and the script recreates them.

## Run it

```bash
pip install -r requirements.txt
python update_nfl_data.py
```

Then open the `.xlsm` workbook, enable macros, and run `UpdateNFLData` (or click **Data → Refresh All** after running the script yourself).

The macro and the Power Query sources point to the folder where I keep the project. If you clone it somewhere else, update the script path in the `NFLDataUpdater` module and the query sources under **Data → Queries & Connections**.

## Tools

Python (nflreadpy, urllib) · Excel Power Query · Power Pivot / data model · Pivot tables · VBA

Data: [nflverse](https://github.com/nflverse), licensed under CC-BY 4.0 by its contributors.
