import csv

def clean_word(word):
    # Remove punctuation and convert to lowercase
    return word.translate(str.maketrans('', '', string.punctuation)).lower()

def count_word_frequency(word_list):
    word_frequency = {}
    for word in word_list:
        cleaned_word = clean_word(word)
        if cleaned_word:
            word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1
    return word_frequency

def main():
    file_path = 'sometext.txt'  # Replace 'sometext.txt' with the actual file path

    try:
        with open(file_path, 'r') as file:
            text = file.read()

        words = text.split()
        word_frequency = count_word_frequency(words)

        print("Word Frequency:")
        print("------------------")
        for word, frequency in word_frequency.items():
            print(f"Word: {word.title()}")
            print(f"Frequency: {frequency}\n")

    except FileNotFoundError:
        print("File does not exist.")


if __name__ == "__main__":
    main()
