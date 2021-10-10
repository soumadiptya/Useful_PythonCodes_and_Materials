# Lessons on multi processing using multiprocessing library with a real world example
# 1)  Multi threading is best used for I/O bound tasks such as downloading pictures when multiple threads can be used
# for multiple downloads. MUlti threading actually doesn't run tasks in parallel just gives an illusion of doing so.
# 2) Multi processing is best used for CPU bound tasks such as data manipulation where big numbers are being crunched
# Imports
import time
import multiprocessing
import sys


def do_something(seconds=2):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done sleeping...')


if __name__ == "__main__":
    print(sys.path)
    start = time.perf_counter()
    # p1 = multiprocessing.Process(target=do_something, args=[1])
    # p2 = multiprocessing.Process(target=do_something, args=[2])
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    process_list = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[2])
        p.start()
        # We can't do a join inside the loop because it would be same as doing it synchronously
        process_list.append(p)
    print(type(process_list[0]))
    for process in process_list:
        process.join()

    finish=time.perf_counter()
    print(f"Finished in {finish-start} seconds")
