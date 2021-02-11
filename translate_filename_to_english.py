import os
import time

from googletrans import Translator


def google_translate(message):
    translator = Translator()
    lang = translator.detect(message)
    # print(lang.lang, lang.confidence)

    if lang.lang == 'ru':
        dest_lang = 'en'
    else:
        dest_lang = 'ru'

    result = translator.translate(message, dest=dest_lang)

    # result.src - исходный язык сообщения
    # result.dest - язык назначения
    # result.origin - оригинальное сообщение
    # result.text - переведенное сообщение
    # result.pronunciation - транслитерация переведенного сообщения

    return result.text


def is_russian(input_string):
    russian_abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
                   'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
                   'э', 'ю', 'я']

    for char in input_string:
        if char.lower() in russian_abc:
            return True


def delete_unwanted_characters(input_string):
    unwanted_characters = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '+',
                           '=', '-']

    for char in input_string:
        if char in unwanted_characters:
            input_string.replace(char, '')


def file_rename(old_filename, new_filename, directory, file_extension):
    old_full_filename = old_filename + '.' + file_extension
    old_path = os.path.join(directory, old_full_filename)
    new_full_filename = new_filename + '.' + file_extension
    new_path = os.path.join(directory, new_full_filename)
    os.rename(old_path, new_path)


def main():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    for file in files:
        filename, file_extension = file.split('.')

        if is_russian(filename) and not os.path.basename(__file__):

            filename_words = filename.split()
            translate_words = []

            for word in filename_words:
                translate_words.append(google_translate(word))
                time.sleep(0.2)

            delete_unwanted_characters(filename)

            new_filename = '_'.join(translate_words).lower()

            file_rename(filename, new_filename,
                        current_directory, file_extension)


if __name__ == '__main__':
    main()
