import time
import random
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def generate_datasets(size):
    return {
        "random": [random.randint(0, 10000) for _ in range(size)],
        "sorted": list(range(size)),
        "reverse": list(range(size, 0, -1))
    }

def analyze(size):
    datasets = generate_datasets(size)
    print(f"\nAnalyzing input size: {size}")
    for dtype, data in datasets.items():
        d_data = data.copy()
        r_data = data.copy()

        start = time.time()
        quicksort(d_data)
        det_time = time.time() - start

        start = time.time()
        randomized_quicksort(r_data)
        rand_time = time.time() - start

        print(f"{dtype.title()} Input -> Deterministic: {det_time:.5f}s | Randomized: {rand_time:.5f}s")

if __name__ == "__main__":
    for size in [1000, 5000, 10000]:
        analyze(size)