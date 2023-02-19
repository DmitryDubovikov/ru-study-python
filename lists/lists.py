class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return []
        max_val = input_list[0]
        for el in input_list:
            if el > max_val:
                max_val = el
        return [max_val if el > 0 else el for el in input_list]

    @staticmethod
    def search(input_list: list[int], query: int, left: int = 0, right: int = -1) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if not input_list:
            return -1
        if len(input_list) == 1:
            return 0 if input_list[0] == query else -1
        if right == -1:
            right = len(input_list)

        while left <= right:

            m = (left + right) // 2

            if input_list[m] > query:
                return ListExercise.search(input_list, query, left, m - 1)
            elif input_list[m] < query:
                return ListExercise.search(input_list, query, m + 1, right)
            else:
                return m
        return -1
