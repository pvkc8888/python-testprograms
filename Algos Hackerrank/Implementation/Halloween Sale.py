#!/bin/python3

import sys


def howManyGames(p, d, m, s):
    total_games = 0
    if p <= s:
        total_spent = p
        next_game = p - d
        total_games += 1
    else:
        return 0
    while total_spent < s and next_game <= s - total_spent:
        if next_game > m:
            total_spent += next_game
            # print(total_spent)
            total_games += 1
            next_game -= d
        else:
            number = (s - total_spent) // m
            total_spent += number * m
            total_games += number
            break

    return total_games


if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)
