import os
from markdown_to_html import markdown_to_html_node


def extract_title(markdown: str) -> str:
    """
    : @summary :
    Extracts the title from a string of valid markdown.
    e.g., # Title
    Raises an exception if no title is found.
    ___________________

    : @args :
        * markdown (str): the markdown to extract from
    ___________________

    : @returns : 
        * str: the title text
    ___________________
    """
    lines = markdown.split("\n")
    for l in lines:
        line = l.strip()
        if line[:2] == "# ":
            return line[2:].strip()
    raise Exception("Title not found")


def generate_page(from_path: str, template_path: str, dest_path: str) -> bool:
    """
    : @summary :
    Generates a HTML page from a markdown file.
    ___________________

    : @args :
        * from_path (str): the markdown source
        * template_path (str): the HTML template
        * dest_path (str): the destination to write to
    ___________________

    : @returns : 
        * bool: success?
    ___________________
    """
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    markdown = None
    try:
        with open(from_path, 'r') as from_file:
            markdown = from_file.read()
    except Exception as e:
        print(f"Failed to open {from_path}: {e}")
        return False

    print(f"From: {from_path} successfully read")

    # convert to html
    node = markdown_to_html_node(markdown)
    html_content = node.to_html()
    title = extract_title(markdown)

    print("Converted Markdown to HTML")

    # read template
    template = None
    try:
        with open(template_path, 'r') as from_file:
            template = from_file.read()
    except Exception as e:
        print(f"Failed to open {template_path}: {e}")
        return False

    print(f"Template: {template_path} successfully read")

    # insert content
    full_html_content = template.replace(
        "{{ Title }}", title).replace("{{ Content }}", html_content)

    # write to output
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)  # generate dirs
        with open(dest_path, "w") as dest_file:
            dest_file.write(full_html_content)
    except Exception as e:
        print(f"Failed to write to {dest_path}: {e}")
        return False

    print(f"Dest: {dest_path} written successfully")
    return True


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> bool:
    """
    : @summary :
    Recursively generates HTML pages from a directory of markdown content.
    ___________________

    : @args :
        * dir_path_content (str): the source directory
        * template_path (str): the HTML template
        * dest_dir_path (str): the destination directory
    ___________________

    : @returns : 
        * bool: success?
    ___________________
    """
    for filename in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                print(f"Generating page from: {file_path}")
                dest_filename = filename.replace(".md", ".html")
                dest_file_path = os.path.join(dest_dir_path, dest_filename)
                generate_page(file_path, template_path, dest_file_path)
            elif os.path.isdir(file_path):
                print(f"Traversing: {file_path}")
                new_path = os.path.join(dest_dir_path, filename)
                os.mkdir(new_path)
                generate_pages_recursive(file_path, template_path, new_path)
        except Exception as e:
            print(f'Failed to crawl {file_path}. Reason: {e}')
            return False
