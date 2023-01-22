import requests

def single_word_list():
    string = (input().split(' '))

    if (len(string) > 1):
        return

    address = 'https://speller.yandex.net/services/spellservice.json/checkText'
    getparams = {
        'text': string[0]
    }
    response = requests.get(url=address, params=getparams)
    if response.status_code == 200:
        data = response.json()
        for error in data:
            AnsList = list(error['s'])
            for Answer in AnsList:
                print(Answer, AnsList.index(Answer) ,sep=' ')



if __name__ == '__main__':
    single_word_list()
