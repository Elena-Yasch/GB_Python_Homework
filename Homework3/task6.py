# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

word = input('Введите любое слово, состоящее из маленьких латинских букв - ')

def int_func(word:str):
    new_word = word.capitalize()
    return new_word

print(int_func(word))

your_string = input('Введите любую строку из слов, состоящих из маленьких латинских букв и разделенных пробелов - ')


def int_fun(your_string):
    new_str = your_string.title()
    return new_str


print(int_fun(your_string))