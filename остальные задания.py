import heapq
import random
from collections import deque


# ---------- Задание 5: выбор заявок ----------
def max_events(events):
    events = sorted(events, key=lambda p: p[1])  # по времени окончания
    chosen, end = [], -1
    for s, f in events:
        if s >= end:
            chosen.append((s, f))
            end = f
    return chosen


def shortest_first(events):
    # другое жадное правило: брать самое короткое мероприятие
    chosen = []
    for s, f in sorted(events, key=lambda p: p[1] - p[0]):
        if all(f <= cs or s >= cf for cs, cf in chosen):
            chosen.append((s, f))
    return chosen


def task5():
    print("=== Задание 5 ===")
    ev = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
          (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    res = max_events(ev)
    print("По времени окончания:", res, "->", len(res), "шт.")
    bad = [(0, 5), (4, 6), (5, 10)]
    print("Контрпример для правила 'самое короткое':", bad)
    print("  короткое первым:", shortest_first(bad), "->", len(shortest_first(bad)), "шт.")
    print("  по окончанию:   ", max_events(bad), "->", len(max_events(bad)), "шт.")


# ---------- Задание 6: лесенка ----------
def stairs(n):
    a, b = 1, 1  # способов для 0 и 1 ступеньки
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def task6():
    print("\n=== Задание 6 ===")
    print("n -> способов:", [(n, stairs(n)) for n in range(1, 11)])
    print("Это числа Фибоначчи: ways(n) = ways(n-1) + ways(n-2)")


# ---------- Задание 7: жадность против динамики ----------
def greedy_coins(coins, s):
    cnt = 0
    for c in sorted(coins, reverse=True):
        cnt += s // c
        s %= c
    return cnt


def dp_coins(coins, S):
    INF = 10 ** 9
    dp = [0] + [INF] * S
    for x in range(1, S + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp


def task7():
    print("\n=== Задание 7 ===")
    coins = [1, 3, 4]
    dp = dp_coins(coins, 20)
    print("dp[0..10] =", dp[:11])
    print("Для 10: динамика", dp[10], ", жадность", greedy_coins(coins, 10))
    wrong = [(x, greedy_coins(coins, x), dp[x]) for x in range(1, 21)
             if greedy_coins(coins, x) != dp[x]]
    print("Суммы, где жадность ошибается (сумма, жадность, оптимум):", wrong)


# ---------- Задание 8: Евклид вручную (проверка кодом) ----------
def task8():
    print("\n=== Задание 8 ===")
    a, b, steps = 252, 198, 0
    while b:
        print(f"{a} = {a // b} * {b} + {a % b}")
        a, b = b, a % b
        steps += 1
    print(f"НОД = {a}, делений: {steps}")


# ---------- Задание 9: быстрая степень ----------
def power_mod(a, n, m):
    result = 1
    a %= m
    while n > 0:
        if n & 1:
            result = result * a % m
        a = a * a % m
        n >>= 1
    return result


def task9():
    print("\n=== Задание 9 ===")
    for a, n, m in [(2, 10, 1000), (3, 13, 1000)]:
        print(f"{a}^{n} mod {m}: power_mod = {power_mod(a, n, m)}, pow = {pow(a, n, m)}")


# ---------- Задание 10: решето Эратосфена ----------
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        i += 1
    return [i for i in range(2, n + 1) if is_prime[i]]


def task10():
    print("\n=== Задание 10 ===")
    for n in (100, 1000, 10 ** 6):
        print(f"простых чисел не больше {n}: {len(sieve(n))}")


# ---------- Задание 11: Дейкстра ----------
def dijkstra(graph, start):
    d = {v: float('inf') for v in graph}
    d[start] = 0
    heap = [(0, start)]
    while heap:
        du, u = heapq.heappop(heap)
        if du > d[u]:
            continue
        for v, w in graph[u]:
            if du + w < d[v]:
                d[v] = du + w
                heapq.heappush(heap, (d[v], v))
    return d


def task11():
    print("\n=== Задание 11 ===")
    g = {'A': [('B', 4), ('C', 1)],
         'B': [('A', 4), ('C', 2), ('D', 1)],
         'C': [('A', 1), ('B', 2), ('D', 5)],
         'D': [('B', 1), ('C', 5)]}
    print("Исходный граф:", dijkstra(g, 'A'))
    g['A'].append(('D', 3))
    g['D'].append(('A', 3))
    print("С ребром A-D (3):", dijkstra(g, 'A'))


# ---------- Задание 12: Монте-Карло ----------
def monte_carlo_pi(N):
    inside = 0
    for _ in range(N):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / N


def task12():
    print("\n=== Задание 12 ===")
    random.seed(1)
    print("N        оценка pi")
    for N in (100, 10 ** 4, 10 ** 6):
        print(f"{N:<8} {monte_carlo_pi(N)}")


if __name__ == "__main__":
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
    task11()
    task12()
