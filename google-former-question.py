def longestWord(array:list[str]):
    longestWord = ''
    for element in array:
        if len(element) > len(longestWord):
            longestWord = element
    return longestWord

def mapString(string:str):
    map = {}
    for i in range(len(string)):
        letter = string[i]
        if letter in map:
            map[letter].append(i)
        else:
            map[letter] = [i]
    return map

def findNextIndex(array:list[int],minIndex:int):
    for element in array:
        if element >= minIndex:
            return element+1
    return False

def isSubsequence(word:str,map:dict):
    minIndex = 0
    for letter in word:
        if letter in map:
            minIndex = findNextIndex(map[letter],minIndex)
            if minIndex == False:
                return False
        else:
            return False
    return True

def longestMatch(string:str,dictionary:list[str]):
    subsequences = []
    map = mapString(string)
    for element in dictionary:
        if isSubsequence(element,map):
            subsequences.append(element)
    return longestWord(subsequences)

stringSequence = 'abppplee'
dictionary = ["able", "ale", "apple", "bale", "kangaroo"]

print(stringSequence)
print(dictionary)
print(longestMatch(stringSequence,dictionary))
