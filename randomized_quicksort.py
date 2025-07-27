import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    arr.remove(pivot)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]

    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    test = [5, 3, 8, 4, 2, 7, 1, 10]
    print("Sorted:", randomized_quicksort(test))