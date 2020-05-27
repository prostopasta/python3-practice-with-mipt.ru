"""
Контест 1 неделя: E - Результаты работы студентов в семестре

Есть результаты работы студентов в семестре. Студентов выводить в порядке суммы их баллов. Требуется вывести
отсортированные результаты работ для каждого студента.

Данные вводятся как: student_id value
student_id принимает значения от 0 до N. value от 1 до 10

Пример входных данных: 0 3 0 5 1 3 1 2

Тут представленны данные о двух студента: 0 и 1. Сумма балов студента 0 - 8. Студента 1 - 5. Значит, сначала должны
быть напечатаны результаты 0 студента, затем 1. Таким образом сначала надо вывести отсортированные результаты
студента 0, затем студента 1:
5 3 3 2

Напомним, что у list в питоне есть встроенный метод sort и есть функция sorted. У них есть параметр key, который
определяет по каким значениям будет сортироваться объект. Например код ниже будет сортировать лист по длине его
элементов. Так же есть параметр reverse:
a = ['###', '@', '??']

a.sort(key=lambda x: len(x))                    # ['@', '??', '###']

a.sort(key=lambda x: len(x), reverse=True)      # ['###', '??', '@']

Формат входных данных
В первой строке N - количество студентов. Далее идет какое-то количество строк (не равное N) с результатами студентов в
формате: student_id value. 0 <= student_id < N. Значения разделены пробелом. Ввод заканчивается #.

Формат выходных данных
Вывести отсортированные результаты студентов в одну строку. Сначала печатаются результаты лучшего по сумме баллов
студента, потом второго и так далее. Результаты в одну строку
"""
x = int(input())        # кол-во студентов
student_grades = [[]]

while True:
    s = input()
    if s == "#":
        break
    else:
        n, g = map(int, s.split())
        student_grades[n].append(g)
    student_grades.sort(key=lambda a: (a, int()))
#    student_grades.sort(key=lambda a: sum([a]))
#    student_grades.sort(key=lambda a: [a])

print(x, student_grades)