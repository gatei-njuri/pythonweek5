def main():
    try:
        #File Creation and Writing
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: Python file handling.\n")
            file.write("Line 3: Number 12345. \n")

        #File Reading and Display
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Content After Initial Writing:")
            print(content)

        #File Appending
        with open('my_file.txt', 'a') as file:
            file.write("Line 4: This is a new line.\n")
            file.write("Line 5: This is another new line.\n")
            file.write("Line 6: This is the last line.\n")

        #Reading the appended text
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File Content After Appending:")
            print(content)

    except FileNotFoundError:
        print("File not found.")
        
    except  PermissionError:
         print("You do not have permission to access this file.")
        
    except Exception as e:
        print (f"An unexpected error occurred: {e}")
        
    finally:
        print("File handling operations are complete.")

if __name__ == "__main__":
    main()