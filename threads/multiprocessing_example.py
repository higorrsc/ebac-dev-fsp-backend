import multiprocessing

# creating a Global Variable
results = []


def calc_square(numbers):
    global results
    for i in numbers:
        print(f'square: {str(i * i)}')
        results.append(i * i)
        print(f'within a result: {str(results)}')


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    # creating on Process here P1
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # starting Process here parallel by using start function
    p1.start()
    # this join() will wait until the calc_square() function is finished
    p1.join()
    # this print didn't work here we have to print in within the process
    print(f'result: {str(results)}')
    print('Success!')
