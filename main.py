from binary_search import binary_search
from bisect import bisect_left


def main():
    test_list = [i + 10 for i in range(1000)]
    find_number = 100
    total_index = binary_search(test_list, find_number)
    print('Найденный индекс:', total_index)

    print('Итоговый результат', test_list[total_index])


if __name__ == '__main__':
    main()
