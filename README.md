# Static Site Generator 📄

This is a simple static site generator I built in Python.

## Markdown

The generator takes **markdown** files as input, and generates static
HTML output based on the content provided.

## Conversion

To create the HTML content, the generator first converts the markdown to an
internal format of `HTMLNode`s, and then translates that into a valid HTML
representation which is then generated as a .html file for each .md file.

`Markdown Files (.md) -> HTMLNodes -> HTML Files (.html)`

So, for example, we might translate the following markdown:

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

And represent the internal structure as something like:

```text
h1: value="My Heading"
h2: value="My Subheading 1"
ul: children=[
    li: value="this is a list item",
    li: value="so is this",
    li: value="and this"
]
h3: value="My Subheading 2"
p: value="Hello world!"
a: value="A link", url="https://github.com/wkeebs/ssgen"
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
