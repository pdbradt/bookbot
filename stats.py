def count_of_words(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        temp_String = f.read()
        splited_String = temp_String.split()
    return len(splited_String)

def unique_character_counts(content_of_book):
    to_lower_case = content_of_book.lower()
    counting_uniques = {}  # Initialize an empty dictionary
    for character in to_lower_case:
        if character in counting_uniques:
            counting_uniques[character] += 1
        else:
            counting_uniques[character] = 1
    return counting_uniques