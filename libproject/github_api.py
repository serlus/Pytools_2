import requests


def github_api(user):
    """
    Funçao que busca informaçoes de usuario no github
    :param user:
    :return: int
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['id']

if __name__ == '__main__':
    print(github_api('serlus'))