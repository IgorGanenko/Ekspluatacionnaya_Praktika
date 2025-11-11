import string
from collections import defaultdict

def show_result(text, words, sorted_words):
    """ Записываем результат в файл и выводим в консоль """
    with open("result_1.txt", "w", encoding="utf-8") as result_file:
        for word, count in sorted_words:
            result_file.write(f"{word} {count}\n")

    for word, count in sorted_words:
        print(f"{word} {count}")

def count_and_sort_text(text, words):
    """ Подсчитываем количество слов и сортируем текст """
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words

def translation_text(text):
    """ Убираем пунктуацию и разделяем текст на отдельные слова """
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    words = text.split()
    sorted_words = count_and_sort_text(text, words)
    show_result(text, words, sorted_words)

def read_file():
    """ Читаем содержимое файла """
    with open("resource_1.txt", "r", encoding="utf-8") as file:
        text = file.read().lower()
        translation_text(text)

if __name__ == "__main__":
    read_file()
