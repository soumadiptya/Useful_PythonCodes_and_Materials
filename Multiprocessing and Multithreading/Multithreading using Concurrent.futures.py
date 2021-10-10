# Lessons on multi threading using concurrent futures library with a real world example
# 1)  Multi threading is best used for I/O bound tasks such as downloading pictures when multiple threads can be used
# for multiple downloads. MUlti threading actually doesn't run tasks in parallel just gives an illusion of doing so.
# 2) Multi processing is best used for CPU bound tasks such as data manipulation where big numbers are being crunched


# Imports
import concurrent.futures
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Main
start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done sleeping...')


# do_something()
# do_something()
# Turn them into threads
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")


# Threading with concurrent.futures
# Create a context manager
def do_something2(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


with ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something2, 2)
    print(f1.result())

start = time.time()
with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something2, sec) for sec in secs]
    for f in as_completed(results):
        print(f.result())
finish = time.time()
print(f"Finished in {round(finish - start, 2)} seconds")

# With the map method
start = time.time()
with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something2,secs)
    for result in results:
        print(result)
finish = time.time()
print(f"Finished in {round(finish - start, 2)} seconds")
