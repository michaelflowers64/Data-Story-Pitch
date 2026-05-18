import pandas as pd
import os

# 1. Load the expanded multi-state dataset
df = pd.read_csv("ny_gambling_helpline.csv")

# 2. Sort the states by the hardest-hit percentage increase
df_sorted = df.sort_values(by="Pct_Increase", ascending=False)

print("\n--- MULTI-STATE COMPARISON: HELPLINE CALL SPIKES ---")
print(df_sorted[['Location', 'Event', 'Pct_Increase']])

# 3. Save the new comparative data into your output folder
os.makedirs("../output", exist_ok=True)
df_sorted.to_csv("../output/multi_state_betting_impact.csv", index=False)