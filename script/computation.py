import pandas as pd
from pathlib import Path


hourly = pd.read_csv("data/hourly/hourly_2020_2024.csv", parse_dates=["date"])


hourly_2024 = hourly[hourly["date"].dt.year == 2024].copy()
hourly_2024["dow"] = hourly_2024["date"].dt.dayofweek  

weekend = hourly_2024[hourly_2024["dow"].isin([5, 6])]         
weekday = hourly_2024[hourly_2024["dow"].isin([0,1,2,3,4])]     

w2024_ln = weekend[weekend["hour"].between(0,4)]["entries"].sum()
w2024_all = weekend["entries"].sum()


d2024_am = weekday[weekday["hour"].between(7,9)]["entries"].sum()
d2024_all = weekday["entries"].sum()

share_2024_ln = w2024_ln / w2024_all if w2024_all else float("nan")
share_2024_am = d2024_am / d2024_all if d2024_all else float("nan")

W2019_ALL = 5494195   
D2019_ALL = 5493875   

w2019_ln = share_2024_ln * W2019_ALL
d2019_am = share_2024_am * D2019_ALL

recovery_ln = w2024_ln / w2019_ln if w2019_ln else float("nan")
recovery_am = d2024_am / d2019_am if d2019_am else float("nan")

out = pd.DataFrame([{
    "W2024_LN": w2024_ln,
    "W2024_ALL": w2024_all,
    "D2024_AM": d2024_am,
    "D2024_ALL": d2024_all,
    "Share_2024_LN": share_2024_ln,
    "Share_2024_AM": share_2024_am,
    "W2019_ALL": W2019_ALL,
    "D2019_ALL": D2019_ALL,
    "W2019_LN_est": w2019_ln,
    "D2019_AM_est": d2019_am,
    "Recovery_weekend_late_night": recovery_ln,
    "Recovery_weekday_am_peak": recovery_am,
    "Recovery_diff": recovery_ln - recovery_am
}])

Path("results").mkdir(exist_ok=True, parents=True)
out.to_csv("results/recovery_summary.csv", index=False)
print(out.T)
