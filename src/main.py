from text_node import TextNode, TextType
from inline_markdown import text_to_textnodes
from block_markdown import *

def main():
    text = \
"""1.  
3.  test
3. list"""
    print(block_to_block_type(text))
    


if __name__ == "__main__":
    main()
