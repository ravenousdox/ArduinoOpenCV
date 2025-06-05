import concurrent.futures
import time

t1 = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...\n')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
