from html_node import HTMLNode
from parent_node import ParentNode
from leaf_node import LeafNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, block_type_to_html_tag, get_heading_level
from inline_markdown import text_to_textnodes
from text_node import text_node_to_html_node


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

    # get nested inline children
    children = text_to_children(block)

    return ParentNode(tag=tag, children=children)


def text_to_children(text: str) -> list[HTMLNode]:
    """
    : @summary :
    Takes a string of text and returns a list of HTMLNodes that represents
    the lines of inline markdown.
    ___________________

    : @args :
        * text (str): the text to convert
    ___________________

    : @returns : 
        * list[LeafNode]: the nodes
    ___________________
    """
    # convert to TextNodes
    text_nodes = text_to_textnodes(text)

    # convert to HTMLNodes
    html_nodes = list(map(text_node_to_html_node, text_nodes))

    return html_nodes
