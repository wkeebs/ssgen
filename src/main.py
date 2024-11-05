from text_node import TextNode, TextType
from inline import extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link

def main():
    node = TextNode(
            "This is text with the same image ![here](https://www.boot.dev) and ![here](https://www.boot.dev) and this is ![also here](www.keeble) and ![also here](www.keeble)",
            TextType.TEXT,
        )
    new_nodes = split_nodes_image([node])
    for n in new_nodes:
        print(n)


if __name__ == "__main__":
    main()
