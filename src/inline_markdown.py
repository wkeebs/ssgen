import re
from text_node import TextNode, TextType
from types import FunctionType

def text_to_textnodes(text: str) -> list[TextNode]:
    """
    : @summary :
    Converts some text to TextNode format.
        1. Converts base string to TextNode.
        2. Chains curried splitter functions for:
            * bold -> italic -> code -> images -> links
    ___________________

    : @args :
        * text (str): _description_
    ___________________

    : @returns : 
        * list[TextNode]: _description_
    ___________________
    """
    bold_split = split_nodes_delimiter("**", TextType.BOLD)
    italic_split = split_nodes_delimiter("*", TextType.ITALICS)
    code_split = split_nodes_delimiter("`", TextType.CODE)
    
    # all splitter functions
    # NOTE: bold must come before italics as the syntax is a superset
    splitters = [
        bold_split,
        italic_split,
        code_split,
        split_nodes_image,
        split_nodes_link,
    ]
    
    node = TextNode(text, TextType.TEXT)
    nodes = [node]
    for splitter in splitters:
        nodes = splitter(nodes)
    
    return nodes


def split_nodes_delimiter(delimiter: str, text_type: TextType) -> list[TextNode]:
    """
    : @summary :
    [**CURRIED**] Splits a list of text nodes by a delimiter and supplied type.
    ___________________

    : @args :
        * old_nodes (list[TextNode]): the nodes to be split
        * delimeter (str): the delimiter to split by
        * text_type (TextType): the type of formatted text to split by
    ___________________

    : @returns : 
        * list[TextNode]: the new, split text nodes
    ___________________
    """
    def split_nodes(old_nodes: list[TextNode]) -> list[TextNode]:
        new_nodes = []

        # split the nodes
        for old_node in old_nodes:
            split_text = old_node.text.split(delimiter)

            if len(split_text) % 2 == 0:
                raise ValueError("Invalid markdown: formatted section not closed")

            for idx, text in enumerate(split_text):
                if text == "":
                    # .split() generates empty strings if nothing exists
                    # before or after the delimiter
                    continue

                # the formatted nodes have odd indices
                if idx % 2 == 0:
                    new_nodes.append(
                        TextNode(text=text, text_type=old_node.text_type))
                else:
                    new_nodes.append(TextNode(text=text, text_type=text_type))

        return new_nodes
    return split_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    : @summary :
    Extracts image data from markdown text.
    For example:
        "Text with ![an image](src/image.png) and ![another](image2.jpg)"
    returns
        [("an image", "src/image.png"), ("another", "image2.jpg")]
    ___________________

    : @args :
        * text (str): the markdown text to extract from
    ___________________

    : @returns : 
        * list[tuple[str, str]]: a list of images as (alt text, URL)
    ___________________
    """
    regexp = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regexp, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    : @summary :
    Extracts link data from markdown text.
    For example:
        "Text with [a link](www.google.com) and [another](boot.dev)"
    returns
        [("a link", "www.google.com"), ("another", "boot.dev")]
    ___________________

    : @args :
        * text (str): the markdown text to extract from
    ___________________

    : @returns : 
        * list[tuple[str, str]]: a list of images as (alt text, URL)
    ___________________
    """
    regexp = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regexp, text)


def split_nodes(old_nodes: list[TextNode], replace_type: TextType, extract_function: FunctionType, expr_start: str = None) -> list[TextNode]:
    """
    : @summary :
    Splits a list of nodes, extracting their images or links into respective
    IMAGE and TEXT nodes. This is based on an input parameter.
    ___________________

    : @args :
        * old_nodes (list[TextNode]): the nodes to extract from
        * split_by_images (bool): do we split by images or links?
    ___________________

    : @returns : 
        * list[TextNode]: the new nodes
    ___________________
    """
    new_nodes = []

    for old_node in old_nodes:
        # extract the image links
        delimiters = extract_function(old_node.text)

        # split by each link
        split_nodes = [old_node]  # the nodes split by the current link
        for alt, url in delimiters:
            expression = f"[{alt}]({url})"  # full expr to split by
            if expr_start is not None:
                expression = expr_start + expression

            new_split_nodes = []
            for node in split_nodes:
                if node.text_type != TextType.TEXT:
                    # already processed
                    new_split_nodes.append(node)
                    continue

                split_text = node.text.split(expression)
                num_links = len(split_text) - 1
                nodes_to_add = list(
                    map(lambda t: TextNode(t, TextType.TEXT), split_text))

                # insert the link at each odd index in range
                # (only applicable if the link appears multiple times in
                # the same string; usually just adds once)
                for i in range(num_links):
                    idx = 1 + (i * 2)  # 1, 3, 5, 7, ...
                    link_node = TextNode(alt, replace_type, url)
                    nodes_to_add.insert(idx, link_node)
                new_split_nodes.extend(nodes_to_add)

            # replace our current nodes to repeat for all links
            split_nodes = new_split_nodes

        # filter out empty TEXT nodes
        filtered_nodes = list(
            filter(lambda n: n.text != "" or n.text_type != TextType.TEXT, split_nodes))
        new_nodes.extend(filtered_nodes)

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    : @summary :
    Splits a list of nodes based on any images present in their text.
    ___________________

    : @args :
        * old_nodes (list[TextNode]): the nodes
    ___________________

    : @returns : 
        * list[TextNode]: the split nodes
    ___________________
    """
    return split_nodes(old_nodes=old_nodes, replace_type=TextType.IMAGE, extract_function=extract_markdown_images, expr_start="!")


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    : @summary :
    Splits a list of nodes based on any links present in their text.
    ___________________

    : @args :
        * old_nodes (list[TextNode]): the nodes
    ___________________

    : @returns : 
        * list[TextNode]: the split nodes
    ___________________
    """
    return split_nodes(old_nodes=old_nodes, replace_type=TextType.LINK, extract_function=extract_markdown_links)
