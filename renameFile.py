import os
from natsort import natsorted

path = r""
nb_file = 3 # ~N
renamed = 0 # N-1~
print(f"Before Renaming: {natsorted(os.listdir(path))}")

for file in natsorted(os.listdir(path)):
    if file.startswith("012345678"):
        if renamed < nb_file:
            os.rename(path+file,f"{path}Relevé_{renamed+1}.pdf")
            renamed+=1
        else:
            break
print(f"After Renaming: {os.listdir(path)}")