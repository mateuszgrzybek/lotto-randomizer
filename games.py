from random import sample

class EuroJackpot(Lottery):
    """Class that models an EuroJackpot lotto game."""

    @staticmethod
    def get_numbers():
        """Gets 5 random, non-repeating numbers out of 50 + gets 2 random,
        non-repeating numbers out of 10."""
        big_numbers_list = sample(range(1, 51), 5)
        big_numbers_list.sort()
        print('5 out of 50:', (', ').join(str(x) for x in big_numbers_list))
        small_numbers_list = sample(range(1, 11), 2)
        small_numbers_list.sort()
        print('2 out of 10:', (', ').join(str(x) for x in small_numbers_list))


class LottoClassic():
    """Class that models a classic Lotto game."""

    @staticmethod
    def get_numbers():
        """Gets 6 random, non-repeating numbers out of 49."""
        numbers_list = sample(range(1, 50), 6)
        numbers_list.sort()
        print('6 out of 49:', (', ').join(str(x) for x in numbers_list))


class MiniLotto():
    """Class that models a mini lotto game."""

    @staticmethod
    def get_numbers():
        """Gets 5 random, non-repeating numbers out of 42."""
        numbers_list = sample(range(1, 43), 5)
        numbers_list.sort()
        print('5 out of 42:', (', ').join(str(x) for x in numbers_list))