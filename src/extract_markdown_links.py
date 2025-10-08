import re

def extract_markdown_links(text):
    matches = re.findall(r'(?<!\[)\[(?![^\]]*?\((?:https?|ftp|mailto):[^\)]*\)[^\]]*\])([^\]]*)\]\(([^\)]+)\)',text)
    if matches:
        return matches
    else:
        return "No matches were found."

