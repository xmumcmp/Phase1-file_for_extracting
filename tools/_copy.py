import os.path
import shutil
direction = os.getcwd()
for files in os.listdir(os.path.join(direction,'errlog')):
    print(files)
    shutil.copy(os.path.join(direction,'middle',files[0:-3]+'txt'),os.path.join(direction,'copy',files[0:-3]+'txt'))
