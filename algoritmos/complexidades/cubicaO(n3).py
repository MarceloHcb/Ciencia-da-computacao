def show_with_all(numbers_list):
    for x in numbers_list:  # O(n)
        for y in numbers_list:  # O(n)
            for z in numbers_list:  # O(n)
                print(x, y, z)

# O(n³)
if __name__ == "__main__":
    my_list = [2, 5, 8]
    show_with_all(my_list)
