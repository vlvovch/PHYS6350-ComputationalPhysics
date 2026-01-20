// To compile
// On Unix: g++ -fopenmp parallel_sum_openmp.cpp -o parallel_sum_openmp
// On Mac:  clang++ -Xpreprocessor -std=c++11 -Xclang -fopenmp -L/opt/homebrew/opt/libomp/lib -I/opt/homebrew/opt/libomp/include -lomp parallel_sum_openmp.cpp -o parallel_sum_openmp


#include <iostream>
#include <omp.h>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <repetitions_size> <num_threads>" << std::endl;
        return 1;
    }

    // Parse command-line arguments for array size and number of threads
    int repetitions_size = std::stoi(argv[1]);
    int num_threads = std::stoi(argv[2]);

    const long long N = 10000000;

    // Initialize the array with sample data
    std::vector<long long> arr(N, 5);

    // Declare a variable to store the sum
    long long sum = 0;

    // Set the number of threads to use for the parallel region
    omp_set_num_threads(num_threads);

    for (int i = 0; i < repetitions_size; ++i) {
        // Compute the sum in parallel using OpenMP
        #pragma omp parallel for reduction(+:sum)
        for (int i = 0; i < arr.size(); i++) {
            sum += arr[i];
        }
    }
    // Print the result
    std::cout << "Sum of the array " << repetitions_size << " times: " << sum << std::endl;

    return 0;
}
