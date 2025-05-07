# (c) 2025 Full Name 
# A program to move image files.

import os 
import glob 
import shutil


RAW_DATASET = "data/raw" 
PREPROCESSED_DATASET = "data/preprocessed" 

def move_images(source, destination, category): 
    """ Move image files to final directory. """
    
    os.makedirs(f"{destination}/{category}", exist_ok=True)
    
    images = glob.glob(f"{source}/{category}/*.jpg") 
    for filepath in images: 
        filename = os.path.basename(filepath) 
        print(f" - {category}/{filename}") 
        new_filepath = filepath.replace(source, destination) 
        shutil.move(filepath, new_filepath) 
        
def main(): 
    """ Move image files to final directory. """ 
    
    print("[Moving Images]") 
    categories = ["standing-crops", "post-harvest-field", "long-fallow"] 
    for category in categories: 
        # in actual practice, preprocessing can be done here 
        # the output images are moved to another location 
        move_images(RAW_DATASET, PREPROCESSED_DATASET, category)
        
        
if __name__ == "__main__": 
    main() 