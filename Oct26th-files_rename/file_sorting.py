import os


def get_list_of_file_names(dir_path):
    list_of_files = os.listdir(dir_path)
    return sorted(list_of_files)

def get_file_names_to_rename(files_list):
    sub_str = '0'
    lis = []
    for eachfile in files_list:
        if eachfile.startswith(sub_str) !=0:
            pass
        else:
            lis.append(eachfile)
    return lis

def rename_files(inputs1):
    for eachfile in inputs1:
        new_filename = eachfile.zfill(6)
        os.rename(eachfile, new_filename)

def main():
    dir_path = '/home/praneeth/Desktop/Examples/files_rname'
    files_list = get_list_of_file_names(dir_path)
    files_to_rename = get_file_names_to_rename(files_list)
    #print(files_to_rename)
    rename_files(files_to_rename)


if __name__ == '__main__':
    main()
