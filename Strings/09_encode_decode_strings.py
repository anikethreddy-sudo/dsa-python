def encode(strs):
    result = ""

    for word in strs:
        result += str(len(word)) + "#" + word

    return result


def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        word = s[j + 1:j + 1 + length]
        result.append(word)

        i = j + 1 + length

    return result


words = ["apple", "cat", "hello"]
encoded = encode(words)

print(encoded)
print(decode(encoded))
