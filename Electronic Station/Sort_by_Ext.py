from typing import List
import os


def sort_be_ext(files: List[str]):
    if not files: return files

    files_dic = {}
    result_list = []

    for i in files:
        file_name, ext = os.path.splitext(i)
        ext = ext[1:]
        files_dic[ext] = file_name

    files_dic = dict(sorted(files_dic.items()))
    file_in_order = ""
    for i in files_dic:
        file_in_order = files_dic[i] + "." + i
        result_list.append(file_in_order)

    return result_list


files = ["1.bat", "2.bat", "5.cad", "5.aa"]
print(sort_be_ext(files))