import numpy as np
import pandas as pd
from statsbombpy import sb
from mplsoccer import VerticalPitch
import matplotlib.pyplot as plt

df = sb.events(match_id='3795506') #Final Euro
df.head()

pitch = VerticalPitch(
    half=True,
    pitch_color='grass', 
    line_color='white', 
    positional = True)

#print(df.info())
eng_color = "#ff0066"
ita_color = "#0720de"

# Split df into two parts, one for each team
eng_df = df[df["team"] == "England"].copy()
ita_df = df[df["team"] == "Italy"].copy()

# Split England's df into two parts, goals and non-goals
eng_df_g = eng_df[eng_df["shot_outcome"] == "Goal"].copy()
eng_df_ng = eng_df[eng_df["type"] != "Goal"].copy()

# Split Italy's df into two parts, goals and non-goals
ita_df_g = ita_df[ita_df["shot_outcome"] == "Goal"].copy()
ita_df_ng = ita_df[ita_df["type"] != "Goal"].copy()

eng_df_g["start_location_x"] = eng_df_g["location"].str.extract(r'\[(-?\d+\.\d+), -?\d+\.\d+\]')
eng_df_g["start_location_y"] = eng_df_g["location"].str.extract(r'\[-?\d+\.\d+, (-?\d+\.\d+)\]')

fig, ax = pitch.draw(figsize=(10, 8))




# Eng non-goal shots:
eng_sc_ng = pitch.scatter(eng_df_ng["location"].str[0].astype(float),
                          eng_df_ng["location"].str[1].astype(float),
                          s=eng_df_ng["shot_statsbomb_xg"]*500+100,
                          c=eng_color, 
                          alpha=0.6,
                          edgecolor="#101010",
                          marker="h",
                          ax=ax)


# Ita non-goal shots:
ita_sc_ng = pitch.scatter(ita_df_ng["location"].str[0].astype(float),
                          ita_df_ng["location"].str[1].astype(float),
                          s=ita_df_ng["shot_statsbomb_xg"]*500+100,
                          c=ita_color,
                          alpha=0.6,
                          edgecolor="#101010",
                          marker="h",
                          ax=ax)
# Eng goals:
eng_sc_g = pitch.scatter(eng_df_g["location"].str[0].astype(float),
                         eng_df_g["location"].str[1].astype(float),
                         s=eng_df_g["shot_statsbomb_xg"]*500+100,
                         marker="s",
                         alpha=0.75,
                         c=eng_color,
                         ax=ax)

# Ita goals:
ita_sc_g = pitch.scatter(ita_df_g["location"].str[0].astype(float),
                         ita_df_g["location"].str[1].astype(float),
                         s=ita_df_g["shot_statsbomb_xg"]*500+100,
                         marker="s",
                         c=ita_color,
                         alpha=0.75,
                         ax=ax)

txt = ax.text(x=40, y=80, s='ENG 1 (2) - (3) 1 ITA ',
              size=30,
              # here i am using a downloaded font from google fonts instead of passing a fontdict
              color="#000000",
              va="center", ha="center")