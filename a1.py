# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID
from pathlib import Path


def recur_dir(directory: Path):
    # input: directory
    # output: list of paths
    paths = []
    for path in directory.iterdir():
        if path.is_file():
            paths.append(path)

    dirs = []
    for path in directory.iterdir():
        if path.is_dir():
            dirs.append(path)
    for path in dirs:
        paths.append(path)
        paths.extend(recur_dir(path))
    return paths 


def paths_to_strs(path_list:list):
    # input: list of paths
    # output: string of path directories
    output = ""
    for path in path_list:
        output += str(path) + "\n"

    return output.strip()


def command_L(directory: Path, subs: list, extra_input: str):
    # input: diectory, list of sub commands, extra input
    # output: string of paths
    output = []
    iter_paths = []

    allowed_ext = [".dsu", ".py",".txt"]
    for path in directory.iterdir():
        iter_paths.append(path)

    if len(subs) == 0 and extra_input == "":
        output = paths_to_strs(iter_paths)
    elif "-r" in subs:
        # it r time
        output = recur_dir(directory)
        if "-f" in subs:
            # r  + f
            output = list(filter(lambda p: p.is_file(), output))
            output = paths_to_strs(output)
        elif "-e" in subs:
            # r + e
            if "."+extra_input in allowed_ext:
                output = list(filter(lambda p: p.suffix == "." + extra_input, output))
                output = paths_to_strs(output)
            else:
                output = "ERROR"
        elif "-s" in subs:
            # r + s
            if extra_input != "":
                output = list(filter(lambda p: p.name == extra_input, output))
                output = paths_to_strs(output)
            else:
                output = "ERROR"
        else:
            output = paths_to_strs(output)
    elif "-f" in subs:
        # f
        if extra_input == "":
            output = list(filter(lambda p: p.is_file(), iter_paths))
            output = paths_to_strs(output)
        else:
            output = "ERROR"
    elif "-e" in subs:
        # e
        if "." + extra_input in allowed_ext:
            output = list(filter(lambda p: p.suffix == "." + extra_input, iter_paths))
            output = paths_to_strs(output)
        else:
            output = "ERROR"
    elif "-s" in subs:
        # s
        if extra_input != "":
            output = list(filter(lambda p: p.name == extra_input, iter_paths))
            output = paths_to_strs(output)
        else:
            output = "ERROR"
    else:
        output = "ERROR"
    return output


def command_C(directory: Path, subs, filename):
    output = ""
    if "-n" in subs:
        filename_dsu = filename + ".dsu"
        file = directory/filename_dsu
        file.touch()
        output = str(file)
    else:
        output = "ERROR"
    return output


def command_D(file_dir: Path):
    if file_dir.exists() and file_dir.suffix == ".dsu":
        str_file = str(file_dir)
        file_dir.unlink()
        print(str_file + " DELETED")
    else:
        print("ERROR")


def command_R(file_dir: Path):
    contents = ""
    if file_dir.suffix != ".dsu":
        contents = "ERROR"
    elif len(file_dir.read_text()) != 0:
        contents = file_dir.read_text().strip()
    else:
        contents = "EMPTY"
    return contents


def parse_input(input:str):
    command_letter = input[0]
    allowed_sub_letters  = ["-r","-f","-s","-e","-n"]
    rest_input = input[2:]
    directory_input = ""
    small_input = ""
    extra_input = ""

    some_str = rest_input

    input_lst = some_str.split()

    for sub_letter in allowed_sub_letters:
        if sub_letter in input_lst:
            small_input = sub_letter
            input_lst.remove(sub_letter)
            extra_input = input_lst[-1].strip()
            input_lst.remove(input_lst[-1])
    
    directory_input = " ".join(input_lst)

    directory_input = " ".join(input_lst)
    if directory_input == "":
        directory_input = extra_input
        extra_input = ""

    output_lst = [command_letter, directory_input, small_input, extra_input]

    return output_lst


def parse_input_2(input:str):
    input_list = []

    command_letter = ""
    dir_input = ""

    allowed_subs = ["-r","-f","-s","-e","-n"]

    # command letter
    command_letter = input[0]

    remaining_str = input[2:]
    remaining_lst = remaining_str.split() # a list of subsections without the first letter

    subs = list(filter(lambda s: s in allowed_subs, remaining_lst))

    for i in range(len(remaining_lst)):
        try:
            check = remaining_lst[i] + " " + remaining_lst[i+1]
            if Path(check).exists():
                dir_input = check
                remaining_lst.remove(remaining_lst[i+1])
                remaining_lst.remove(remaining_lst[i])
            elif remaining_lst[i] in subs:
                remaining_lst.remove(remaining_lst[i])
            else:
                dir_input = remaining_lst[0]
                remaining_lst.remove(dir_input)
        except:
            for sub in remaining_lst:
                if sub in subs:
                    remaining_lst.remove(sub)

    remain = "".join(remaining_lst)
    if Path(remain).exists() and dir_input == "": # last edge case 
        dir_input = remain
        remain = ""
        

    # finalize
    input_list.append(command_letter)
    input_list.append(dir_input)
    input_list.append(subs)
    input_list.append(remain)      


    return input_list
        

def main():
    usr_input = input()
    command_input, directory_input, subs, extra = parse_input_2(usr_input)

    while command_input != "Q":
        if len(usr_input) == 1:
            print("ERROR")
            return
        directory_path = Path(directory_input)
        if command_input == "L":
            print(command_L(directory_path, subs, extra))
        elif command_input == "C":
            print(command_C(directory_path, subs, extra))
        elif command_input == "D":
            command_D(directory_path)
        elif command_input == "R":
            print(command_R(directory_path))

        usr_input = input()
        command_input, directory_input, subs, extra = parse_input_2(usr_input)
        

if __name__ == "__main__":
    main()
