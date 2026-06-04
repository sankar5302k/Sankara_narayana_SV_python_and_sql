import os

def read_file_content(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"File Content:\n{content}")
    except Exception as e:
        print(f"An error occurred: {e}")

read_file_content("greeting.txt")
