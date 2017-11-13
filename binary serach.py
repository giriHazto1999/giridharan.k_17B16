def binary_search(my1, token):
    found = False

    left = 0
    right = len(my1)-1

    while left <= right and not found:
        mid = (right+left)//2
        if my1[mid] == token:
            found = True

        if my1[mid] > token:
            right = mid - 1
        else:
            left = mid + 1
    return found

found = [45]
print(binary_search(found))
