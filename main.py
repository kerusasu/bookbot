def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    lowered_string = text.lower()
    for ch in lowered_string:
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    return char_dict

def convert_to_list(dictionary):
    list_of_dicts = []
    for key, value in dictionary.items():
        list_of_dicts.append({"ch": key, "count":value})
    return list_of_dicts

def return_ch(dict):
    return dict["ch"]

def filter_and_sort(dic):
    new_list = []
    for _ in dic:
        if _["ch"].isalpha():
            new_list.append(_)
    new_list.sort(reverse=True, key=return_ch)
    return new_list

def print_report(text):
    word_count = count_words(text)
    character_count = count_characters(text)
    character_list = convert_to_list(character_count)
    sorted_characters = filter_and_sort(character_list)

    print(f"--- Begin report ---\n\n"\
          f"{word_count} words found in the document\n")
    
    for _ in sorted_characters:
        print(f"The {_["ch"]} was found {_["count"]} times")

    print("\n--- End report ---")
    
main()