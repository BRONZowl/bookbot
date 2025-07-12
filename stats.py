# stats.py

# Counts how many words are in a document
def get_num_words(path: str) -> str:
    with open(path, "r") as file:
        text = file.read()
        return text

# Counts the number of times each character appears in the text


def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Sorts characters from most to least frequent


def sort_characters_by_count(char_counts: dict) -> list:
    sorted_list = [{"char": char, "num": count}
                   for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
