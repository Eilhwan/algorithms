from collections import deque
def solution(cacheSize, cities):
    running_time = 0
    q = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.upper()
        if city in q:
            running_time += 1
            q.remove(city)
            q.append(city)
        else:
            running_time += 5
            q.append(city)
    return running_time


cities = ["Jeju", "Pangyo", "JEJU", "Seoul", "NewYork", "LA", "JEJU"]
solution(3, cities)