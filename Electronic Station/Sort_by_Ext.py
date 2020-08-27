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


def sort_by_ext2(files: List[str]) -> List[str]:
    out_list = []
    files_wext = []
    input_list = files

    for i in range(len(input_list)):
        dot_location = input_list[i].rfind(".")

        if dot_location == -1:
            out_list.append(input_list[i])
        elif dot_location == 0 or dot_location == len(input_list[i]) - 1:
            out_list.append(input_list[i])
        else:
            files_wext.append(input_list[i])

    out_list = sorted(out_list)

    files_wext = sorted(files_wext, key=lambda x: x[x.rfind("."):])
    extensions = {}

    for filename in files_wext:
        key = filename[filename.rfind("."):]
        try:
            extensions[key].append(filename)
        except KeyError:
            extensions[key] = [filename]

    for value in extensions.values():
        out_list += sorted(value)

    return out_list
files = ["1.bat", "2.bat", "5.cad", "5.aa"]
print(sort_be_ext(files))
print(sort_be_ext2(files))