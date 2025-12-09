import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023, 2024]
avg_weekday = [5493875, 2040580, 2369655, 3189904, 3625326, 3735571]
avg_weekend = [5494195, 2135312, 2888620, 3703485, 4237280, 4419517]

weekday_recovery = avg_weekday[-1] / avg_weekday[0]
weekend_recovery = avg_weekend[-1] / avg_weekend[0]

plt.figure(figsize=(6.5, 4.2))
plt.bar(["Average Weekday", "Average Weekend"],
        [weekday_recovery, weekend_recovery])
plt.axhline(1.0, linestyle="--", linewidth=1)
plt.ylabel("Recovery Ratio (2024 / 2019)")
plt.title("Systemwide Subway Recovery in 2024 vs 2019")
plt.ylim(0, max(weekday_recovery, weekend_recovery) * 1.2)

plt.text(0, weekday_recovery + 0.01, f"{weekday_recovery:.2f}",
         ha="center", va="bottom", fontsize=10)
plt.text(1, weekend_recovery + 0.01, f"{weekend_recovery:.2f}",
         ha="center", va="bottom", fontsize=10)

plt.tight_layout()
plt.savefig("Figure2_Systemwide_Recovery_2024_vs_2019.png", dpi=300)
plt.close()

plt.figure(figsize=(7.0, 4.2))
plt.plot(years, avg_weekday, marker="o", label="Average Weekday")
plt.plot(years, avg_weekend, marker="o", label="Average Weekend")
plt.ylabel("Average Ridership (entries)")
plt.title("Average Weekday vs Weekend Subway Ridership, 2019–2024")
plt.xticks(years)
plt.legend()

plt.tight_layout()
plt.savefig("Figure3_Average_Weekday_vs_Weekend_2019_2024.png", dpi=300)
plt.close()

print("Saved Figure 2 and Figure 3.")
