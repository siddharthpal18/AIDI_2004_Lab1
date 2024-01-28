This Python script allows users to input their name, writes it to a file named "user_name.txt," and then reads the name back from the file for a personalized greeting. The script consists of three functions:

write_name_to_file(file_name, name): This function takes two parameters - file_name representing the name of the file to write to and name representing the user's name. It attempts to open the file in write mode ('w') and writes the user's name to the file. If an error occurs during the process, it catches the exception and prints an error message.

read_name_from_file(file_name): This function takes file_name as a parameter and attempts to open the file in read mode ('r'). It reads the content of the file, which should be the user's name, and returns it. If an error occurs, it catches the exception, prints an error message, and returns None.

main(): The main function initializes file_name as "user_name.txt." It prompts the user to input their name and then calls write_name_to_file() to write the name to the file. After that, it calls read_name_from_file() to read the stored name from the file. If a name is successfully retrieved, it prints a personalized greeting. Finally, it prints a completion message.

The script is executed when the file is run directly (not imported as a module) using the if __name__ == "__main__": block. It ensures that the main() function is called when the script is executed.
