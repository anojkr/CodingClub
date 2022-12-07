# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import bisect

def findIndex(arr, target, pos="right"):
    flag = False
    if pos == "left":
        idx = bisect.bisect_left(arr, target)
        if arr[idx] == target:
            flag=True
        return flag, idx
    else:
        idx = bisect.bisect_right(arr, target)
        if arr[idx-1] == target:
            flag=True
        return flag, idx-1

def solve(rectangles, lines):

    for (start, end) in rectangles:
        x = findIndex(lines, start, "left")
        y = findIndex(lines, end)
        print(x,y)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rectangles  = [(2,5),(4,8)]
    lines = [1,3,4,6,7]
    solve(rectangles, lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
