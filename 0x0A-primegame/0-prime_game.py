#!/usr/bin/python3
""" Module of Prime Game Solution """


def isWinner(x, nums):
    """Function that solves the Prime Game"""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(start):
        """Function that returns the next prime"""
        num = start + 1
        while not is_prime(num):
            num += 1
        return num

    def determine_game_winner(n):
        """Function that determins the gime winner"""
        if n == 1:
            return "Ben"  # Ben wins when n is 1
        prime = 2
        maria_turn = True
        while prime <= n:
            if n % prime != 0:
                return "Maria" if maria_turn else "Ben"
            prime = get_next_prime(prime)
            maria_turn = not maria_turn
        return "Maria" if maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
