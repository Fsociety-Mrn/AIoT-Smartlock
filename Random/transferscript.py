import os
import shutil


class transfercript:
    
    def __init__(self):
            
        # define path to folder containing subfolders
        self.path_to_folders = "D:/Art Lisboa files/Python/design-1-Smart-AioT/Known_Faces/"

        # define new folder to move split folders to
        self.new_folder = "D:/Art Lisboa files/Python/design-1-Smart-AioT/sub/"
        
    def transferPath(self):

        # loop through each subfolder in the parent folder
        for folder in os.listdir(self.path_to_folders):
    
            # create a list of all the files in the current subfolder
            files = os.listdir(self.path_to_folders + folder)
    
            # split the list of files in half
            split_index = len(files) // 2
    
            # create a new folder name by appending "new_" to the current folder name
            new_folder_name = folder
    
            # create the new folder in the specified directory
            os.makedirs(self.new_folder + new_folder_name)
    
            # move the second half of the files to the new folder
            for file in files[split_index:]:
                shutil.move(self.path_to_folders + folder + "/" + file, self.new_folder + new_folder_name)

transfercript().transferPath()