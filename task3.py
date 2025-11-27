def hanoi(n: int, source: str, target: str, auxiliary: str, state: dict[str, list[int]]) -> None:
    """
    Рекурсивна функція для розв'язання задачі Ханойської вежі.

    Args:
        n (int): Кількість дисків для переміщення.
        source (str): Назва початкового стрижня.
        target (str): Назва цільового стрижня.
        auxiliary (str): Назва допоміжного стрижня.
        state (dict): Поточний стан стрижнів.
    """
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        return

    # Перемістити n-1 дисків з source на auxiliary
    hanoi(n - 1, source, auxiliary, target, state)

    # Перемістити найбільший диск з source на target
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")

    # Перемістити n-1 дисків з auxiliary на target
    hanoi(n - 1, auxiliary, target, source, state)


def main() -> None:
    try:
        user_input = input("Введіть кількість дисків: ")
        n = int(user_input)
        if n < 0:
            print("Кількість дисків не може бути від'ємною.")
            return
        if n == 0:
            n = 3  # Демо-режим
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Початковий стан: диски розміщені на стрижні A у порядку зменшення (3, 2, 1)
    # Використовуємо список як стек: кінець списку - це верх стрижня.
    state = {"A": list(range(n, 0, -1)), "B": [], "C": []}

    print(f"Початковий стан: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    main()
