from pathlib import Path
# /Users/alexra/Documents/UCI_Winter_2023/ICS_32/test_folder


def recur_dir_r(directory: Path, usr_input = ""):
    content = ""
    first_files = ""
    for path in directory.iterdir():
        if not path.is_dir():
            if usr_input != "":
                first_files += str(path) + "\n"
            else:
                content += str(path) + "\n"
        else:
            content += str(path) + "\n"
            content += recur_dir_r(path)
    return first_files + content


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
    print("Options of the 'L' command:")
    print("\t-r Output directory content recursively.")
    print("\t-f Output only files, excluding directories in the results.")
    print("\t-s Output only files that match a given file name.")
    print("\t-e Output only files that match a given file extension.\n")
    output = ""

    directory = dir


    dir_content = []
    for path in directory.iterdir():
        dir_content.append(path.name)

    if ltr_command == "" and xtr_input == "": # if ltr command and xtra_input are empty
        for path in directory.iterdir():
            output += str(path) + "\n"
    elif xtr_input == "":
        if ltr_command == "-r": # r - output directory contents recursively
            output = recur_dir_r(directory, "1")
            print(output)
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
    return output

def command_C(directory: Path, ltr_input, filename):
    print("Options of the 'C' command:")
    print("\t-n Input a filename\n")
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
    if file_dir.suffix != ".dsu":
        print("ERROR")
    elif len(file_dir.read_text()) != 0:
        print(str(file_dir))
        print(file_dir.read_text())
    else:
        print("EMPTY")

def print_start_options():
    print("Welcome to a1 file management tool!")
    print("Your options are:")
    print("L - List the contents of the user specified directory.")
    print("C - Create a new file in a specified directory.")
    print("D - Delete a file.")
    print("R - Read the contents of a file.")
    print("Q - Quit the program.")


def main():

    print_start_options()
    user_input = input().split()
    command_input = user_input[0]
    while command_input != "Q":
        directory_input = user_input[1]
        directory_path = Path(directory_input)
        if len(user_input) == 4:
            letter_command = user_input[2]
            extra_input = user_input[3]
        elif len(user_input) == 3:
            letter_command = user_input[2]
            extra_input=""
        else:
            letter_command=""
            extra_input=""
        if command_input == "L":
            print(command_L(directory_path, letter_command, extra_input))
        elif command_input == "C":
            if len(user_input) != 4:
                print("You need to specifiy what option, and what file.")
            else:
                print(command_C(directory_path, letter_command, extra_input))
        elif command_input == "D":
            if len(user_input) != 2:
                print("Inufficient inputs recieved.")
            else:
                command_D(directory_path)
        elif command_input == "R":
            if len(user_input) != 2:
                print("Inufficient inputs recieved.")
            else:
                command_R(directory_path)

        print()
        print_start_options()
        user_input = input().split()
        command_input = user_input[0]
        print()


if __name__ == "__main__":
    main()
