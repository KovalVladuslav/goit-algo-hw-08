import heapq

def minimize_connection_cost(cables):
    # Перетворюємо список довжин кабелів на мін-heap
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Повторюємо, поки не залишиться один кабель
    while len(cables) > 1:
        # Вилучаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на їх об'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на об'єднання кабелів:", minimize_connection_cost(cables))
