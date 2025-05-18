def write_to_file(filename,content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    write_to_file('output.txt', 'Hello, from python script!')
    print("File created and content written successfully.")
