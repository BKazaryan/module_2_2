first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))
if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)