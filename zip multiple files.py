

'''
    1. ask for the name of the zip file, append '.zip' to that string
    2. input how many files need to be zipped
    3. one by one, get input of the files' names
    4. add folders to the zip
    4. adding various exceptions for input and zipping process
'''

from zipfile import ZipFile

def zipper():
    zip_destination=input("Enter final zip file's path and name: ")
    if '.zip' not in zip_destination:
        zip_destination+='.zip'
    
    num_of_files= int(input("How many files do you want to zip:"))

    with ZipFile(zip_destination, 'w') as myzip:
        for i in range(num_of_files):

            file=input('Path and Name of file '+str(i+1)+' with the proper extention such as .txt or .pdf: ')

            try:
                myzip.write(file)
            except FileNotFoundError:
                print("This file doesn't exist! Enter another name")
                i-=1
            except:
                print('A new exception occured')
            else:
                print('File was added successfully')
    print('Result Zip file was saved at the location specified')
        
zipper()
