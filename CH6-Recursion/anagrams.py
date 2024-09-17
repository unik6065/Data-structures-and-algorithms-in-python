def anagrams(word):
    if len(word) <= 1:
        return[word]
    result = []
    for part in anagrams(word[1:]):
        for i in range(len(part) + 1):
            result.append(part[:i] + word[0] + part[i:])
    return result
