import requests
import datetime
from date import Date

class Registry:
    def __init__(self, image, registry):
        self.image = image
        self.registry = registry

    def fetch_tags(self):
        if f"{self.registry}" == "docker.io":
            namespace = "library"
            url = f"https://hub.docker.com/v2/repositories/{namespace}/{self.image}/tags/"
            today_date = datetime.date.today()
            date = Date()

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    result = response.json()
                    images = result['results']
                    for image in images:
                        pushed_date = image['last_updated']
                        age = date.numOfDays(today_date, pushed_date)
                        print(f"Name: {image['name']} and age: {age}")

            except requests.RequestException as e:
                print(f"Request failed: {e}")

        if f"{self.registry}" == "quay.io":
            url = f"https://quay.io/v2/repositories/{self.image}/tags/"
            print(f"Quay.io: {url}")
