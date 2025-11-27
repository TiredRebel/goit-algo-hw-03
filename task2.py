import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Малює криву Коха.

    Args:
        t (turtle.Turtle): Об'єкт turtle для малювання.
        order (int): Рівень рекурсії.
        size (float): Довжина сегмента.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    """
    Налаштовує середовище turtle та малює сніжинку Коха.

    Args:
        order (int): Рівень рекурсії.
        size (float): Розмір сніжинки.
    """
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")
    
    # Вимикаємо анімацію для швидкого малювання та уникнення зависання
    window.tracer(0)

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Оновлюємо екран після завершення малювання
    window.update()
    window.mainloop()


def main() -> None:
    try:
        user_input = input("Введіть рівень рекурсії (ціле число, наприклад, 3): ")
        order = int(user_input)
        if order < 0:
            print("Рівень рекурсії має бути невід'ємним числом.")
            return
        print(f"Малюємо сніжинку Коха з рівнем {order}...")
        draw_koch_snowflake(order)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    main()
