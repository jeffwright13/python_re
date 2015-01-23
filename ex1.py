import re

def main():
    try:
        fh = open("simpsons_phone_book.txt")
    except:
        print 'Error opening file'

    for line in fh.readlines():
        if re.search(r'[jJ].*Neu', line):
            print line.strip()
    
if __name__ == "__main__":
    main()