import os
import shutil


def copy_dir_contents(src: str, dest: str) -> bool:
    """
    : @summary :
    Copies the contents from one directory to another,
    overwriting the old content.
    ___________________

    : @args :
        * src (str): the source path
        * dest (str): the destination path
    ___________________

    : @returns : 
        * bool: success?
    ___________________
    """
    # validate paths
    if not os.path.exists(src):
        print(f"Source does not exist: {src}")
        return False

    if not os.path.exists(dest):
        print(f"Destination does not exist: {dest}")
        return False

    # print(f"Cleaning {dest} ...")

    # clean the destination directory
    for filename in os.listdir(dest):
        file_path = os.path.join(dest, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return False

    # print(f"{dest} successfully cleaned")
    # print(f"Copying {src} into {dest} ...")
    success = copy_contents(src, dest)
    return success


def copy_contents(src: str, dir: str) -> bool:
    """
    : @summary :
    Copies one directory into another recursively.
    ___________________

    : @args :
        * src (str): the source path
        * dir (str): the destination path
    ___________________

    : @returns : 
        * bool: success?
    ___________________
    """
    for filename in os.listdir(src):
        file_path = os.path.join(src, filename)
        try:
            new_path = os.path.join(dir, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                # print(f"File: {file_path} -> {new_path}")
                shutil.copy(file_path, new_path)
            elif os.path.isdir(file_path):
                # print(f"Dir: {new_path} -> {new_path}")
                new_dir = dir + filename
                os.mkdir(new_dir)
                copy_contents(file_path, new_dir)
        except Exception as e:
            print('Failed to copy in %s. Reason: %s' % (file_path, e))
            return False
    return True
