def mymin_and_mymax(list):
    mymin = list[0]
    for i in list:
        if i < mymin:
            mymin = i
    print(f'minimum number in list:{mymin}')

    mymax = list[0]
    for j in list:
        if j > mymax:
            mymax = j
    print(f'maximum number in list {mymax}')

    # sorting the list
    for k in range(0, len(list)):
        for l in range((k + 1), len(list)):
            if list[k] > list[l]:
                list[k], list[l] = list[l], list[k]
    print(f'this is the sorted list: {list}')


mylist = [3, 65, 55, 3, 12]  # enter your list of numbers here
mymin_and_mymax(mylist)
