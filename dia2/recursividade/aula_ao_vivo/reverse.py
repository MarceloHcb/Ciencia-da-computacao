def invert_list_elements(numbers: list[int]) -> list[int]:    
    if len(numbers) <= 1:
        return numbers
    
    return [numbers[-1]] + invert_list_elements(numbers[:-1])

if __name__ == "__main__":
    my_numbers = [1,2,3,4,5] # saída: [5, 4, 3, 2, 1]
    print(invert_list_elements(my_numbers))