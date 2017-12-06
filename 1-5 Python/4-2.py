PASSPHRASE_FILENAME = "4.txt"

if __name__ == "__main__":

    valid = 0

    with open(PASSPHRASE_FILENAME) as f:
        for line in f:
            passdict = dict()
            isValid = True
            for word in line.split():
                sortedWord = ''.join(sorted(word))
                passdict.setdefault(sortedWord, 0)
                if passdict[sortedWord] == 1:
                    isValid = False
                    break
                passdict[sortedWord] = passdict[sortedWord] + 1
            if isValid:
                valid = valid + 1

    print valid
