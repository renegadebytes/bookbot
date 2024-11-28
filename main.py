
def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
        # print to console 
        print(file_contents)

        count_words = word_count(file_contents)
        print(f"The book contains {count_words} words.")

    except FileNotFoundError:
        print(f"Error: '{path_to_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def word_count(text):
    #takes the string and returns the number of words in it.

    words = text.split()
    return len(words)

main()