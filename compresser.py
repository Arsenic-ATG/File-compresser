# backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import os,zipfile

def backup_to_zip(folder):
	# Backup the entire contents of "folder" into a ZIP file.
	folder = os.path.abspath(folder)

	# Figure out the filename this code should use based on what files already exist.
	number = 1;
	while True:
		zipFile_name = os.path.basename(folder) + '_' + str(number) + '.zip'

		if not os.path.exist(zipFile_name):
			break

		number + number + 1

	# Create the ZIP file.
	print("creating %s...",zipFile_name)
	backup = zipfile.ZipFile('zipFile_name','w')

	# Walk the entire folder tree and compress the files in each folder.
	for foldername,subfolder,filenames in os.walk(folder):
		print("Adding file %s...",foldername)
		
		# Add the current folder to the zip file
		backup.write(foldername)
		
		# Adding all the files to the backup folder
		for filename in filenames:
			# TODO: Find a way to exclude already backed up files 
			# Add the reamaining files to the zipfile
			backup.write(os.path.join(foldername,filename))
			
	backup.close()
	print('Done.')