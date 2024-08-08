import requests


def get_user_info(user_id: int):
    resp = requests.get(f'https://api.github.com/users/{user_id}')

    if resp.status_code == 200:
        return resp.json()

    return None
