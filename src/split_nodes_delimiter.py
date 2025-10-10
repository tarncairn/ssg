from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #from old nodes, split using delimiter
    if not delimiter:
        return old_nodes
    if not text_type:
        return old_nodes
    if delimiter == "":
        return old_nodes
    result = []
    for node in old_nodes:
        if node.text_type != "text":
            result.append(node)
            continue
        parts = node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError("No matching closing delimiter was found. Invalid Markdown syntax.")
        
        
        for i in range(len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    result.append(TextNode(text=parts[i], text_type=TextType.TEXT))
                else:
                    text_type_enum = TextType(text_type)
                    result.append(TextNode(text=parts[i], text_type=text_type))
    return result


