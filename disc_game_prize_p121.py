def denominator(discs):
    return reduce((lambda x, y: x * y), range(1, discs + 2))

def probabilities(discs, turns_done, color_is_blue):
    if turns_done == discs:
        reds = sum(map(lambda x: 1 if not x else 0, color_is_blue))
        blues = sum(map(lambda x: 1 if x else 0, color_is_blue))
        if blues <= reds:
            return 0
        probability = reduce((lambda x, (idx, color_blue): x * (1 if color_blue else idx + 1)), enumerate(color_is_blue), 1)
        return probability
    return (probabilities(discs, turns_done + 1, color_is_blue[:] + [True]) + 
        probabilities(discs, turns_done + 1, color_is_blue[:] + [False]))


def numerator(discs):
    return probabilities(discs, 0, [])

turns = 15 
print(denominator(turns)/numerator(turns))
