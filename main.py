
def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
        # print to console 
        print(file_contents)

        print(f"\n--- Beginning report of {path_to_file} ---")
        #get word count
        count_words = word_count(file_contents)
        print(f"{count_words} words were found in the document.\n")

        #get frequency of chars
        count_char = letter_count(file_contents)
        
        for char, count in sorted(count_char.items()):
            print(f"The '{char}' character was found {count} times.")
        print("--- End of Report ---")
        
    except FileNotFoundError:
        print(f"Error: '{path_to_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def word_count(text):
    #takes the string and returns the number of words in it.

    words = text.split()
    return len(words)

def letter_count(text):
    
    #this will make them all lowercase
    text = text.lower()
    
    #dictionary for it to go to
    char_freq = {}
    
    for char in text:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

    return char_freq
main()