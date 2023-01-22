import requests


def single_word_json():
    adres = "https://speller.yandex.net/services/spellservice.json/checkText"
    word = input()
    if len(word.split()) == 1:
        get_params ={
            'text': word
        }
        responce = requests.get(url=adres, params=get_params)
        if responce.status_code == 200:
            data = responce.json()
            print(data)
        else:
            print("Ошибка: {}".format(responce.status_code))
    else:
        print("Ошибка: введено не одно слово")


if __name__ == '__main__':
    single_word_json()
