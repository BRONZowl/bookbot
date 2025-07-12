from stats import get_num_words, count_characters, sort_characters_by_count
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


def main():

    print("============ BOOKBOT =============")
    print("Analyzing book found at <path_to_book>...")

    text = get_num_words(book_path)
    word_count = len(text.split())

    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_characters_by_count(char_counts)

    print("--------- Character Count --------")
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():  # Skip non-letter characters
            print(f"{char}: {item['num']}")
    print("============= END ================")


if __name__ == "__main__":
    main()
