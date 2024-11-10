# Static Site Generator 📄

This is a simple static site generator I built in Python.

The generator takes **markdown** files as input, and generates static HTML output based on the content provided.

## Conversion

To create the HTML content, the generator first converts the markdown to an internal format of `HTMLNode`s, and then translates that into a valid HTML representation which is then generated as a .html file for each .md file.

`Markdown Files (.md) -> HTMLNodes -> HTML Files (.html)`

So, for example, we might take the following markdown:

```markdown
# My Heading

## My Subheading 1

* this is a list item
* so is this
* and this

### My Subheading 2

Hello World!
[A link](https://github.com/wkeebs/ssgen)
```

And transform it into some internal structure that looks something like:

```text
ParentNode
Tag: div
    ParentNode
    Tag: h1
        LeafNode
        Value:
        "My Heading"

    ParentNode
    Tag: h2
        LeafNode
        Value:
        "My Subheading 1"

    ParentNode
    Tag: ul
        ParentNode
        Tag: li
            LeafNode
            Value:
            "this is a list item"

        ParentNode
        Tag: li
            LeafNode
            Value:
            "so is this"

        ParentNode
        Tag: li
            LeafNode
            Value:
            "and this"

    ParentNode
    Tag: h3
        LeafNode
        Value:
        "My Subheading 2"

    ParentNode
    Tag: p
        LeafNode
        Value:
        "Hello World! "

        LeafNode
        Tag: a
        Value:
        "A link"
        -- Props:
            href=https://github.com/wkeebs/ssgen
```

This is then converted to the following HTML:

```html
<h1>My Heading</h1>
<h2>My SubHeading 1</h2>
<ul>
    <li>this is a list item</li>
    <li>so is this</li>
    <li>and this</li>
</ul>
<h3>My Subheading 2</h3>
<p>Hello world!</p>
<a href="https://github.com/wkeebs/ssgen">A link</a>
```

This would then be rendered as something like:

---

# My Heading

## My Subheading 1

* this is a list item
* so is this
* and this

### My Subheading 2

Hello World!
[A link](https://github.com/wkeebs/ssgen)

---

## Using the Generator

When the `main.sh` script is executed, the following occurs:

1. Any files placed in the `static/` directory are first copied into the `public/` directory; overwriting the previous content.
2. Then, the markdown content from `content/` is transformed into HTML, which is also outputted into `public/`.
3. Finally, a Python web server is started to view the content.
