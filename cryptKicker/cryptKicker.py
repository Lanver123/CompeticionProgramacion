import sys

def isPromising(alphabet,used, encrypted, word):
    for i in range(len(word)):
        isEncrypted = alphabet.get(encrypted[i])
        isUsed = used.get(word[i])
        if isEncrypted is not None:
            if isEncrypted != word[i]:
                return None,None
        else:
            if isUsed is not None:
                if isUsed != encrypted[i]:
                    return None,None
            alphabet[encrypted[i]] = word[i]
            used[word[i]] = encrypted[i]
    return alphabet,used

def backtracking(line, sol, alphabet, decryption, used):
    if sol == len(line):
        return decryption
    else:
        encrypted = line[sol]
        posibleWords = words.get(len(encrypted))
        if posibleWords is not None:
            for word in posibleWords:
                newDict,newUsed = isPromising(alphabet.copy(),used.copy(), encrypted, word)
                if newDict is not None:
                    decryption[encrypted] = word
                    r = backtracking(line, sol + 1, newDict, decryption,newUsed)
                    if r is not None:
                        return r
    return None


def decrypt(line, words):
    return backtracking(line, 0, {}, {}, {})

if __name__ == '__main__':

    nWords = int(input())
    words = {}
    for i in range(nWords):
        word = input().strip()
        length = words.get(len(word),[])
        length.append(word)
        words[len(word)] = length
    
    while True:
        try:
            line = None
            line = input()
        except:
            pass
        if line is None: break
        line = line.strip()
        if len(line) == 0: break
        
        line = line.split()
        decryption = decrypt(line, words)
        res = ''
        if decryption is None:
            for i,l in enumerate(line):
                res += '*' * len(l)
                if i != len(line) - 1:
                    res += ' '
        else:
            for i, word in enumerate(line):
                res += decryption.get(word)
                if i != len(line) - 1:
                    res += ' '

        print(res)