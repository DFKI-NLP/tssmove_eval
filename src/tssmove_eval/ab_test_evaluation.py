import pandas as pd
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
df = df[df["Bewertung"].isin(["antwort a", "antwort b"])].copy()

# Determine selected/winning run and losing run
df["winner"] = df.apply(
    lambda row: row["Variante_A"] if row["Bewertung"] == "antwort a" else row["Variante_B"],
    axis=1
)

df["loser"] = df.apply(
    lambda row: row["Variante_B"] if row["Bewertung"] == "antwort a" else row["Variante_A"],
    axis=1
)

# Create unordered pair label, e.g. "chatgpt vs run_v2"
df["pair"] = df.apply(
    lambda row: " vs ".join(sorted([row["Variante_A"], row["Variante_B"]])),
    axis=1
)

# Remove self-comparisons if any
df = df[df["Variante_A"] != df["Variante_B"]].copy()


# ----------------------------
# 1. Global run preference
# ----------------------------
global_counts = (
    df["winner"]
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

global_pct = global_counts / global_counts.sum() * 100

plt.figure(figsize=(8, 5))
bars = plt.bar(global_counts.index, global_counts.values)

plt.title("Global Run Preference")
plt.ylabel("Number of votes")
plt.xlabel("Run")
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
plt.savefig(OUTPUT_DIR / "global_run_preference.png", dpi=200)
plt.close()


# ----------------------------
# 2. Pairwise run preferences
# ----------------------------
pairwise_counts = (
    df.groupby(["pair", "winner"])
    .size()
    .unstack(fill_value=0)
)

# Ensure all runs are present as columns
pairwise_counts = pairwise_counts.reindex(columns=RUN_ORDER, fill_value=0)

# Convert to percentages within each pair
pairwise_pct = pairwise_counts.div(pairwise_counts.sum(axis=1), axis=0) * 100

# Keep only columns that appear in each pair visually via stacked bar
plt.figure(figsize=(10, max(5, len(pairwise_pct) * 0.5)))

left = pd.Series(0, index=pairwise_pct.index)

for run in RUN_ORDER:
    values = pairwise_pct[run]
    plt.barh(pairwise_pct.index, values, left=left, label=run)

    # Add percentage labels for visible segments
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

plt.title("Pairwise Run Preferences")
plt.xlabel("Preference share within pair (%)")
plt.ylabel("Run pair")
plt.xlim(0, 100)
plt.legend(title="Preferred run", bbox_to_anchor=(1.02, 1), loc="upper left")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "pairwise_run_preferences.png", dpi=200)
plt.close()


# ----------------------------
# 3. One-vs-all-others preferences
# ----------------------------
# Count appearances of each run in key_a and key_b
appearances = (
    pd.concat([df["Variante_A"], df["Variante_B"]])
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

wins = (
    df["winner"]
    .value_counts()
    .reindex(RUN_ORDER, fill_value=0)
)

losses = appearances - wins
win_rate = wins / appearances * 100

one_vs_all = pd.DataFrame({
    "wins": wins,
    "losses": losses,
    "appearances": appearances,
    "win_rate": win_rate
})

plt.figure(figsize=(8, 5))
bars = plt.bar(one_vs_all.index, one_vs_all["win_rate"])

plt.title("One-vs-All-Others Win Rate")
plt.ylabel("Win rate (%)")
plt.xlabel("Run")
plt.ylim(0, 100)
plt.xticks(rotation=30, ha="right")

for bar, run in zip(bars, one_vs_all.index):
    wr = one_vs_all.loc[run, "win_rate"]
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
plt.savefig(OUTPUT_DIR / "one_vs_all_win_rate.png", dpi=200)
plt.close()


# ----------------------------
# Optional: print summary tables
# ----------------------------
print("\nGlobal preference counts:")
print(global_counts)

print("\nPairwise counts:")
print(pairwise_counts)

print("\nPairwise percentages:")
print(pairwise_pct.round(1))

print("\nOne-vs-all summary:")
print(one_vs_all.round(2))

print(f"\nCharts saved to: {OUTPUT_DIR.resolve()}")