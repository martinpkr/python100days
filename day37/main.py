import requests

TOKEN = 'mytokenforhabittraker'
USERNAME = 'krast0'
BOOK_ID = 'bookreadcounter'
# CREATES A GRAPH
# user_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'

# graph_params = {
#     'id': 'bookreadcounter',
#     'name': 'Pages Tracker',
#     'unit': 'page',
#     'type': 'int',
#     'color': 'ajisai'
# }

add_pixel_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{BOOK_ID}'

pixel_params = {
    'date': '20230626',
    'quantity': '10'
}
header_params = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=header_params)

print(response.text)