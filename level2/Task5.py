# File Manipulation
import string
def count_word_occurrences(file_path):
    word_count = {}
    
    # Open the file and read its content
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into words
            words = line.split()
            for word in words:
                # Remove punctuation marks and convert to lowercase
                
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                # Count occurrences of each word
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
    
    # Sort the dictionary by keys (words) in alphabetical order
    sorted_word_count = sorted(word_count.items())
    
    # Display the results
    for word, count in sorted_word_count:
        print(f"{word}: {count}")


def main():
    file_path = input("Enter the path of the text file: ")
    try:
        count_word_occurrences(file_path)
    except FileNotFoundError:
        print("File not found. Please make sure the file path is correct.")


if __name__ == "__main__":
    main()
