import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

reference_data = df.iloc[:200]
current_data = df.iloc[200:]

report = Report(metrics=[DataDriftPreset()])

report.run(
    reference_data=reference_data,
    current_data=current_data
)

print(report)
