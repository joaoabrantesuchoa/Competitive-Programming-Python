'''
---COMPLEXIDADE---
O(logN)
'''
a = list(int,input().split())
target = int(input())

L = 0
R = len(a) - 1

def main():
    while L <= R:
        mid = L + (R-L)//2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            L = mid + 1
        else:
            R = mid - 1

    return -1




