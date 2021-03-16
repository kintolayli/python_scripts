import os


def insert_zeros(number):
    if len(number) == 1:
        return f"{0 * 2}{number}"
    elif len(number) == 2:
        return f"{0 * 1}{number}"
    else:
        return number


print("Введите путь, где будут созданы новые директории:")
target_dir = input()

print("Введите кол-во папок:")
dir_count = int(input())

print("Введите префикс папки: (default = 'view')")
input_dir_name = input()

directories = ["CXR", "PSD", "render_elements"]

try:
    for i in range(1, dir_count + 1):
        number = insert_zeros(str(i))
        
        if input_dir_name == "":
            dir_name = f'view_{number}'
        else:
            dir_name = f'{input_dir_name}_{number}'

        new_dir = os.path.join(target_dir, dir_name)
        for directory in directories:
            os.makedirs(os.path.join(new_dir, directory))
    print("Директории созданы успешно")
except:
    print("Возникла ошибка при создании директорий")
