def write_greeting():
    filename = "greeting.txt"
    try:
        with open(filename, "w") as f:
            f.write("Hello World")
        print(f"Confirmation: successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

write_greeting()
