# backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.
import os
from zipfile import ZipFile
import argparse


def backup_to_zip(folder):
    """
    Backup the entire contents of "folder" into a ZIP file in ./backup directory.
    :param folder: str
    :return: None
    """


    if not os.path.exists("backup"):
        os.mkdir("backup")
    os.chdir("backup")

   # increment file suffix number if it already exists.
    inc = 0
    while os.path.exists(folder.split("/")[-1] + "_%s.zip" % inc):
        inc += 1
    zip_file_name = folder.split("/")[-1]+ "_" + str(inc) + ".zip"

    # Create the ZIP file
    print("Zipping file "+folder_name+" into backup/"+zip_file_name)

    with ZipFile(zip_file_name, 'w') as zipf:
        # writing each file one by one
        for root, dirs, files in os.walk(folder):
            for file in files:
                zipf.write(os.path.join(root, file),arcname=os.path.join(root.replace(folder, ""), file))
                # print(os.path.join(root, file))
    print('Done')


if __name__ == "__main__":

    # Read folder name from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', required=True, help="Enter absolute folder name of the file to be zipped")
    args = parser.parse_args()
    folder_name = args.folder

    #print(folder_name)
    backup_to_zip(folder_name)