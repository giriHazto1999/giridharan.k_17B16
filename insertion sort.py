def insertsort(L):

  for index in range(1, len(L)):
    key = L[index]
    j = index - 1

    while j >= 0 and (L[j] > key):
      L[j + 1] = L[j]
      j = j - 1
      L[j + 1] = key
  return L

L = [14, 24, 25, 26, 21]
print(insertsort(L))


