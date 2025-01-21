import random
def test_birthday_paradox(num_people):
    birthdays = [random.randrange(0,365) for _ in range(num_people)]
    birthday_set = set()
    for bday in birthdays:
        if bday in birthday_set: return True
        else: birthday_set.add(bday)
    return False


def paradox_stats(num_people = 23, num_trials = 100):
    num_successes = 0
    for _ in range(num_trials):
        if test_birthday_paradox(num_people): num_successes += 1
    return num_successes/num_trials


for x in range(101):
    print (f'For {x} people, the probability is approximately: {paradox_stats(x)}')
            