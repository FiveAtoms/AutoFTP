# AutoFTP
A simple Python command line tool to automatically keep local folders synced with FTP folders.

## Basic usage

You just need to modify two variables in autoftp.py to get it setup. Modify the following variables: "serverAddress" and "serverUsername" on lines 6 and 7 respectively.

Simply run the autoftp.py file from your terminal (python3 autoftp.py). It will ask for the local folder to watch (this is NOT relative to it's location, so be sure to enter the full path). It will then ask for the remote path, which is the folder on your FTP server that you want to keep in sync with your local folder. It then asks for your FTP password.

It will then run a simple loop that will print out changes you make.

Limitations:

In its current phase, AutoFTP has issues with you renaming files, of course, it will upload the new file but the old file will still be on your server. This is a simple fix that should be coming soon.