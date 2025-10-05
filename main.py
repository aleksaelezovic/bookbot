import sys
from stats import count_words, get_character_count, count_to_sorted


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    content = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = count_words(content)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count = get_character_count(content)
    sorted = count_to_sorted(count)
    for dic in sorted:
        c = dic["char"]
        if not c.isalpha():
            continue
        n = dic["num"]
        print(f"{c}: {n}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
