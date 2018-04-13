import requests

def get_github_repos(language):

    url = "https://api.github.com/search/repositories"

    payload = {
        'q': 'language:{}'.format(language),
        'sort': 'stars'
    }

    response = requests.get(url, params=payload)

    if response.status_code != 200:
        return []

    json_response = response.json()
    items = json_response.get('items', [])
    return items
