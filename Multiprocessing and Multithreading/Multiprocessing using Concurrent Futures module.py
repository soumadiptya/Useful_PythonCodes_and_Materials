# Lessons on multi processing using multiprocessing library with a real world example
# 1)  Multi threading is best used for I/O bound tasks such as downloading pictures when multiple threads can be used
# for multiple downloads. MUlti threading actually doesn't run tasks in parallel just gives an illusion of doing so.
# 2) Multi processing is best used for CPU bound tasks such as data manipulation where big numbers are being crunched
# Imports
import concurrent.futures
import time


def do_something(seconds=2):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


if __name__ == "__main__":
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = range(8, 0, -1)
        # results = [executor.submit(do_something, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f"Finished in {finish - start} seconds")
