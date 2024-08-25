from bs4 import BeautifulSoup
from googletrans import Translator
import requests

translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")
        return None
def translate_to_russian(text):
    result = translator.translate(text, dest="ru")
    return result.text


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        english_word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        print(english_word)
        print(word_definition)

        # Перевод слова и определения на русский
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        print(f"Значение слова: {russian_definition}")
        user = input("Что это за слово? ")

        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово: {russian_word}")

        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()
