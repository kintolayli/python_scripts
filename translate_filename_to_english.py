import os

from googletrans import Translator


def google_translate(message):
    translator = Translator()
    translations = translator.translate(message, dest="en")
    return translations.text


def is_russian(input_string):
    russian_abc = [
        "а",
        "б",
        "в",
        "г",
        "д",
        "е",
        "ё",
        "ж",
        "з",
        "и",
        "й",
        "к",
        "л",
        "м",
        "н",
        "о",
        "п",
        "р",
        "с",
        "т",
        "у",
        "ф",
        "х",
        "ц",
        "ч",
        "ш",
        "щ",
        "ъ",
        "ы",
        "ь",
        "э",
        "ю",
        "я",
    ]

    for char in input_string:
        if char.lower() in russian_abc:
            return True


def delete_unwanted_characters(input_string):
    unwanted_characters = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "+",
        "=",
        "-",
        ".",
        "(",
        ")",
    ]

    new_string = ""

    for char in input_string:
        if char not in unwanted_characters:
            new_string += char

    return new_string


def file_rename(new_filenames_dict, directory):

    for key, values in new_filenames_dict.items():
        old_filename = key
        new_filename = values[0]
        file_extension = values[1]
        old_path = os.path.join(directory, old_filename)
        new_full_filename = new_filename + "." + file_extension
        new_path = os.path.join(directory, new_full_filename)
        os.rename(old_path, new_path)


def get_extension(filename):
    extension = ""
    for char in filename[::-1]:
        if char != ".":
            extension += char
        else:
            return extension[::-1]


def system_path_validator(path):
    path_exists = os.path.exists(path)

    while path_exists is False:
        print("Такого пути не существует, введите корректный путь:")
        path = input()
        path_exists = os.path.exists(path)

    return path


def answer_validator():
    while True:
        answer = input()
        if answer == "n":
            return False
        if answer == "y":
            return True
        else:
            print("Для ответа нажмите на клавиатуре 'y'(yes) или 'n'(no)")
            continue


def translate_example(input_path):
    files = os.listdir(input_path)

    filenames_dict = {}

    for file in files:
        if os.path.isfile(os.path.join(input_path, file)):

            file_extension = get_extension(file)
            filename = file[: -(len(file_extension) + 1)]

            if is_russian(filename):
                old_filename = filename
                filename = delete_unwanted_characters(filename)
                translate_words = google_translate(filename).split()
                new_filename = "_".join(translate_words).lower()
                filenames_dict[old_filename + "." + file_extension] = [
                    new_filename,
                    file_extension,
                ]

    return filenames_dict


def main():
    print("Введите путь к директории, где будут переименованы файлы:")
    current_directory = system_path_validator(input())

    new_filenames_dict = translate_example(current_directory)

    print("Файлы в папке будут переименованы следующим образом:")
    for key, values in new_filenames_dict.items():
        print(key, "->", values[0] + "." + values[1])

    print("Желаете продолжить?(y/n)")

    if answer_validator():
        file_rename(new_filenames_dict, current_directory)
    else:
        exit()


if __name__ == "__main__":
    main()
