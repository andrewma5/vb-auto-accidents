import pandas as pd
import requests

# file_path = './FINAL_Police_Traffic_Crash_Reports.csv'
file_path = './TESTING.csv'
file_path2 = './saved_df.csv'
df = pd.read_csv(file_path)
# df2 = pd.read_csv(file_path2)
print(df.info())
# print(df2.info())

api_key = ''
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

def get_coordinates(address):
    params = {'address': address, 'key': api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        result = response.json().get('results')
        if result:
            location = result[0].get('geometry').get('location')
            return location['lat'], location['lng']
    return None, None

df['latitude'] = None
df['longitude'] = None

# address = df['Main_Street'][1] + " Virginia Beach"
# print(address)
# lat, lng = get_coordinates(address)
# print("lat: ", lat)
# print("lng: ", lng)

for index, row in df.iterrows():
    address = row['Main_Street'] + " Virginia Beach"
    # print("Address: ", address)
    lat, lng = get_coordinates(address)
    # print("lat: ", lat, " long: ", lng)
    df.at[index, 'latitude'] = lat
    df.at[index, 'longitude'] = lng

df.to_csv('FINAL_Police_Traffic_Crash_Reports.csv', index=False)
