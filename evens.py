def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        return True
    else:
        raise TypeError("A list was not pased into the function")


if __name__ == '__main__':
    print(even_number_of_evens(5))
