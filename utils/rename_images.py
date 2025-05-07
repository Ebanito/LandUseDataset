# (c) 2025 Full Name 
# A program to rename image files. 

import os 
import glob 

def rename_images(path, category): 
    """ Standardized the filenames of the final samples. """
    
    images = glob.glob(f"{path}/{category}/*.jpg") 
    for i, filepath in enumerate(images): 
        counter = str(i+1).zfill(4) 
        basepath = os.path.dirname(filepath) 
        filename = os.path.basename(filepath) 
        print(f" - {category}/{filename} --> {counter}.jpg") 
        new_filepath = f"{basepath}/{counter}.jpg" 
        os.rename(filepath, new_filepath)
        
def main(): 
    """ Rename image files. """ 
    
    print("[Renaming Images]") 
    categories = ["standing-crops", "post-harvest-field", "long-fallow"] 
    for category in categories: 
        rename_images("data/preprocessed", category) 
        
        
if __name__ == "__main__": 
    main()