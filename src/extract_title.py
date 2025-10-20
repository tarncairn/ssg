

def extract_title(markdown):
    blocks = markdown.split('\n')
    for block in blocks:
        stripped = block.strip()
        if stripped.startswith("# "):
            return stripped[2:]
    raise Exception("There is no h1 header.")
