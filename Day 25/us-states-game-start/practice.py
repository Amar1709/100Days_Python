# pylint: disable=E1101
import pandas as pd

df = pd.read_csv("Day 25/us-states-game-start/50_states.csv")

df2_state = df.state.to_list()
df2_x = df.x.to_list()
df2_y = df.y.to_list()

for item in df2_state:
    print(item.lower())