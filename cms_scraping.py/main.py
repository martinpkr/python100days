from bs4 import BeautifulSoup
import requests

ENDPOINT_URL = "http://localhost:7180/"
HOSTS_URL = '/api/v14/clusters/cluster/hosts'

    "returnUrl": "",

}
response2 = requests.get('http://localhost:7180/api/v14/clusters/cluster/hosts')
print(response2)
# s = requests.session()
# response = s.get(ENDPOINT_URL)
# print(response.status_code)  # If the request went Ok we usually get a 200 status.


# soup = BeautifulSoup(response.content, "html.parser")
# protected_content = soup.find(attrs={"id": "pageName"}).text
# print(protected_content)