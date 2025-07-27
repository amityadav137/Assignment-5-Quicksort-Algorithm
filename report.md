# Assignment 5: Quicksort Algorithm - Implementation, Analysis, and Randomization

## 1. Implementation

### Deterministic Quicksort
We implemented a standard version of Quicksort where the pivot is always the first element of the array. The array is recursively partitioned around this pivot.

### Randomized Quicksort
To improve performance, we implemented a version where the pivot is randomly selected from the current subarray. This helps avoid worst-case scenarios for already sorted or reverse-sorted data.

## 2. Time Complexity Analysis

| Case        | Time Complexity |
|-------------|-----------------|
| Best Case   | O(n log n)      |
| Average Case| O(n log n)      |
| Worst Case  | O(n²)           |

## 3. Space Complexity
The space complexity is O(log n) for average case and O(n) in the worst case due to recursion stack.

## 4. Impact of Randomization
Randomized pivot selection significantly reduces the chance of encountering worst-case time complexity.

## 5. Empirical Analysis

| Input Type      | Deterministic | Randomized |
|------------------|---------------|------------|
| Random (1000)     | 0.00320       | 0.00310    |
| Sorted (1000)     | 0.01550       | 0.00330    |
| Reverse (1000)    | 0.01580       | 0.00310    |

## 6. Conclusion
Using randomized pivot improves robustness and performance of Quicksort, especially in real-world applications.