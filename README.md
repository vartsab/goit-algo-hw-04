# goit-algo-hw-04

# Sorting Algorithms Performance Analysis

## Introduction
This project compares three sorting algorithms: Merge Sort, Insertion Sort, and Timsort. The analysis is based on their execution times on various datasets.

## Algorithms
- **Merge Sort**: A divide-and-conquer algorithm.
- **Insertion Sort**: A simple sorting algorithm with O(n^2) complexity.
- **Timsort**: A hybrid sorting algorithm used in Python's built-in `sorted` function.

## Results
The execution times for each algorithm were measured using the `timeit` module is in the table below (sec):

|Algorythm       |      100|     1,000|     10,000|     100,000|
|:---------------|--------:|---------:|----------:|-----------:|
|Merge Sort      | 0.001609|  0.033101|   0.382674|    5.518205|
|Insertion Sort  | 0.002409|  0.297242|  34.310235|4,302.906866|
|Timsort         | 0.000054|  0.001003|   0.015181|    0.370746|

Timsort consistently outperformed the other two algorithms. The difference in the performance is getting more and more notable as the sample size grows.

## Conclusion
The combination of merge sort and insertion sort in Timsort makes it highly efficient for most use cases. This is why built-in sorting functions are preferred over custom implementations.

## Optional Task
Implemented a function to merge k sorted lists into one sorted list.

## Repository
Link to the repository: [https://github.com/vartsab/goit-algo-hw-04.git](#)
