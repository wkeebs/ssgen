# Static Site Generator

This is a simple static site generator I built in Python.

## Markdown

The generator takes **markdown** files as input, and generates static
HTML output based on the content provided.

## Conversion

To convert the markdown content, the generator first converts it to an
internal format of `HTMLNode`s, and then translates that into a valid HTML
representation which is then generated as a .html file for each .md file.

`Markdown Files (.md) -> HTMLNode -> HTML Files (.html)`

So, for example, we might translate the following markdown:

```markdown
# My Heading
## My Subheading 1
Content content content

### My Subheading 2
Hello World!
[A link](https://github.com/wkeebs/ssgen)
```

And represent the internal structure as something like:

```text
h1: value="My Heading"
h2: value="My Subheading 1"
p: value="Content content content"
h3: value="My Subheading 2"
p: value="Hello world!"
a: value="A link", url="https://github.com/wkeebs/ssgen"
```

This is then converted to the following HTML:

```html
<h1>My Heading</h1>
<h2>My SubHeading 1</h2>
<p>Content content content</p>
<h3>My Subheading 2</h3>
<p>Hello world!</p>
<a href="https://github.com/wkeebs/ssgen">A link</a>
```

This would then be rendered as something like:

## My Heading

### My Subheading 1

Content content content

#### My Subheading 2

Hello World!
[A link](https://github.com/wkeebs/ssgen)
