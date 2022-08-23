import random

# with open('doc.txt', 'a') as f:
#     print(f.read())
#     f.write("Hello world Python Programming")


with open('table.csv', 'w') as table:
    
    for i in range(1000):
        height = random.choice(range(150, 180))
        weight = random.choice(range(50, 100))
        table.write(f"키: {height}, 몸무게: {weight}")
