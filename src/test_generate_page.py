import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        text = "# Title"
        self.assertEqual(extract_title(text), "Title")
        
        text = """## Heading 2
    #      Heading 1
        paragraph
""" 
        self.assertEqual(extract_title(text), "Heading 1")

        text = "### No title"
        output = None
        try:
            title = extract_title(text)
        except Exception as e:
            output = str(e)
        self.assertNotEqual(output, None)

if __name__ == "__main__":
    unittest.main()
