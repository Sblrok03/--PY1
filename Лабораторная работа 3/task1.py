src = not False and True or False and not True

#scr = (True and True) or (False and False) # В первую очередь избавляемся от отрицаний
#scr = True or False # Избавляемся от логического "И"
#scr = True # Избавляемся от логического "ИЛИ"
result = True

print(src == result)
