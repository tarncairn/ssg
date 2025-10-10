from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = r"#+ "
    CODE = r'^```[\s\S]+```$'
    QUOTE = r"^(?:>.*(?:\n>.*)*)$"
    OL = r"^(\s*\d+\.\s+\S.*\n?)+$"
    UL = r"^(\s*-\s\S.*\n?)+$"


    
def block_to_block_type(block):
    if not isinstance(block, str):
        raise ValueError("Blocks must be string.")
    if re.search(BlockType.HEADING.value, block):
        return BlockType.HEADING
    elif re.search(BlockType.CODE.value, block, re.DOTALL):
        return BlockType.CODE
    elif re.search(BlockType.QUOTE.value, block, re.DOTALL):
        return BlockType.QUOTE
    elif re.search(BlockType.UL.value, block, re.DOTALL):
        return BlockType.UL
    elif re.search(BlockType.OL.value, block, re.DOTALL):
        return BlockType.OL
    else:
        return BlockType.PARAGRAPH
