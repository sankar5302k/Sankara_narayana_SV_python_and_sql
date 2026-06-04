def get_string_length(text):
    if not isinstance(text, str):
        print("Invalid input: not a string")
        return
    length = len(text)
    print(f"Length of string: {length}")

get_string_length("Hello, World!")
