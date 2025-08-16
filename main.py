from stats import count_of_words, unique_character_counts
from sys import argv

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)
    file_path = argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    to_console = count_of_words(file_path)
    print("----------- Word Count ----------")
    print(f"Found {to_console} total words")
    print("--------- Character Count -------")
    with open(f"{file_path}", encoding="utf-8") as f:
        book_content = f.read()
    unique_character_directonary = unique_character_counts(book_content)
    unique_character_directonary = dict(sorted(unique_character_directonary.items(), key=lambda item: item[1], reverse=True))
    for character, count in unique_character_directonary.items():
        print(f"{character}: {count}")


if __name__ == "__main__":
    main()