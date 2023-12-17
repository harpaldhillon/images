from mongo import Mongo
import json
from request import Registry

# conn = Mongo()
# names = conn.list_databases()
# print(f"Databases present in the mongo db are: {names}")

file_path = "./images.json"

# read images file
try:
    with open(file_path, "r") as file:
        json_data = json.load(file)
        for data in json_data:
            registry_obj = Registry(data.get('name'), data.get('registry'))
            registry_obj.fetch_tags()
except FileNotFoundError:
    print(f"File is not present")
except json.JSONDecodeError as e:
    print(f"Failed to decode file: {e}")
except IOError as e:
    print(f"Error reading the file: {e}")

     
