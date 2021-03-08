import webbrowser, time, glob, os, math
from urllib.request import Request, urlopen
from urllib.error import HTTPError
ID = int(input("Input the ID you'd like to download: "))
SaveAs = input("Save as file type? ('rbxm' or 'rbxl'): ")
def findMaxVersions(id):
    Version = 1
    GrowBy = 25
    Rounds = 0
    GoingDown = False
    Found = False
    while not Found:
        #print("version "+str(Version)+"\tgrowby: "+str(GrowBy))
        try:
            req = Request('https://assetdelivery.roblox.com/v1/asset/?id='+str(id)+'&version='+str(Version), headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read().decode('utf-8')
            if not GoingDown:
                Version = Version + GrowBy
            else:
                GoingDown = False
                GrowBy = math.floor(GrowBy / 2)
                Version = Version + GrowBy
        except UnicodeDecodeError:
            if not GoingDown:
                Version = Version + GrowBy
            else:
                GoingDown = False
                GrowBy = math.floor(GrowBy / 2)
                Version = Version + GrowBy
        except HTTPError:
            if not GoingDown and Version == 1:
                Version = Version + 1
            elif GoingDown and Version == 1:
                GoingDown = False
                Version = Version + 1
            else:
                GrowBy = math.floor(GrowBy / 2)
                Version = Version - GrowBy
                GoingDown = True
        except:
            if Version == 1:
                exit
            else:
                GrowBy = math.floor(GrowBy / 2)
                Version = Version - GrowBy
                GoingDown = True
        if GrowBy == 0:
            #print("Largest AVID: "+str(Version-1))
            Found = True
    return Version - 1
gameName = input("Enter the name of the game: ")
maxVersions = int(input("Enter largest asset version ID (enter -1 if you aren't sure): "))
if maxVersions == -1:
    maxVersions = findMaxVersions(ID)
    print("This asset has "+str(maxVersions)+" IDs")
Version = 1
time.sleep(2)
while Version <= maxVersions:
    try:
        req = Request('https://assetdelivery.roblox.com/v1/asset/?id='+str(ID)+'&version='+str(Version), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf-8')
        webbrowser.open('https://assetdelivery.roblox.com/v1/asset/?id='+str(ID)+'&version='+str(Version))
        print("Downloading version "+str(Version)+"...")
        time.sleep(3)
        list_of_files = glob.glob('/Users/User/Downloads/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        try:
            os.rename(latest_file,"/Users/User/Downloads/"+gameName+str(Version)+"."+SaveAs)
        except:
            print("ERROR: A file with the name '"+gameName+str(Version)+"."+SaveAs+"' already exists. Move or delete this file and run this program again.")
            quit
    except:
        print("Error: Version "+str(Version)+" does not exist. Skipping to next version...")
    Version = Version + 1
