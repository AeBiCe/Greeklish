import os
import time

print('''
   _____               _    _ _     _     
  / ____|             | |  | (_)   | |    
 | |  __ _ __ ___  ___| | _| |_ ___| |__  
 | | |_ | '__/ _ \/ _ \ |/ / | / __| '_ \ 
 | |__| | | |  __/  __/   <| | \__ \ | | |
  \_____|_|  \___|\___|_|\_\_|_|___/_| |_| 

      "Translate Greek to Greeklish"                                   

''')

# Alphabet mapping
greek = "ΑΆΒΓΔΕΈΖΗΉΘθΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΩΏαάβγδεέζηήιίϊΐκλμνξοόπρσςτυύϋΰφχωώ;" 
english = "AAVGDEEZII88IIIKLMNXOOPRSTYYYFXOOaavgdeeziiiiiiklmnxooprsstuuuufxoo?"

subfolders   = ''
choice_alt  = ['Y','y','N','n']
directory   = input("Enter directory: ")

def greeklish(file):
    table = file.maketrans(greek, english) # Map characters
    try:
        os.rename((os.path.join(subdir,file)),os.path.join(subdir,file.translate(table))) # Rename file
    except PermissionError: # Skips files with special permissions
        pass

while not os.path.isdir(directory):
    directory = input("\nInvalid directory!\nEnter a new directory: ")

os.chdir(directory) # Change dir to input
files = os.listdir(os.getcwd()) # Get files in directory

while subfolders not in choice_alt:
    subfolders = input("Translate subfolders (Y/N): ")

if subfolders == 'Y' or subfolders == 'y':
    print("[Subfolders included]")
    start = time.time()
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            greeklish(file)
    end = time.time()

else:
    subdir = ""
    print("[Subfolders excluded]")
    start = time.time()
    for file in files:
        greeklish(file)
    end = time.time()

print("\nTranslation complete! [",round((end-start),3),"seconds ]")

