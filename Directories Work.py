from pathlib import Path

# Absolute Path -> starting from the root hdd
# Relative Path -> starting from current directory

path = Path()
for file in (path.glob("*.py")):
    print(file)

#  .glob -> search files  .mkdir -> create directory  .rmdir -> remove directory
