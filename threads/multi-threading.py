import time
import threading


def calc_square(numbers):
    print('Calculate square numbers: ')
    for i in numbers:
        time.sleep(2)
        print(f'square: {str(i * i)}')


def calc_cube(numbers):
    print('Calculate cube numbers: ')
    for i in numbers:
        time.sleep(2)
        print(f'cube: {str(i * i * i)}')


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    # creating two threads here t1 & t2
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))
    # starting threads here parallel by using start function
    t1.start()
    t2.start()
    # this join() will wait until the calc_square() function is finished
    t1.join()
    # this join() will wait until the calc_cube() function is finished
    t2.join()
    print('Main Thread Here!!')
    print('Successes!')
