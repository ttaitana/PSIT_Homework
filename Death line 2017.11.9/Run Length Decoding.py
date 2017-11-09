"""Run Length Decoding"""
def main():
    """ Main function """
    text = input()
    saved_int = ''
 
    for i in text:
        if i.isdigit():
            saved_int += i
        elif i.isalpha():
            print(i * int(saved_int), end='')
            saved_int = ''
main()
