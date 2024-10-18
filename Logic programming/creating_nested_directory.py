from pathlib import Path
Path("D:/demo_directory/directory").mkdir(parents = True, exist_ok = True)
#exist_ok is added to not throw an error when program is run again and the idrectory already exists 