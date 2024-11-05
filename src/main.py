from text_node import TextNode, TextType
from utils import split_nodes_delimiter

def main():
    nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT),
            TextNode("This is text *with some* italics", TextType.TEXT),
            TextNode("This is **text with some bold**", TextType.TEXT),
            TextNode("This is normal text!", TextType.TEXT)
        ]
    bold_split = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split,"*",TextType.ITALICS)
    new_nodes = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    main()
