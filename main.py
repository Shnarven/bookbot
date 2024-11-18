def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    c_count = character_count(text)
    print(c_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    word = book.split()
    word_count=len(word)
    return(word_count)

def character_count(book):
    character_dict={}
    for c in book:
        lowered = c.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return(character_dict)    

main()
