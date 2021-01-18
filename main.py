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

directory = input("Enter directory: ")

while not os.path.isdir(directory):
    directory = input("\nInvalid directory!\nEnter a new directory: ")

os.chdir(directory) # Change dir to input
files = os.listdir(os.getcwd()) # Get files in directory


start = time.time()
for file in files:
    table = file.maketrans(greek, english) # Map characters
    try:
        os.rename(file,file.translate(table)) # Rename file
    except PermissionError: # Skips files with special permissions
        pass
end = time.time()

print("\nTranslation complete! [",round((end-start),3),"seconds ]")
                                          
                                          


