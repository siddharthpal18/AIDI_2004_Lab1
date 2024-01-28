

def write_name_to_file(file_name, name):
    try:
        with open(file_name, 'w') as file:
            file.write(name)
        print("Name written to file successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_name_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            name = file.read()
            return name
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None

def main():
    file_name = "user_name.txt"

    # Get user's name
    user_name = input("Enter your name: ")

    # Write user's name to file
    write_name_to_file(file_name, user_name)

    # Read user's name from file
    stored_name = read_name_from_file(file_name)

    if stored_name:
        # Print personalized greeting
        print(f"Hello, {stored_name}! Welcome back.")

    print("\nProgram execution completed.")

if __name__ == "__main__":
    main()
