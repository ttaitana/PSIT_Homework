"""Run Length Decoding"""
def decode(text, length):
    """decoding"""
    if text[length:length+4].isdigit():
        print(int(text[length:length+4])*text[length+4], end='')
        length += 5
    elif text[length:length+3].isdigit():
        print(int(text[length:length+3])*text[length+3], end='')
        length += 4
    elif text[length:length+2].isdigit():
        print(int(text[length:length+2])*text[length+2], end='')
        length += 3
    else:
        print(int(text[length])*text[length+1], end='')
        length += 2
    if length < len(text):
        decode(text, length)
decode(input(), 0)
