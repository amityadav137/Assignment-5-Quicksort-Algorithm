def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

# Example usage
if __name__ == "__main__":
    test = [5, 3, 8, 4, 2, 7, 1, 10]
    print("Sorted:", quicksort(test))