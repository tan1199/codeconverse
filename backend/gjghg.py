import os
import stat
import shutil


def make_writable(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


destination_folder = r'C:\\Users\\Tanmay Saini\\Desktop\\codeconverse\\backend\\repositories\\a\data\\ustropo_websocket-example'

# Replace this with your repository processing logic

# Delete the cloned repository
shutil.rmtree(destination_folder, onerror=make_writable)


