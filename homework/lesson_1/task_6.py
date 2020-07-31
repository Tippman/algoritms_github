"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class Task_Desk:
    def __init__(self):
        self.current_queue = QueueClass()  # базовая очередь задач
        self.unsolved_tasks = QueueClass()  # очередь нерешенных задач
        self.complited_tasks = []  # список решенных задач

    def to_current_queue(self, task):
        """Добавить задачу в общую очередь"""
        self.current_queue.to_queue(task)

    def complete_task(self):
        """Доавить задачу в список решенных"""
        self.complited_tasks.append(self.current_queue.from_queue())

    def for_revision(self):
        """Отправить задачу на доработку"""
        return self.unsolved_tasks.to_queue(self.current_queue.from_queue())

    def show_current_queue(self):
        """Показать текущую очередь"""
        return self.current_queue.elems

    def show_current_task(self):
        """показать текущую решаемую задачу"""
        return self.current_queue.elems[-1]

    def show_unsolved_tasks(self):
        return self.unsolved_tasks.elems

    def show_completed_tasks(self):
        """показать список решенных задач"""
        return self.complited_tasks


if __name__ == '__main__':
    td = Task_Desk()
    td.to_current_queue('task1')
    td.to_current_queue('task2')
    td.to_current_queue('task3')
    td.to_current_queue('task4')
    print(td.show_current_queue(), "показать всю очередь")
    print(td.show_current_task(), "показать текущую задачу")
    print("решаем текущую задачу")
    td.complete_task()
    print(td.show_completed_tasks(), "показать список решенных задач")
    print(td.show_current_task(), "показать текущую задачу")
    print("отправляем текущую задачу в очередь нерешенных")
    td.for_revision()
    print(td.show_unsolved_tasks(), "очередь нерешенных задач")
    print(td.show_completed_tasks(), "показать список решенных задач")
    print(td.show_current_queue(), "показать всю очередь")
