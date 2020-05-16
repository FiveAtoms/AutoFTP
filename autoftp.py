import os, sys, time
from ftplib import FTP
import getpass


serverAddress = ""
serverUsername = ""


def files_to_timestamp(path):
	files = [os.path.join(path, f) for f in os.listdir(path)]
	return dict ([(f, os.path.getmtime(f)) for f in files])


# FTP functions

def update(filename, fullFilename):
	ftp = FTP(serverAddress)
	ftp.login(serverUsername, password)

	ftp.cwd(serverFolder)
	
	if os.path.isdir(fullFilename):
		ftp.mkd(filename)
	else:
		with open(fullFilename, 'rb') as f:
			ftp.storbinary('STOR %s' % filename, f)

	ftp.quit()
	
	print("Uploaded: " + filename)

def remove(filename, fullFilename):
	ftp = FTP(serverAddress)
	ftp.login(serverUsername, password)

	ftp.cwd(serverFolder)

	if filename in ftp.nlst(serverFolder):
		ftp.delete(filename)
		print("Deleted: " + filename)
	else:
		print("The file '{0}' was not removed because it was not found on the server.".format(filename))

	ftp.quit()



if __name__ == "__main__":
	path_to_watch = input("Local path: ")
	serverFolder = input("Remote path: ")
	
	# For security I dislike keeping passwords
	# in code files, thus I ask for it everytime
	# you launch AutoFTP
	password = getpass.getpass("FTP Password: ")
	
	if path_to_watch == "":
		path_to_watch = os.getcwd()
	
	print('Watching {}..'.format(path_to_watch))

	before = files_to_timestamp(path_to_watch)

	while 1:
		time.sleep (2)
		after = files_to_timestamp(path_to_watch)

		added = [f for f in after.keys() if not f in before.keys()]
		removed = [f for f in before.keys() if not f in after.keys()]
		modified = []

		for f in before.keys():
			if not f in removed:
				if os.path.getmtime(f) != before.get(f):
					modified.append(f)
		
		if added: 
			filename = os.path.basename('{}'.format(', '.join(added)))
			fullFilename = '{}'.format(', '.join(added))
			
			# If the file doesn't exist, the update
			# function will automatically create a
			# new file
			update(filename, fullFilename)
		if removed: 
			filename = os.path.basename('{}'.format(', '.join(removed)))
			fullFilename = '{}'.format(', '.join(removed))
			
			remove(filename, fullFilename)
		if modified: 
			filename = os.path.basename('{}'.format(', '.join(modified)))
			fullFilename = '{}'.format(', '.join(modified))
			
			update(filename, fullFilename)

		before = after