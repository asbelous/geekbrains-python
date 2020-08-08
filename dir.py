import os

def make_dir():
    for i in range(1, 10):
        folder = f'{i}'
        os.mkdir(folder)

def remove_dir():
    for i in range(1, 10):
        folder = f'{i}'
        os.rmdir(folder)
