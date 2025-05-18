import os
from file_writer import test_file_written

def test_write_to_file():
    test_filename = "test_output.txt"
    test_content = "test content for CI"
    test_file_written(test_filename,test_content)
    
    assert os.path.exists(test_filename),"File not created"
    
    with open(test_filename,"r") as f:
        content = f.read()
        assert content == test_content,"File content do not match"

    # os.remove(test_filename)