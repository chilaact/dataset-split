import os
import os.path as osp
import shutil as sh

def list_dirs(path):
    '''
    Given a path, it will return all subdirectories in it
    (except hidden ones).
    '''
    dirs = [f for f in os.listdir(path) if osp.isdir(osp.join(path, f))]
    #Filter hidden directories
    dirs = list(filter(lambda x: x[0] != '.', dirs))
    return dirs

def create_dirs(path, dirs):
    '''
    Recieves a list of dirs and a path.
    Will create empty dirs inside the path.
    '''
    for d in dirs:
        os.mkdir(osp.join(path, d))

def remove_dirs(path, dirs):
    '''
    Recieves a list of dirs and a path.
    Will remove recursively every listed directories
    inside the path and anything inside them.
    '''
    for d in dirs:
        sh.rmtree(osp.join(path, d))
