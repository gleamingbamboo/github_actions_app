import requests as re

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Github Actions')
    res = re.get('https://get.docker.com/')
    if res.status_code == 200:
        print(res.text[0])
