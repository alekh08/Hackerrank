#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int value;
    int index;
} Element;

// Comparator function for sorting
int compare(const void *a, const void *b) {
    return ((Element *)a)->value - ((Element *)b)->value;
}

// Function to count swaps for sorting the array
int countSwaps(int *arr, int n, int ascending) {
    Element *sorted_arr = malloc(n * sizeof(Element));
    int *visited = calloc(n, sizeof(int)); // Initialize all to 0 (false)

    // Populate sorted array with values and their original indices
    for (int i = 0; i < n; i++) {
        sorted_arr[i].value = arr[i];
        sorted_arr[i].index = i;
    }

    // Sort the array based on values (ascending or descending)
    qsort(sorted_arr, n, sizeof(Element), compare);
    if (!ascending) {
        for (int i = 0; i < n / 2; i++) {
            Element temp = sorted_arr[i];
            sorted_arr[i] = sorted_arr[n - 1 - i];
            sorted_arr[n - 1 - i] = temp;
        }
    }

    int swaps = 0;
    for (int i = 0; i < n; i++) {
        // If already visited or already in the correct position
        if (visited[i] || sorted_arr[i].index == i) {
            continue;
        }

        // Compute the cycle length
        int cycle_size = 0;
        int j = i;
        while (!visited[j]) {
            visited[j] = 1;
            j = sorted_arr[j].index;
            cycle_size++;
        }

        // Add (cycle_size - 1) to swaps (minimum swaps to resolve a cycle)
        if (cycle_size > 1) {
            swaps += (cycle_size - 1);
        }
    }

    // Free memory and return result
    free(sorted_arr);
    free(visited);
    return swaps;
}

// Main function for Lily's Homework
int lilysHomework(int n, int *arr) {
    // Calculate swaps for ascending and descending order
    int ascSwaps = countSwaps(arr, n, 1);
    int descSwaps = countSwaps(arr, n, 0);

    // Return the minimum of the two
    return ascSwaps < descSwaps ? ascSwaps : descSwaps;
}

int main() {
    int n;
    scanf("%d", &n);

    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int result = lilysHomework(n, arr);
    printf("%d\n", result);

    free(arr);
    return 0;
}
