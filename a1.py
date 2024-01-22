from pathlib import Path
import time

# /Users/alexra/Documents/UCI_Winter_2023/ICS_32

def recur_dir_r(dir):
    directory = Path(dir)
    content = ""
    for path in directory.iterdir():
        if not path.is_dir():
            content += str(path) + "\n"
        else:
            content += str(path) + "\n"
            content += recur_dir_r(path)
    return content

def recur_dir_s(dir, given_name):
    directory = Path(dir)
    content = ""
    for path in directory.iterdir():
        if not path.is_dir():
            if path.name == given_name:
                content += str(path)
        else:
            content += recur_dir_s(path, given_name)
    return content

def command_L(dir, ltr_command,xtr_input):
    print("Options of the 'L' command:\n\n\t-r Output directory content recursively.\n\t-f Output only files, excluding directories in the results.\n\t-s Output only files that match a given file name.\n\t-e Output only files that match a given file extension.\n")
    output = ""

    directory = Path(dir)
    dir_content = []
    for path in directory.iterdir():
        dir_content.append(path.name)

    if ltr_command == "" and xtr_input == "":
        # if ltr command and xtra_input are empty
        for path in directory.iterdir():
            output += str(path) + "\n"
    elif xtr_input == "":
        if ltr_command == "-r":
            # r - output directory contents recursively
            output = recur_dir_r(directory)
            
        if ltr_command == "-f":
            # f - output only files(no folders)
            for path in directory.iterdir():
                if not path.is_dir():
                    output += str(path) + "\n"
    else:
        if ltr_command == "-s":
            # s - output only files that match a given file name
            output = recur_dir_s(directory, xtr_input)
        if ltr_command == "-e":
            # e - output only files that match a given extension
            for path in directory.iterdir():
                if path.suffix == xtr_input:
                    output += str(path)
    return output



def print_start_options():
    print("Welcome to a1 file management tool!")
    print("Your options are:\nL - List the contents of the user specified directory.\nQ - Quit the program.")

def main():
    # Big command, directory, small command, another input

    # big command and directory are necessary

    print_start_options()
    user_input = input().split()

    command_input = user_input[0]
    

    while command_input != "Q":
        directory_input = user_input[1]

        if len(user_input) == 4:
            letter_command = user_input[2]
            extra_input = user_input[3]
        elif len(user_input) == 3:
            letter_command = user_input[2]
            extra_input = ""
        else:
            letter_command = ""
            extra_input = ""

        # beginning of command parse
        if command_input == "L":
            print(command_L(directory_input, letter_command, extra_input))
        user_input = input().split()
        command_input = user_input[0]


if __name__ == "__main__":
    main()