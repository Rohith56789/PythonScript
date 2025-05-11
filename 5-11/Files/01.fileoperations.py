import shutil
#copy file froim source to destination
shutil.copy('./files/source.txt', './files/destination.txt')

#copy2 is similar to copy function but it also copies the metadata of the file
shutil.copy2('./files/source.txt', './files/destination.txt')   

#copy entire directory
shutil.copytree('./files', './myFolder')