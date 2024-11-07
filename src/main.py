from generate_page import extract_title

def main():
    text = """## Test
  #      MY TITLE
  
"""    
    print(extract_title(text))


if __name__ == "__main__":
    main()
