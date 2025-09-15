import os
def findFile(filepath):
    absolute_path = os.path.abspath(filepath)
    print('File path ',absolute_path)
    if os.path.exists(absolute_path):
        if os.path.isdir(absolute_path):
            print('This is a directory')
        if os.path.isfile(absolute_path):
            print('This is a file')
            print('file size: ',os.path.getsize(absolute_path)*100,'kb')
    else:
        print('Path icluded is not exist!!')

my_path = os.path.join('H:\\','Users','Razmik','Desktoop')
for item in os.listdir(my_path):
    findFile(os.path.join(my_path,item))
# findFile(my_path)