def plus_two(value):
    try:
        result = 2 + int(value)
        print(f"Результат: {result}")
    except ValueError:
        print(f"Ошибка: ожидается числовое значение, а получено '{value}'.")

# Пример вызова
plus_two("3")
plus_two("abc")
