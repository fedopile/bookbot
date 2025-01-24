def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    charc = charcount(file_contents)
    words = file_contents.split()
    print(charc)
    print("--- Begin report of ",path_to_file," ---")
    print(len(words)," words found in the document")
    print()
    for chark, charv in charc.items():
        print("The '",chark,"' character was found ",charv," times")

def charcount(string:str):
    low = string.lower()
    loldict = {}
    for char in low:
        if char in loldict:
            loldict[char] = loldict[char]+1
        elif char.isalpha():
            loldict[char] = 1
    return loldict

main()