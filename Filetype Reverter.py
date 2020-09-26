import glob, os
list_of_files = glob.glob('/Users/User/Desktop/') # CHANGE THIS LINE SO THAT IT GOES TO THE FILE YOU WANT TO CHANGE
for latest_file in range(len(list_of_files)):
    os.rename(list_of_files[latest_file],list_of_files[latest_file].replace(".rbxm",".ppt")) #REPLACE .ppt WITH YOUR FILE TYPE.
