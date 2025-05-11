import shutil

# Move file or directory to new location
shutil.move('./myfolder', './test_folder')
# If the destination location is on the same file system it's moves
# If it's different it copies and deletes the original
# Remove Directories
shutil.rmtree('./test_folder')
# It deletes a folder and all its content recursively
# Creating zip archive
shutil.make_archive('archived', 'zip', './files')
# Extract an Archive
shutil.unpack_archive('archived.zip', 'extracted_folder')
