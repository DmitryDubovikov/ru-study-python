from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def movie_is_suitable(movie: dict) -> bool:
            return (
                movie.get("rating_kinopoisk", 0) != 0
                and movie.get("rating_kinopoisk", 0) != ""
                and movie.get("rating_kinopoisk", 0) != "0"
                and len(movie.get("country", "").split(sep=",")) > 1
            )

        ratings = list(
            map(lambda x: float(x["rating_kinopoisk"]), filter(movie_is_suitable, list_of_movies))
        )
        return sum(ratings) / len(ratings)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def movie_is_suitable(movie: dict) -> bool:
            rating_kinopoisk = movie.get("rating_kinopoisk", 0)
            if rating_kinopoisk:
                return float(rating_kinopoisk) >= rating
            return False

        filtered_and_mapped = list(
            map(lambda x: x["name"].count("и"), filter(movie_is_suitable, list_of_movies))
        )
        return sum(filtered_and_mapped)
