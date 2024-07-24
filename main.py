from binary_search import binary_search


def main():
    test_list = [i for i in range(1000)]
    find_number = 500
    total_index = binary_search(test_list, find_number)
    print('Итоговый результат:', total_index)
