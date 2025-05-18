import os
from file_writer import write_to_file

def test_write_to_file():
    test_filename = "test_output.txt"
    test_content = "test content for CI"
    write_to_file(test_filename,test_content)
    
    assert os.path.exists(test_filename),"File not created"
    
    with open(test_filename,"r") as f:
        content = f.read()
        assert content == test_content,"File content do not match"