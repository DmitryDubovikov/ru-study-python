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
        max_val = max(input_list)
        return [max_val if el > 0 else el for el in input_list]

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
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
        left, right = 0, len(input_list)
        while left < right:
            m = (left + right) // 2
            if input_list[m] == query:
                return m
            elif input_list[m] < query:
                left = m + 1
            else:
                right = m
        return -1
