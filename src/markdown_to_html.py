from html_node import HTMLNode
from parent_node import ParentNode
from leaf_node import LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, block_type_to_html_tag, get_heading_level, text_to_list_nodes
from inline_markdown import text_to_children


def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    : @summary :
    Converts a string of markdown text to one HTMLNode.
    This HTMLNode will be a parent node containing all content.
    ___________________

    : @args :
        * markdown (str): the markdown to convert
    ___________________

    : @returns : 
        * HTMLNode: the new HTMLNode
    ___________________
    """
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)

    # create nodes based on each block
    nodes = []
    for block in blocks:
        nodes.append(block_to_html_node(block))

    # create one parent node for the document
    return ParentNode(tag="div", children=nodes)


def block_to_html_node(block: str) -> HTMLNode:
    """
    : @summary :
    Converts a single block of markdown to a corresponding HTML node.
    ___________________

    : @args :
        * block (str): the markdown
    ___________________

    : @returns : 
        * HTMLNode: the node
    ___________________
    """
    # get type
    block_type = block_to_block_type(block)
    
    # get the corresponding tag
    if block_type == BlockType.HEADING:
        level = get_heading_level(block)
        if level == -1:
            tag = "p"
        else:
            tag = f"h{level}"
    else:
        tag = block_type_to_html_tag(block_type)

    # process the string to get raw text
    if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
        # convert to <li> elements
        children = text_to_list_nodes(block, block_type)
    elif block_type == BlockType.CODE:
        block = f"`{block.strip("`").strip()}`"
        children = text_to_children(block)
    else:
        block = block.replace("\n", " ") # remove newlines
        if block_type == BlockType.HEADING:
            # strip the heading characters
            block = block.lstrip("#").lstrip()
        elif block_type == BlockType.QUOTE:
            # strip the "> "
            block = block.replace("> ", "")
        
        children = text_to_children(block)

    return ParentNode(tag=tag, children=children)
