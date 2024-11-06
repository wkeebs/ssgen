from text_node import TextNode, TextType
from inline_markdown import text_to_textnodes

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    for n in nodes:
        print(n)


if __name__ == "__main__":
    main()
