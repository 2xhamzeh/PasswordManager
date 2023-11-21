def cipher(text, key):
    # takes a text and a key (strings), uses the key to cipher the text with the Vigenère cipher
    textArr = list(text)
    codeArr = list(key)
    codeArrLong = []

    i = 0
    while len(textArr) > len(codeArrLong):
        codeArrLong.append(codeArr[i])
        i += 1
        if (i > len(codeArr) - 1):
            i = 0

    cipheredText = ""
    for j in range(len(textArr)):
        newCharValue = ord(textArr[j]) + ord(codeArrLong[j])
        if (newCharValue) > 1114111:
            newCharValue -= 1114111
        cipheredText += chr(newCharValue)

    return cipheredText


def decipher(text, key):
    # takes a text and a key (strings), uses the key to decipher the text with the Vigenère cipher
    textArr = list(text)
    codeArr = list(key)
    codeArrLong = []

    i = 0
    while len(textArr) > len(codeArrLong):
        codeArrLong.append(codeArr[i])
        i += 1
        if (i > len(codeArr) - 1):
            i = 0

    decipheredText = ""
    for j in range(len(textArr)):
        newCharValue = ord(textArr[j]) - ord(codeArrLong[j])
        if (newCharValue) < 0:
            newCharValue += 1114111
        decipheredText += chr(newCharValue)

    return decipheredText
