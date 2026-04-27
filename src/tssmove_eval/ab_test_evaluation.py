import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Config
# ----------------------------
EXCEL_FILE = "data/ab_test_voting_results.xlsx"   # change this
OUTPUT_DIR = Path("charts")
OUTPUT_DIR.mkdir(exist_ok=True)

RUN_ORDER = ["run_v2", "run_v3", "original", "chatgpt_bezug", "run_fid"]

# ----------------------------
# Load data
# ----------------------------
df = pd.read_excel(EXCEL_FILE)

# Normalize text
df["Bewertung"] = df["Bewertung"].str.lower().str.strip()
df["Variante_A"] = df["Variante_A"].str.strip()
df["Variante_B"] = df["Variante_B"].str.strip()

# Keep only valid votes
df = df[df["Bewertung"].isin(["antwort a", "antwort b", "gleichwertig"])].copy()

# Remove self-comparisons if any
df = df[df["Variante_A"] != df["Variante_B"]].copy()

# Determine winner and loser.
# For ties, winner and loser are NaN.
df["winner"] = np.select(
    [
        df["Bewertung"] == "antwort a",
        df["Bewertung"] == "antwort b"
    ],
    [
        df["Variante_A"],
        df["Variante_B"]
    ],
    default=np.nan
)

df["loser"] = np.select(
    [
        df["Bewertung"] == "antwort a",
        df["Bewertung"] == "antwort b"
    ],
    [
        df["Variante_B"],
        df["Variante_A"]
    ],
    default=np.nan
)

df["is_tie"] = df["Bewertung"] == "gleichwertig"

# Canonical unordered pair label
df["pair"] = df.apply(
    lambda row: " vs ".join(sorted([row["Variante_A"], row["Variante_B"]])),
    axis=1
)


# ----------------------------
# 1. Global run preference
# ----------------------------
# Ties are not assigned to either run, but shown separately.
global_win_counts = (
    df.loc[~df["is_tie"], "winner"]
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

tie_count = df["is_tie"].sum()

global_counts = pd.concat([
    global_win_counts,
    pd.Series({"tie": tie_count})
])

global_pct = global_counts / global_counts.sum() * 100

plt.figure(figsize=(8, 5))
bars = plt.bar(global_counts.index, global_counts.values)

plt.title("Global Run Preference Including Ties")
plt.ylabel("Number of votes")
plt.xlabel("Preferred run")
plt.xticks(rotation=30, ha="right")

for bar, pct in zip(bars, global_pct):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{pct:.1f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "global_run_preference_with_ties.png", dpi=200)
plt.close()


# ----------------------------
# 2. Pairwise run preferences including ties
# ----------------------------
# Count wins by pair and winner
pairwise_wins = (
    df.loc[~df["is_tie"]]
    .groupby(["pair", "winner"])
    .size()
    .unstack(fill_value=0)
)

pairwise_wins = pairwise_wins.reindex(columns=RUN_ORDER, fill_value=0)

# Count ties by pair
pairwise_ties = (
    df.loc[df["is_tie"]]
    .groupby("pair")
    .size()
    .rename("tie")
)

# Combine wins + ties
pairwise_counts = pairwise_wins.join(pairwise_ties, how="outer").fillna(0)

# Ensure integer counts
pairwise_counts = pairwise_counts.astype(int)

# Sort pairs alphabetically
pairwise_counts = pairwise_counts.sort_index()

# Convert to percentages within each pair
pairwise_pct = pairwise_counts.div(pairwise_counts.sum(axis=1), axis=0) * 100

PLOT_COLUMNS = RUN_ORDER + ["tie"]

plt.figure(figsize=(10, max(5, len(pairwise_pct) * 0.5)))

left = pd.Series(0.0, index=pairwise_pct.index)

for col in PLOT_COLUMNS:
    values = pairwise_pct[col]

    plt.barh(
        pairwise_pct.index,
        values,
        left=left,
        label=col
    )

    # Add percentage labels
    for i, value in enumerate(values):
        if value > 3:
            plt.text(
                left.iloc[i] + value / 2,
                i,
                f"{value:.0f}%",
                ha="center",
                va="center",
                fontsize=8,
                color="white"
            )

    left += values

plt.title("Pairwise Run Preferences Including Ties")
plt.xlabel("Share within pair (%)")
plt.ylabel("Run pair")
plt.xlim(0, 100)
plt.legend(title="Result", bbox_to_anchor=(1.02, 1), loc="upper left")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "pairwise_run_preferences_with_ties.png", dpi=200)
plt.close()


