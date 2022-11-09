# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

def zoo(word):
    return "Yes" if word.count("z") * 2 == word.count("o") else "No"

word = input()
print(zoo(word))