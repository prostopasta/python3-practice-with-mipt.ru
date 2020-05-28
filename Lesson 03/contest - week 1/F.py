def recurs(n, array, listing, previous, n_plus1=True):
    k = len(array)
    if k == 2:
        check = array[1] - array[0]
        if check == 1 or check == 3:
            print("HORRA!")
            listing.append([array[0], array[1]])
            return 1
        else:
            print("OOOPS!")
            return 0

    if n in array:
        if (n + 1 in array) and (n % 3 != 0):
            listing.append([n, n+1])
            array.remove(n)
            array.remove(n + 1)
            print(n, n+1, array, 'n+1')
            return recurs(array[0], array, listing, n)
        elif (n + 3) in array:
            listing.append([n, n+3])
            array.remove(n)
            array.remove(n + 3)
            print(n, n+3, array, 'n+3')
            return recurs(array[0], array, listing, False)
        else:
            print(n, array, 'no')
            array.insert(0, previous)
            if n_plus1:
                array.insert(1, previous+1)
                listing.remove([previous, previous+1])
            else:
                array.insert(1, previous+3)
                listing.remove([previous, previous+3])
            return recurs(array[1], array, listing, n_plus1)
    else:
        print(n, array, '0')
        print("OOOPS!")
        return 0


num = int(input())      # size of chocolate = 3 x num, num % 2 == 0 !!!
result = 0
total_list = []

for i in range(3 * num - 1):
    arr = list(range(1, 3 * num + 1))
    lists = []
    print('-------------------NEW--------------------')
    result += recurs(i + 1, arr, lists, 1)
    print(result, lists, 'not sorted?')
    lists.sort(key=lambda x: [x[0], lists])
    print(result, lists, 'sorted!!!!!')

    if lists not in total_list:
        total_list.append(lists)

print(result, len(total_list), total_list)
