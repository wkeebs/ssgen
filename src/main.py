from generate_page import generate_page
from copy_contents import copy_dir_contents

def main():
    # copy static/ into public/
    copy_dir_contents("static/", "public/")
    
    # generate content
    from_path, template, dest_path = "content/index.md", "template.html", "public/index.html"
    generate_page(from_path, template, dest_path)


if __name__ == "__main__":
    main()
