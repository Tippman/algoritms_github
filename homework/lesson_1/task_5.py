"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:
    def __init__(self, stack_size):
        self.elems = [[]]
        self.stack_size = stack_size

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems[-1]) < self.stack_size:
            self.elems[-1].append(el)
        else:
            self.elems.append([el])

    def pop_out(self):
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems

    def get_stack_size(self):
        plates_count = 0
        for stack in self.elems:
            plates_count += len(stack)
        return plates_count

if __name__ == '__main__':
    SC_OBJ = StackClass(3)
    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)

    # получаем значения всех элементов во всех стопках
    print(SC_OBJ.get_val())

    # узнаем размер всех элементов
    print(SC_OBJ.get_stack_size())

    print(SC_OBJ.is_empty(), 'стек не пустой')  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # получаем значения всех элементов во всех стопках
    print(SC_OBJ.get_val())

    # убираем элемент с вершины  крайнего стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины крайнего стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.get_stack_size())