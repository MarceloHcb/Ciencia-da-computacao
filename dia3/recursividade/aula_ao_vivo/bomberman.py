import time

def bomb(number: int):
    if number == 0:
        print("boom")
        return
    print(number)
    time.sleep(1)
    next_number = number - 1
    bomb(next_number)

if __name__ == '__main__':
    bomb(5)
    