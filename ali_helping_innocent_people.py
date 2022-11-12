# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

tag = input()

def validity(t):
    v = ["A", "E", "I", "O", "U", "Y"]
    odd = lambda n, m: (n+m) % 2 != 0
    if t[2] in v:
        return "invalid"
    elif odd(int(t[0]), int(t[1])):
        return "invalid"
    elif odd(int(t[3]), int(t[4])):
        return "invalid"
    elif odd(int(t[4]), int(t[5])):
        return "invalid"
    elif odd(int(t[4]), int(t[5])):
        return "invalid"
    elif odd(int(t[-1]), int(t[-2])):
        return "invalid"
    else:
        return "valid"


print(validity(tag))