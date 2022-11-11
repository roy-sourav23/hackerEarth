#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/special-number-9-a0cda359/


def special_no(num):
    digits = list(map(int, list(str(num))))
    sum_of_digits = sum(digits)
    if sum_of_digits % 4 == 0:
        print(f"{num}")
    else:
        num += 1
        special_no(num)

n = int(input())
for x in range(n):
    num = int(input())
    special_no(num)