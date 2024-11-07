from enum import Enum


class BlockType(Enum):
    """
    : @summary :
    Enumerator for blocks of markdown.
    ___________________
    """
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    """
    : @summary :
    Splits markdown into a list of blocks, stripping any whitespace.
    ___________________

    : @args :
        * markdown (str): the markdown to split
    ___________________

    : @returns : 
        * list[str]: the blocks
    ___________________
    """
    blocks = map(lambda b: b.strip(), markdown.split(
        "\n\n"))  # split and strip whitespace
    # filter empty blocks
    return list(filter(lambda b: b != "" and b != "\n", blocks))


def all_lines_start_with(prefix: str, text: str) -> bool:
    """
    : @summary :
    Determines if all lines of a block of text start with a given prefix.
    ___________________

    : @args :
        * prefix (str): the prefix to check for
        * text (str): the text to check
    ___________________

    : @returns : 
        * bool: do all lines start with the prefix?
    ___________________
    """
    lines = text.split("\n")
    for l in lines:
        if len(l) < len(prefix) or l[:len(prefix)] != prefix:
            return False
    return True


def block_to_block_type(block: str) -> BlockType:
    """
    : @summary :
    Determines the block type for a given block of markdown text, 
    based on how it is prefixed.
    ___________________

    : @args :
        * block (str): the block to analyse
    ___________________

    : @returns :
        * BlockType: the determined block type
    ___________________
    """
    match block[0]:
        case '#':
            count = 0
            for char in block:
                if char != '#':
                    break
                count += 1
            if count > 6 or block[count] != ' ':
                return BlockType.PARAGRAPH
            return BlockType.HEADING
        case '`':
            if len(block) < 6 or block[:3] != "```" or block[-3:] != "```":
                return BlockType.PARAGRAPH
            return BlockType.CODE
        case '>':
            return BlockType.QUOTE if all_lines_start_with('>', block) else BlockType.PARAGRAPH
        case '*':
            return BlockType.UNORDERED_LIST if all_lines_start_with('* ', block) else BlockType.PARAGRAPH
        case '-':
            return BlockType.UNORDERED_LIST if all_lines_start_with('- ', block) else BlockType.PARAGRAPH
        case '1':
            lines = block.split("\n")
            for idx, l in enumerate(lines):
                if len(l) < 3 or l[:3] != f"{idx+1}. ":
                    return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH


def block_type_to_html_tag(type: BlockType) -> str:
    """
    : @summary :
    Converts a given BlockType to its corresponding HTML tag.
    ___________________

    : @args :
        * type (BlockType): the block type
    ___________________

    : @returns : 
        * str: the html tag
    ___________________
    """
    match type:
        case BlockType.PARAGRAPH:
            return "p"
        case BlockType.HEADING:
            # NOTE: Use the get_heading_level to get the correct heading tag
            return "h1"
        case BlockType.CODE:
            return "pre"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case _:
            return "p"


def get_heading_level(block: str) -> int:
    """
    : @summary :
    Determines the level of heading for a given block of markdown.
    ___________________

    : @args :
        * block (str): the heading text
    ___________________

    : @returns : 
        * int: the level of heading [1-6]
    ___________________
    """
    level = 0
    for char in block:
        if char != '#':
            break
        level += 1
    if level == 0 or level > 6 or block[level] != ' ':
        return -1  # invalid heading level / format
    return level
