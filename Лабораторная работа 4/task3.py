def delete(list_, index=None):
    list_new = []
    if (index is not None) and (len(list_) > index >= 0):
        list_new = list_[:index] + list_[(index+1):]
        return list_new
    elif len(list_) == index or (index is None):
        list_new = list_[:(len(list_)-1)]
        return  list_new
    else:
        return 'Неверный индекс'

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
