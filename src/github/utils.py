import requests

def get_github_repos(language):
    """Uses the Google Maps API to calculate the distance between points."""

    url = "https://api.github.com/search/repositories"

    payload = {
        'q': 'language:{}'.format(language),
        'sort': 'stars'
    }

    response = requests.get(url, params=payload)
    json_response = response.json()
    items = json_response.get('items', [])

    return items
