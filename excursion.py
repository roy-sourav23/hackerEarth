# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/excursion-2d080f3a/

from math import ceil
def excursion(boys, girls, seats):
    rooms = lambda person, seats : ceil(person / seats)
    print(f"{rooms(boys, seats)+rooms(girls, seats)}")

t = int(input())
for x in range(t):
    arr = list(map(int, input().split()))
    excursion(arr[0], arr[1], arr[2])