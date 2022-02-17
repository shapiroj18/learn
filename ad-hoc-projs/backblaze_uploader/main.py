import glob
import os
import subprocess

pathname = '/Users/jonathanshapiro/Desktop/Git/phishjams-backend/app/static/img/livephish_logos/*'

for file in glob.glob(pathname):
    subprocess.run(['b2', 'upload-file', 'phishAlbumCovers', file, os.path.basename(file)])
    