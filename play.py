from sys import exit
from games import EuroJackpot, LottoClassic, MiniLotto

print("""Which game would you like to get numbers for?
      1. Lotto
      2. Mini Lotto
      3. EuroJackpot
      Please type the corresponding number (1/2/3).""")
choice = input(">>> ")

while True:
    if choice == str(1):
        game = LottoClassic()
        game.get_numbers()
        exit()
    elif choice == str(2):
        game = MiniLotto()
        game.get_numbers()
        exit()
    elif choice == str(3):
        game = EuroJackpot()
        game.get_numbers()
        exit()
    else:
        print("Try again.")
        choice = input(">>> ")
