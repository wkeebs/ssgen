
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
    