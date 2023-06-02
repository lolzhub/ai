#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int n;
    std::cout << "Enter the size of the input: ";
    std::cin >> n;

    std::vector<int> arr(n);
    std::cout << "Enter the elements of the array:\n";
    for (int i = 0; i < n; i++) {
        std::cout << "Enter the " << (i+1) << " element: ";
        std::cin >> arr[i];
    }

    std::cout << "Unsorted array:\n";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }

    selectionSort(arr);

    std::cout << "\nSorted array:\n";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }

    return 0;
}
