import os
import re


def create_folder_structure():
    folders = {'handlers': 'init.py',
               'keyboards': 'init.py',
               'middlewares': 'init.py',
               'models': '',
               'states': 'init.py',
               }
    for folder, file in folders.items():
        pattern = r'\w{2,}'
        result = re.search(pattern, file)
        os.makedirs(folder, exist_ok=True, mode=0o777)
        if result:
            file = open(f'{folder}/{file}', mode='w+')
            file.close()


create_folder_structure()
