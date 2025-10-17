

def markdown_to_blocks(markdown):
    lines = [line.rstrip() for line in markdown.split('\n')]
    text = '\n'.join(lines)
    raw_blocks = text.split("\n\n")
    
    blocks = []
    for block in raw_blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            if stripped_block.startswith("```"):
                blocks.append(stripped_block)
            else:
                normalized = "\n".join(line.strip() for line in stripped_block.split("\n"))
                blocks.append(normalized)
    return blocks
