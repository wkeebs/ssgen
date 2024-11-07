from text_node import TextNode, TextType
from markdown_to_html import markdown_to_html_node

def main():
    text = \
"""
# Heading

## Subheading

- unordered list
- another *italic* item
- and another

this is some **bold** paragraph text

```
This is a code block with some code in it
```

> this is a quote
> with multiple lines

### this is a heading at the bottom

1. with an ordered list in it
2. which has some items
"""
    html_nodes = markdown_to_html_node(text)
    print(html_nodes)

    


if __name__ == "__main__":
    main()
