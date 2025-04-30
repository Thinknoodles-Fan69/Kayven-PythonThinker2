with open("FiveLetterWords.csv", "r") as fileobj:

        contents = fileobj.read()

        print(contents)

        wordlist = contents.split("<")

