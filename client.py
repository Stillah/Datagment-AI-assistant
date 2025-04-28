import requests

def main():
    header = {'question': 'What is your name?'}
    response = requests.get('http://127.0.0.1:8080/query/text', headers=header)
    print(response.text)

if __name__ == '__main__':
    main()
