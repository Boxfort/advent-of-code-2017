PASSPHRASE_FILENAME = "4.txt"

if __name__ == "__main__":

    valid = 0

    with open(PASSPHRASE_FILENAME) as f:
        for line in f:
            passdict = dict()
            isValid = True
            for word in line.split():
                passdict.setdefault(word, 0)
                if passdict[word] == 1:
                    isValid = False
                    break
                passdict[word] = passdict[word] + 1
            if isValid:
                valid = valid + 1

    print valid
