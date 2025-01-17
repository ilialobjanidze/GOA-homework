def remove_exclamation_marks(s):
    return s.replace("!","")


def get_volume_of_cuboid(length, width, height):
    return length * width * height

def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "rock" and player2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

def is_divisible(n,x,y):

    return n % x == 0 and n % y == 0


def count_by(x, n):
    return [x * i for i in range(1, n + 1)]