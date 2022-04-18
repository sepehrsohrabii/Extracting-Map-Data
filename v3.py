import pandas as pd
import json


df_json = pd.read_json('databishtar.JSON')

df_json = pd.DataFrame(df_json)

df_json["structures"].to_excel('DATAFILE1.xlsx')