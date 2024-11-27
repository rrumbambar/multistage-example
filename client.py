import requests


def get_greeting():
    response = requests.get('http://server:5000/greeting')
    print(response.json())


if __name__ == '__main__':
    get_greeting()
