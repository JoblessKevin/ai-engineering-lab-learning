import time

start = time.perf_counter()
result = 1 + 2
elapsed = time.perf_counter() - start

print(result)
print(f"{elapsed:.6f} seconds")