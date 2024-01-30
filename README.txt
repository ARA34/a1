Alex Reyes Aranda
areyesar@uci.edu

This program takes an input in the specified format of [COMMAND] [INPUT] [[-]OPTION] [INPUT]
and outputs a filtered list of files and directories on the terminal determined by the specific commands.

I did not have enough time to implement mutliple specific inputs as valid inputs.
Although my recursive function was working fine, it did not pass the autograder for some odd reason.

Program Command
    L - List the contents of the user specified directory.
    C - Create a new file in specified directory.
    D - Delete the file.
    R - Read the contents of the file.
    Q - Quit the program.

Options of the 'L' command
    -r Output directory content recursively.
    -f Output only files, excluding directories in the results.
    -s Output only files that match a given file name.
    -e Output only files that match a given file extension.

Options of the 'C' command
    -n specify name of file to be created

Options of the 'D' command
    None, but specify the file to be deleted.

Options of the "R" command
    None, but specify the file to be read.

You can run this file via command line with: python3 a1.py
