def main():
    with open("books/frankenstein.txt") as f:
        book = f.name
        file_contents = f.read()
        words = file_contents.split()
        mydict = char_count(file_contents)
        report(book, words, mydict)

def report(book, words, mydict):
    print(f"--- Begin report of {book} ---")
    print(f"{len(words)} words found in the document\n")
    sorted_chars = sorted(mydict.items(), key=lambda item: item[1], reverse=True)
    for i, x in sorted_chars:
        if i.isalpha():
            print(f"The '{i}' character was found {x} times")
    print("--- End report ---")
    return

def char_count(file_contents):
    char_dict = {}
    file_contents = file_contents.lower()
    for i in file_contents:
        try:
            char_dict[i] += 1
        except:
            char_dict[i] = 1
    return char_dict

main()