import re

def extract_markdown_links(text):
    matches = re.findall(r'(?<!\[)\[(?![^\]]*?\((?:https?|ftp|mailto):[^\)]*\)[^\]]*\])([^\]]*)\]\(([^\)]+)\)',text)
    if not matches:
        return None
    return matches

