# Static Site Generator

This is a simple static site generator I built in Python.

## Markdown

The generator takes **markdown** files as input, and generates static
HTML output based on the content provided.

## Conversion

To convert the markdown content, the generator first converts it to an
internal format of `HTMLNode`s, and then translates that into a valid HTML
representation which is then generated as a .html file for each .md file.

'Markdown Files (.md) -> HTMLNode -> HTML Files (.html)`
