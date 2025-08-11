# lib/file_io.py

def write_file(file_name, file_content):
    # Add .txt extension and write content
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    # Add .txt extension and append content
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)


def read_file(file_name):
    # Add .txt extension and read content
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
