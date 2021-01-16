import os
from glob import glob

#set directory
os.getcwd()


#file_format="\*.xlsx"     
#file_format="\*.png"        
def deleteFile(file_path,file_format):
        deletion_counter = 0
        src_files = glob(file_path +file_format)
        for file_name in src_files:
            full_path = os.path.join( file_name)
            if os.path.isfile(full_path):
                print('removing one...', full_path)
                os.remove(full_path)
                deletion_counter += 1
            else:
                print('Is not a file:', full_path )
        print('Cleaning', str(file_path) ,'directory ended')
        print('Deleted ',  str(deletion_counter), 'files.')
        return deletion_counter
