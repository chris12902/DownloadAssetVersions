# THIS PROGRAM IS NO LONGER MAINTAINED
In the case that this program no longer works in the future, please use this instead: https://gist.github.com/jmkd3v/a3139efc1f4de3d5ac50eb068f8efb61

--

# DownloadAssetVersions
This program downloads every version of an asset and automatically converts it to a .rbxm/.rbxl, depending on the user's choice.

# WARNING! PLEASE READ!

IN ORDER TO USE THIS PROGRAM, THE PLACE OR ASSET YOU'RE DOWNLOADING MUST FOLLOW ONE OF THESE CONDITIONS:

1. The game or model is open source. Players can freely edit the game in Studio or purchase or take the asset.

2. You must own the asset. If you use this program on an asset that you own, but did not create, it will still work. You can even use it on models that are offsale.

3. The asset must not be moderated. If the asset has a version that's moderated, but another version of the asset is just fine, it will still work, but you will be unable to download the moderated version. For example, if I was to download every version of a model and one of the versions of said model was moderated, the program will still open that version as a new tab but it will not be able to download anything, unless you are a Roblox administrator. If you are a Roblox administrator and you happen to be using this program... I'm flattered.

Now, with that being said, let me explain how this program works.

This program depends on the https://assetdelivery.roblox.com/v1/asset/?id=[ID]&version=[VERSION] API endpoint. If Roblox was to ever deprecate this endpoint, this program would immediately break.
To ensure that this program does not require you to pass your cookies to download each version of the asset, the program will open a tab for every single version of the asset, once every three seconds. Three seconds is the fastest rate this program can go at, so please do not make this number lower than it already is.

Once your computer finishes downloading one asset, this program will go into your Downloads folder and rename the most recent item it finds. A few of the runs I've had testing this program have converted some of my homework assignments into RBXM/RBXL files, but you can convert it back with ease. In fact, I have included a program to do this.
To test the full capabilities of this program, I downloaded and inspected every version of Roblox's "Digital Safety Scavenger Hunt" game, which was made by Roblox's educational wing. It's open source, so I'm able to download any version of the game. The .zip file containing every version of the Scavenger Hunt can be downloaded at https://github.com/chris12902/DownloadAssetVersions

The browser that works best with this program is Google Chrome, because unlike Firefox, Chrome does not ask the user if they want to download something from a website. This is potentially dangerous for the user, but in this purpose, it's awesome. (btw, you should switch to Firefox if you haven't already!)
