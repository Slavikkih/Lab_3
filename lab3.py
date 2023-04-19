import random

# зчитування графа з файлу
with open('graph3.txt', 'r') as f:
    lines = f.readlines()
    graph = [[int(x) for x in line.strip().split()] for line in lines]

# випадково оберемо початковий шлях
path = [i for i in range(len(graph))]
random.shuffle(path)
best_path = path

# функція для розрахунку відстані між вершинами
def distance(path):
    d = 0
    for i in range(len(path)-1):
        d += graph[path[i]][path[i+1]]
    d += graph[path[-1]][path[0]]
    return d

# поступове покращення шляху
while True:
    improved = False
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            new_path = path.copy()
            new_path[i:j+1] = reversed(new_path[i:j+1])
            if distance(new_path) < distance(best_path):
                best_path = new_path
                improved = True
        if improved:
            break
    if not improved:
        break

print("Метод поступового покращення")
print("Найкращий шлях: ", best_path)
print("Відстань: ", distance(best_path))
