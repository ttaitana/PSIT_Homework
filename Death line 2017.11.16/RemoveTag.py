"""remove tag"""
def remove_tag(html, read, col_text):
    """remove tag html"""
    for i in html:
        if i == '>':
            read = True
            continue
        elif i == '<':
            read = False
            col_text += ' '
            continue
        if read:
            col_text += i
    return col_text.split()
print(remove_tag(input(), True, ''))
