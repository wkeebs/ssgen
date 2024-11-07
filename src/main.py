from copy_contents import copy_dir_contents

def main():
    src = "static/"
    dest = "public/"
    copy_dir_contents(src, dest)
    


if __name__ == "__main__":
    main()
