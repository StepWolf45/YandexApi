from single_word_json.py import single_word_json
from single_word_list.py import single_word_list

def speller_menu():
    print('1. проверка одного слова (JSON)')
    print('2. проверка одного слова (список подсказок)')
    print('3. проверка строки (JSON)')
    print('4. проверка строки (без ссылок)')
    print('5. проверка строки (without caps)')
    print('0. Назад')
    a=int(input())
    if a==1:
        print(single_word_json())
    elif a==2:
        print(single_word_list())
    elif a==3:
        print('text_json')
    elif a==4:
        print('text_link_ignore')
    elif a==5:
        print('text_ignore_caps')
    elif a==0:
        return 

def main():
    speller_menu()
if __name__ == '__main__':
    main()
