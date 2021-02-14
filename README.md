# python_scripts
some python useful scripts

## translate_filename_to_english.py
# Description
The script uses the googletrans library, and its operation depends entirely on it. Use at your own risk.

# Install
0. Download repository `git clone <repository_url>`
1. Create a new virtual environment in the local repository folder `python -m venv venv`
2. Activate virtual environment `venv\Scripts\activate` and install requirements `pip install -r requirements.txt`
3. Run the script by double-clicking on `translate_filename_to_english.bat` or run cmd.exe in your repository folder, activate the virtual environment and run the python script `python translate_filename_to_english.py`.

# How to use?
1. In the first step, the script will ask you to specify the path to the folder where you want to rename the files, according to PEP8.
2. After you enter the path to the destination folder, if the path is valid, the script will show you
possible translation result, but the files in the folder still won't be translated.
3. If you select yes, only at this point will the script start translating files.
4. If you select no, the script will exit.

# Описание
Скрипт использует библиотеку googletrans, и его работа зависит полностью от нее. Используйте на свой страх и риск.

# Установка
0. Скачайте репозиторий `git clone <repository_url>`
1. Создайте новое виртуальное окружение в папке локального репозитория `python-m venv venv`
2. Активируйте виртуальное окружение `venv\Scripts\activate` и установите зависимости `pip install -r requirements.txt`
3. Запустите скрипт двойным нажатием на translate_filename_to_english.bat или запустите cmd.exe в папке вашего репозитория, активируйте виртуальную среду и запустите скрипт python `python translate_filename_to_english.py`.

# Как использовать?
1. На первом шаге скрипт попросит вас указать путь к папке, в которой вы хотите переименовать файлы, согласно PEP8.
2. После того как вы введете путь к папке назначения, если путь действителен, на втором шаге скрипт покажет вам
возможный результат перевода, но файлы в папке все еще не будут переведены.
3. Если вы выберете да, только в этот момент скрипт начнет работу по переводу файлов.
4. Если вы выберете нет, скрипт завершит свою работу.