# ----------------------------
# 3. One-vs-all-others with wins, losses, ties
# ----------------------------
# Count appearances of each run in either A or B
appearances = (
    pd.concat([df["Variante_A"], df["Variante_B"]])
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

wins = (
    df.loc[~df["is_tie"], "winner"]
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

losses = (
    df.loc[~df["is_tie"], "loser"]
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

# Each tie counts as one tie appearance for both involved runs
tie_appearances = (
    pd.concat([
        df.loc[df["is_tie"], "Variante_A"],
        df.loc[df["is_tie"], "Variante_B"]
    ])
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

one_vs_all = pd.DataFrame({
    "wins": wins,
    "losses": losses,
    "ties": tie_appearances,
    "appearances": appearances
})

one_vs_all["win_rate_including_ties"] = (
    one_vs_all["wins"] / one_vs_all["appearances"] * 100
)

one_vs_all["tie_rate"] = (
    one_vs_all["ties"] / one_vs_all["appearances"] * 100
)

one_vs_all["loss_rate"] = (
    one_vs_all["losses"] / one_vs_all["appearances"] * 100
)

# Optional: win rate excluding ties
one_vs_all["win_rate_excluding_ties"] = (
    one_vs_all["wins"] /
    (one_vs_all["wins"] + one_vs_all["losses"])
    * 100
).replace([np.inf, -np.inf], np.nan)


# Stacked bar: wins, losses, ties as percentage of appearances
plot_rates = one_vs_all[
    ["win_rate_including_ties", "loss_rate", "tie_rate"]
].rename(columns={
    "win_rate_including_ties": "wins",
    "loss_rate": "losses",
    "tie_rate": "ties"
})

plt.figure(figsize=(8, 5))

bottom = np.zeros(len(plot_rates))

for col in ["wins", "losses", "ties"]:
    values = plot_rates[col].values

    bars = plt.bar(
        plot_rates.index,
        values,
        bottom=bottom,
        label=col
    )

    for bar, value, btm in zip(bars, values, bottom):
        if value > 3:
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                btm + value / 2,
                f"{value:.0f}%",
                ha="center",
                va="center",
                fontsize=8,
                color="white"
            )

    bottom += values

plt.title("One-vs-All-Others Results Including Ties")
plt.ylabel("Share of appearances (%)")
plt.xlabel("Run")
plt.ylim(0, 100)
plt.xticks(rotation=30, ha="right")
plt.legend(title="Result")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "one_vs_all_with_ties.png", dpi=200)
plt.close()


# ----------------------------
# Optional: one-vs-all win rate only
# ----------------------------
plt.figure(figsize=(8, 5))
bars = plt.bar(
    one_vs_all.index,
    one_vs_all["win_rate_including_ties"]
)

plt.title("One-vs-All-Others Win Rate Including Ties")
plt.ylabel("Win rate (%)")
plt.xlabel("Run")
plt.ylim(0, 100)
plt.xticks(rotation=30, ha="right")

for bar, run in zip(bars, one_vs_all.index):
    wr = one_vs_all.loc[run, "win_rate_including_ties"]
    w = one_vs_all.loc[run, "wins"]
    n = one_vs_all.loc[run, "appearances"]

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{wr:.1f}%\n{w}/{n}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "one_vs_all_win_rate_including_ties.png", dpi=200)
plt.close()


# ----------------------------
# Print summary tables
# ----------------------------
print("\nGlobal preference counts including ties:")
print(global_counts)

print("\nPairwise counts including ties:")
print(pairwise_counts)

print("\nPairwise percentages including ties:")
print(pairwise_pct.round(1))

print("\nOne-vs-all summary:")
print(one_vs_all.round(2))

print(f"\nCharts saved to: {OUTPUT_DIR.resolve()}")