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
