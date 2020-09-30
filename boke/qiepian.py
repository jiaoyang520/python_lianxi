def qp(list1, start, end, bc):
    while start < end:
        if bc < 0:
            print("语法错误！")
            break
        elif start > 0 and end > 0 or start < end < 0:
            print(list1[start])
        start = start + bc
    while start > end:
        if bc > 0:
            print("语法错误！")
            break
        elif start < 0 and end < 0 or start > end:
            print(list1[start])
        start = start + bc

    # while start < end:
    #     if bc < 0:
    #         print("语法错误！")
    #         break
    #     elif start > 0 and end > 0 or start < end < 0:
    #         print(list1[start])
    #     start = start + bc
    # while start > end:
    #     if bc > 0:
    #         print("语法错误！")
    #         break
    #     elif start < 0 and end < 0 or start > end:
    #         print(list1[start])
    #     start = start + bc
