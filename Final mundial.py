import pandas as pd
from statsbombpy import sb
from mplsoccer import Pitch

competitions = sb.competitions()

WC = sb.matches(43, 106)
Mundial = WC

Match_ID = 3869685 #final del mundial
match_events_df = sb.events(match_id=Match_ID)

match_360_df = pd.read_json(f"C:/Users/herna/OneDrive/Documentos/LUIS/Deporte/Futbol/SANJE ANALYTICA/STATSBOMB/open-data/data/three-sixty/{Match_ID}.json")

match_events_df["id"]
match_360_df["event_uuid"]
match_360_df.head()

match_360_df .iloc[0]["freeze_frame"]

#Juntar match360 con matchevents
df = pd.merge(left=match_events_df, right=match_360_df, left_on=("id"), right_on=("event_uuid"), how=("left"))

df.columns
df.player_id.unique() #ID de jugadores del partido

#Ejemplo con Messi
Messi = 5503
df = df[(df["player_id"] == Messi) & (df["type"] == "Pass")].reset_index(drop=True)
print(df.location)
