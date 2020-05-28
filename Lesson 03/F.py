def recurs(array, tmplst):
    k = len(array)
    print(k, array)
    if k == 0:
        lst = sorted(tmplst, key=lambda x: [x[0], tmplst])
        print(lst)
        return lst

    for n in range(int(k / 2)):
        number = array[n]
        print(number, array)
        array.remove(number)
        if (number + 1) in array:
            array.remove(number + 1)
            recurs(array, tmplst.append([number, number + 1]))
        elif (number + 3) in array:
            array.remove(number + 3)
            recurs(array, tmplst.append([number, number + 3]))
        else:
            array.append(number)
            continue


listOfIndexes = list()
num = int(input())      # size of chocolate = 3 x num, num % 2 == 0 !!!

array1 = list(range(3, 3 * num + 1))
print(array1)

resultlist1 = [1, 2].append(recurs(array1, []))
print(resultlist1)
if resultlist1 not in listOfIndexes:
    listOfIndexes.append(resultlist1)

array2 = list(range(2, 4)) + list(range(5, 3 * num + 1))
print(array2)

resultlist2 = [1, 4].append(recurs(array2, []))
print(resultlist2)
if resultlist2 not in listOfIndexes:
    listOfIndexes.append(resultlist2)

print(len(listOfIndexes) - 1, listOfIndexes)
