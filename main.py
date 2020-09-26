import webbrowser, time, glob, os
ID = int(input("Input the ID you'd like to download: "))
SaveAs = input("Save as file type? ('rbxm' or 'rbxl'): ")
maxVersions = int(input("Latest version serial (≥1): "))
Version = 1
time.sleep(2)
while Version <= maxVersions:
    webbrowser.open('https://assetdelivery.roblox.com/v1/asset/?id='+str(ID)+'&version='+str(Version))
    print("Downloading version "+str(Version)+"...")
    time.sleep(3)
    list_of_files = glob.glob('/Users/User/Downloads/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    try:
        os.rename(latest_file,"/Users/User/Downloads/Version "+str(Version)+"."+SaveAs)
    except:
        print("ERROR: A file with the name 'Version "+str(Version)+"."+SaveAs+"' already exists. Move or delete this file and run this program again.")
        quit
    Version = Version + 1
