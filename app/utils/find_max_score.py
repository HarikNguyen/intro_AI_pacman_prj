from app.constants import FOOD


def find_max_score(map):
    score = 0
    for row in map:
        for cell in row:
            if cell == FOOD:
                score += 1
    return score
