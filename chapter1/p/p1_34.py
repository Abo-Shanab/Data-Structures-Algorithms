import random
count = 0
for i in range(100):
    s= list("I will never spam my friends again")
    flag = random.choice([True, False])
    if flag and count < 8:
        count += 1
        s.insert(random.randrange(0, 34),chr(random.randrange(65, 91)))
        print(f'{"".join(s)}   <-------typo')
    else:
        print("".join(s))