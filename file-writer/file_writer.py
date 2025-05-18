def test_file_written(filename,content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    test_file_written('output.txt', 'Hello, from python script!')
    print("File created and content written successfully.")
