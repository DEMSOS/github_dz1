def access_array_element(array, index):
    try:
        element = array[index]
        print(f"Элемент на индексе {index}: {element}")
    except IndexError:
        print(f"Ошибка: индекс {index} вне границ массива.")

# Пример использования
array = [1, 2, 3, 4, 5]
access_array_element(array, 2)
access_array_element(array, 10)
