import os

base_path = "D:\\!3DsMAX\\3D_MODEL\\!EXTERIOR\\01_TREES\\Maxtree"
target_folders = os.listdir(base_path)

folders_list = list()

for folder in target_folders:
    new_path = os.path.join(base_path, folder)
    new_path_folders = os.listdir(new_path)
    for _folder in new_path_folders:
        if _folder.lower().endswith('maps'):
            final_path = os.path.join(new_path, _folder)
            folders_list.append(final_path)
            break


count = 27

for folder in folders_list:
    result_string = f'Dir{str(count)}={folder}'
    print(result_string)
    count += 1

print(len(folders_list))




