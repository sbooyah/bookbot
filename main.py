def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().split()
        print(f"{len(file_contents)} words were found in the document")


def count_characters():
    character_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        for char in file_contents:
            if char.isalpha() and char.lower() in character_dict:
                character_dict[char.lower()] += 1
            elif char.isalpha():
                character_dict[char.lower()] = 1
            elif not char.isalpha() and char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    for char in character_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {character_dict[char]} times")


#=====================================

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    count_words()
    count_characters()
    print("--- End report ---")
main()