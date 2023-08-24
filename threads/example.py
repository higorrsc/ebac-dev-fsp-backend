import threading


def new():
    for _ in range(6):
        print('Single Thread')


t1 = threading.Thread(target=new)
t1.start()
t1.join()
print('Success')
