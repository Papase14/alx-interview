#!/usr/bin/python3
"""
Prime game
"""

def isWinner(x, nums):
    def sieve_of_eratosthenes(limit):
        primes = []
        is_prime = [True] * (limit + 1)
        for num in range(2, int(limit**0.5) + 1):
            if is_prime[num]:
                primes.append(num)
                for multiple in range(num*num, limit + 1, num):
                    is_prime[multiple] = False
        for num in range(max(2, int(limit**0.5) + 1), limit + 1):
            if is_prime[num]:
                primes.append(num)
        return primes

    def get_winner(n):
        primes = sieve_of_eratosthenes(n)
        total_moves = n + 1  # Assuming all numbers are initially available
        maria_moves = 0
        ben_moves = 0

        for i in range(1, n + 1):
            num_moves = total_moves // len(primes)
            if i in primes:
                if num_moves % 2 == 1:
                    maria_moves += 1
                else:
                    ben_moves += 1

        if maria_moves > ben_moves:
            return 'Maria'
        elif maria_moves < ben_moves:
            return 'Ben'
        else:
            return None

    most_wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = get_winner(n)
        if winner:
            most_wins[winner] += 1

    if most_wins['Maria'] > most_wins['Ben']:
        return 'Maria'
    elif most_wins['Maria'] < most_wins['Ben']:
        return 'Ben'
    else:
        return None
