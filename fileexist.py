import os
import subprocess
import re
import glob



# path = 'E:\\New folder\apnproject\main-file/apn\MMLTask_PS-CS-\.'
for path in glob.glob('MMLTask_PS-CS-MAE*'):
    isFile = os.path.isfile(path)
    if (isFile):
        print("yes")
        subprocess.run(["python", "main.py"])
        print(path)
        os.remove(path)


