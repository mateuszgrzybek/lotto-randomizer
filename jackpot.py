from random import sample

class EuroJackpot():
    """Class that models an EuroJackpot lotto game"""

    @staticmethod
    def get_big_numbers():
        """Gets 5 random, non-repeating numbers out of 50."""
        big_numbers_list = sample(range(1, 51), 5)
        big_numbers_list.sort()
        return big_numbers_list

    @staticmethod
    def get_small_numbers():
        """Gets 2 random, non-repeating numbers out of 10."""
        small_numbers_list = sample(range(1, 11), 2)
        small_numbers_list.sort()
        return small_numbers_list


game = EuroJackpot()
print('5 out of 50:', (', ').join(str(x) for x in game.get_big_numbers()))
print('2 out of 10:', (', ').join(str(x) for x in game.get_small_numbers()))