import requests

def get_html(url, username, password):
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        html_content = response.text
        return html_content
    elif response.status_code == 401:
        print("Error: Authentication failed")
        return None
    else:
        print("Error: Failed to fetch web page")
        return None

# Example usage
web_page_url = "http://cms.controlcho.int:7180/cmf/hardware/hosts#sort"
username = "martin.kirilov"
password = "4@V!F#uzaxkiTW"
html = get_html(web_page_url, username, password)
print(html)