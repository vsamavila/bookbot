def sort_by_num(d):
    return d["num"]

def get_word_count(book: str) -> int:
    count = len(book.split())

    return count

def get_letter_count(book: str) -> dict[str, int]:
    char_count = {}

    for char in book:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1

    return char_count

def get_sorted_dict(char_dict):
    final_list = []

    for char in char_dict:
        value = char_dict[char]
        new_dict_entry = {"char": char, "num": value}

        final_list.append(new_dict_entry)

    final_list.sort(reverse=True, key=sort_by_num)

    return final_list


