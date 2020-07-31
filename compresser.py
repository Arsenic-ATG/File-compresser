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

	# TODO: Walk the entire folder tree and compress the files in each folder.

	print('Done.')