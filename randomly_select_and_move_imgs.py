# Randomly select and move images

import shutil
import numpy as np
import os


def randomly_select_move(src, dest, percentage=0.1):
    """
    Randomly select given #files and move into new destination
    :param src: Source folder
    :param dest:Destination folder
    :param percentage: Testset percentage
    :return:
    """
    
    # List files
    li = os.listdir(src)
    
    num_folders = int(len(li) * percentage)
    
    # Shuffle
    np.random.shuffle(li)
    
    # Select given number of files
    dir_list = np.random.choice(li, num_folders)
    
    # Select unique files 
    dir_list = list(set(dir_list))

    for f in dir_list:
        pat = os.path.join(src, f)
        try:
            shutil.move(pat, dest)
        except Exception as e:
            print("\n" + str(e))
            print("Error: ", f)
            continue
