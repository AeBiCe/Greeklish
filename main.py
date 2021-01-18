import os

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


directory = input("Enter directory:")
if os.path.isdir(directory): # If directory exists
    os.chdir(directory) # Change dir to input
else:
    print("\nInvalid directory!\n")
    while not os.path.isdir(directory):
        directory = input("Enter a new directory:")

os.chdir(directory) # Change dir to input
files = os.listdir(os.getcwd()) # Get files in directory

for file in files:
    table = file.maketrans(greek, english)  # Map characters
    os.rename(file,file.translate(table))   # Rename

print("Translation complete!")
                                          
                                          


