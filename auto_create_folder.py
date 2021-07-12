import os


# get current path
currentPath = os.getcwd()
print('This is the current path:',currentPath)

# change to new path
# cwd = Current Working Directory
changedPath = os.chdir(r'C:\Users\Monster Chick\Desktop')
print('This is the path changed:',os.getcwd())

def mk_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

        print('successfully created!')
    else:
        print('folder exists...')

# new path & name of the folder will be made
mk_dir(os.getcwd() + r'\new_folder')


