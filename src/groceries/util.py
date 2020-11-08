from os import path as ospath


def local_path(path, frompoint):
    return ospath.join(ospath.dirname(frompoint), path)
