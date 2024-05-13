import os
import pandas as pd
import pandas_gbq
import re
import json

project_id = "integral-cell-418310"



query ="""
SELECT *
FROM `integral-cell-418310.dota2.matches_teamfights`
WHERE match_id BETWEEN 3710610588 AND 6184141710
"""

df_teamfights = pd.read_gbq(query, project_id)

df_teamfights.head()




# Initialize an empty DataFrame to store the concatenated teamfights data
teamfights_list = []
i = 0
# for every entry create entries in a new dataframe that will contain all picks/bans of that match id
for row in df_teamfights.itertuples():
    # check if na:
    if pd.notna(row.teamfights):
        # Convert the value to a string and then replace single quotes with double quotes in the JSON string
        teamfights_json = str(row.teamfights).replace("'", '"')
        # teamfights_json = re.sub(r'False', 'false', teamfights_json)
        # teamfights_json = re.sub(r'True', 'true', teamfights_json)
        # print(teamfights_json)  # Print the modified JSON string before parsing
        json_list = json.loads(teamfights_json)
        for item in json_list:
            updated_item = dict(item)
            updated_item.update({"match_id": row.match_id})
            # print(updated_item)
            teamfights_list.append(updated_item)
    print(i)
    i += 1
# add the list of picks and bans to a df
df_teamfights_only = pd.DataFrame(teamfights_list)

pandas_gbq.to_gbq(df_teamfights_only, "dota2.teamfights", "integral-cell-418310")