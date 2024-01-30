from pathlib import Path
# /Users/alexra/Documents/UCI_Winter_2023/ICS_32/test_folder
# L /Users/alexra/Documents/UCI_Winter_2023/ICS_32/test_folder
        
def recur_dir_r_3(directory: Path):
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
        paths.extend(recur_dir_r_3(path))
    return paths 


def recur_dir_s(directory: Path, given_name):
    content = ""
    for path in directory.iterdir():
        if not path.is_dir():
            if path.name == given_name:
                content += str(path)
        else:
            content += recur_dir_s(path, given_name)
    return content


def command_L(dir: Path, ltr_command, xtr_input):
    output = ""
    directory = dir
    dir_content = []
    for path in directory.iterdir():
        dir_content.append(path)

    if ltr_command == "" and xtr_input == "": # if ltr command and xtra_input are empty
        for path in directory.iterdir():
            output += str(path) + "\n"
    elif xtr_input == "":
        if ltr_command == "-r": # r - output directory contents recursively
            output_lst = recur_dir_r_3(directory)

            x = list(map(lambda d: str(d), output_lst))
            for thing in x:
                output += thing + "\n"
            #output = recur_dir_r(directory, "1")
            #print(f"This is the output: {output}")
        if ltr_command == "-f": # f - output only files(no folders)
            for path in directory.iterdir():
                if not path.is_dir():
                    output += str(path) + "\n"
    else:
        if ltr_command == "-s": # s - output only files that match a given file name
            output = recur_dir_s(directory, xtr_input)
        if ltr_command == "-e": # e - output only files that match a given extension
            for path in directory.iterdir():
                if path.suffix == xtr_input:
                    output += str(path)
        
    return output.strip()



def command_C(directory: Path, ltr_input, filename):
    if ltr_input != "-n":
        print("incorrect input. Try again.")
        return
    filename_dsu = filename + ".dsu"
    file = directory/filename_dsu
    file.touch()
    return str(file)

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
        print(str(file_dir))
        contents = file_dir.read_text().strip()
    else:
        contents = "EMPTY"
    return contents

def print_options():
    print("Welcome to a1 file management tool!")
    print("Your options are:")
    print("L - List the contents of the user specified directory.")
    print("C - Create a new file in a specified directory.")
    print("D - Delete a file.")
    print("R - Read the contents of a file.")
    print("Q - Quit the program.")

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
        

def main():
    # did not have time to implement the multiple commands input
    usr_input = input()
    usr_input_lst = parse_input(usr_input)
    command_input = usr_input_lst[0] 
    directory_str = usr_input_lst[1]
    small_input = usr_input_lst[2]
    extra_input = usr_input_lst[3]

    #allowed_sub_letters  = ["-r","-f","-s","-e","-n"]

    while command_input != "Q":
        directory_path = Path(directory_str)
        if command_input == "L":
            # if (small_input and extra_input) in allowed_sub_letters:
            #     # there are two commands,take action
            #     output = ""
            #     recur_str = command_L(directory_path, "-r","")
            #     splitlst = recur_str.split("\n")
            #     x = list(map(lambda p: Path(p), splitlst))
            #     y = list(filter(lambda s: not s.is_dir(), x))
            #     for thing in y:
            #         output += str(thing) + "\n"
            #     print(output.strip())
            # else:
            print(f"user in: {command_input, directory_str, small_input, extra_input}")
            print(command_L(directory_path, small_input, extra_input))
        elif command_input == "C":
            print(command_C(directory_path, small_input, extra_input))
        elif command_input == "D":
            command_D(directory_path)
        elif command_input == "R":
            print(command_R(directory_path))

        usr_input = input()
        

if __name__ == "__main__":
    main()
