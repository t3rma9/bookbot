def main():
    with open("//wsl.localhost/Ubuntu/root/bookbot/books/frankenstein.txt", "r") as myBook:

        file_contents = myBook.read();
    
    listOfWords = {}

    for x in file_contents:
        if x not in listOfWords:
            listOfWords[x] = 1
        else:
            listOfWords[x] += 1

    words = file_contents.split()
    
    print("--- Begin report of books/frankenstein.txt ---")

    print(f"Words found: {len(words)}")
    for x in listOfWords:
        print(f"The {x} character was found {listOfWords[x]} times" )

    print("--- End report ---")

if __name__ == "__main__":
    main()