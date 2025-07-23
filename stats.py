

def get_num_words(booktext):
    words = booktext.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list

