from pathlib import Path
from urllib.request import urlretrieve
import nflreadpy as nfl

NFL_FOLDER = Path(__file__).parent

files = {
    "Player weekly stats": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "stats_player/stats_player_week_2026.csv",
        "stats_player_week_2026.csv"
    ),

    "Team regular season stats": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "stats_team/stats_team_reg_2026.csv",
        "stats_team_reg_2026.csv"
    ),

    "Play-by-play": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "pbp/play_by_play_2026.csv",
        "play_by_play_2026.csv"
    ),

    "Snap counts": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "snap_counts/snap_counts_2026.csv",
        "snap_counts_2026.csv"
    ),

    "Depth charts": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "depth_charts/depth_charts_2026.csv",
        "depth_charts_2026.csv"
    ),

    "Injuries": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "injuries/injuries_2026.csv",
        "injuries_2026.csv"
    ),

    "FTN charting": (
        "https://github.com/nflverse/nflverse-data/releases/download/"
        "ftn_charting/ftn_charting_2026.csv",
        "ftn_charting_2026.csv"
    ),
}

print("\nUpdating NFL data...\n")

for name, (url, filename) in files.items():
    destination = NFL_FOLDER / filename

    try:
        print(f"Downloading {name}...")
        urlretrieve(url, destination)
        print(f"✓ {name}")
    except Exception as error:
        print(f"✗ {name}")
        print(f"  Error: {error}")

print("\nUpdating Next Gen Stats...\n")

ngs_files = {
    "passing": "ngs_passing.csv",
    "receiving": "ngs_receiving.csv",
    "rushing": "ngs_rushing.csv"
}

for stat_type, filename in ngs_files.items():
    try:
        print(f"Downloading NGS {stat_type}...")

        data = nfl.load_nextgen_stats(
            seasons=2026,
            stat_type=stat_type
        )

        destination = NFL_FOLDER / filename
        data.write_csv(destination)

        print(f"✓ NGS {stat_type}")

    except Exception as error:
        print(f"✗ NGS {stat_type}")
        print(f"  Error: {error}")

# Players
try:
    print("Downloading players...")

    players = nfl.load_players()

    destination = NFL_FOLDER / "players.csv"
    players.write_csv(destination)

    print("✓ Players")

except Exception as error:
    print("✗ Players")
    print(f"  Error: {error}")


# Teams, colors, and logos
try:
    print("Downloading teams/colors/logos...")

    teams = nfl.load_teams()

    destination = NFL_FOLDER / "teams_colors_logos.csv"
    teams.write_csv(destination)

    print("✓ Teams/colors/logos")

except Exception as error:
    print("✗ Teams/colors/logos")
    print(f"  Error: {error}")


print("\nNFL data update finished!")

