from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции).
        Если первый элемент кортежа истина, то результат добавляется в список.

        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        :param func: Функция, применяемая к каждому элементу списка.
        :param input_array: Исходный список.
        :return: Отфильтрованный список.
        """
        if len(input_array) == 0:
            return []
        result = []
        for el in input_array:
            y = func(el)
            if y[0]:
                result.append(y[1])
        return result


"""
def is_not_null_even(x: int) -> tuple[bool, int]:
    if not x or x % 2:
        return False, 0
    return True, x


def square_positive(x: int) -> tuple[bool, int]:
    if x >= 0:
        return True, x * x
    return False, 0


class TestFilterMapExercise:
    @pytest.mark.skip
    def test_filter_map_empty(self) -> None:
        empty = FilterMapExercise.filter_map(is_not_null_even, [])
        assert empty == []

    @pytest.mark.skip
    def test_filter_map_is_not_null_even(self) -> None:
        filtered_list = FilterMapExercise.filter_map(is_not_null_even, [-1, 0, 1, 2, 4])
        assert filtered_list == [2, 4]

    @pytest.mark.skip
    def test_filter_map_square_positive(self) -> None:
        filtered_list = FilterMapExercise.filter_map(square_positive, [-1, 0, 1, 2, 4])
        assert filtered_list == [0, 1, 4, 16]
"""
