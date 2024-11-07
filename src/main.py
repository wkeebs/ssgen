from generate_pages import generate_pages_recursive
from copy_contents import copy_dir_contents

dir_path_static = "./static/"
dir_path_public = "./public/"
dir_path_content = "./content/"
template_path = "./template.html"

def main():
    copy_dir_contents(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()
