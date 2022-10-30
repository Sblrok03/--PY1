def get_count_char(str_):
    graders_dict = {}
    DEFAULT_COUNT = 0
    str_ = ''.join(str_.lower().split())  # Можно было не использовать join и split. ( str_ = str_.lower() )
    for letter in str_:
        if letter.isalpha() == True:
            graders_dict[letter] = graders_dict.get(letter, DEFAULT_COUNT) + 1
    return graders_dict
    #print(graders_dict)

def percent_of_sum(varl_):
    second = {}
    for fruit, count in varl_.items():
        second[fruit] = round(count * 100 / sum(varl_.values()), 2)
    print(second)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

dict_ex = get_count_char(main_str)
print(dict_ex) # сколько некоторый элемент встречался в строке

percent_of_sum(dict_ex) # процентное отношение ко всем символам
