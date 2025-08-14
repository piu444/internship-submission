def word_count(text):
    
    try :
        with open(text, 'r') as file:
            text = file.read()
            words = text.split()
            count = len(words)
            print(f"Total number of words: {count}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
text = input("Enter the path to the text file: ")
word_count(text)
        
