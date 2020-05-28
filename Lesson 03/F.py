def recurs(n, array, previous, n_plus1=True):
    k = len(array)
    if k == 2:
        check = array[1] - array[0]
        if check == 1 or check == 3:
            print("HORRA!")
            return 1
        else:
            print("OOOPS!")
            return 0

    if n in array:
        if (n + 1 in array) and (n % 3 != 0):
            array.remove(n)
            array.remove(n + 1)
            print(n, n+1, array, 'n+1')
            return recurs(array[0], array, n)
        elif (n + 3) in array:
            array.remove(n)
            array.remove(n + 3)
            print(n, n+3, array, 'n+3')
            return recurs(array[0], array, False)
        else:
            print(n, array, 'no')
            array.insert(0, previous)
            if n_plus1:
                array.insert(1, previous+1)
            else:
                array.insert(1, previous+3)
            return recurs(array[1], array, n_plus1)
    else:
        print(n, array, '0')
        print("OOOPS!")
        return 0


num = int(input())      # size of chocolate = 3 x num, num % 2 == 0 !!!
result = 0


for i in range(3 * num - 1):
    arr = list(range(1, 3 * num + 1))
    result += recurs(i + 1, arr, 1)

print(result)
