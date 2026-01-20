// To compile
// On Unix: g++ -fopenmp matrix_mult_openmp.cpp -o matrix_mult_openmp
// On Mac:  clang++ -Xpreprocessor -std=c++11 -Xclang -fopenmp -L/opt/homebrew/opt/libomp/lib -I/opt/homebrew/opt/libomp/include -lomp matrix_mult_openmp.cpp -o matrix_mult_openmp

#include <iostream>
#include <omp.h>
#include <vector>
#include <chrono>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <matrix_size> <num_threads>" << std::endl;
        return 1;
    }

    // Parse command-line arguments for matrix size and number of threads
    int matrix_size = std::stoi(argv[1]);
    int num_threads = std::stoi(argv[2]);

    // Initialize matrices A and B with sample data
    std::vector<std::vector<int>> A(matrix_size, std::vector<int>(matrix_size));
    std::vector<std::vector<int>> B(matrix_size, std::vector<int>(matrix_size));

    for (int i = 0; i < matrix_size; i++) {
        for (int j = 0; j < matrix_size; j++) {
            A[i][j] = static_cast<int>(i + j);
            B[i][j] = static_cast<int>(i - j);
        }
    }

    // Initialize matrix C to store the result
    std::vector<std::vector<int>> C(matrix_size, std::vector<int>(matrix_size, 0));

    // Set the number of threads to use for the parallel region
    omp_set_num_threads(num_threads);

    // Start measuring the wall time
    auto start_time = std::chrono::high_resolution_clock::now();

    // Perform matrix multiplication using OpenMP
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < matrix_size; i++) {
        for (int j = 0; j < matrix_size; j++) {
            for (int k = 0; k < matrix_size; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Stop measuring the wall time
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    //std::cout << "Matrix multiplication result: " << C[matrix_size/2][matrix_size/2] << std::endl;

    // Print the elapsed time
    std::cout << "Matrix multiplication took " << elapsed_time << " milliseconds." << std::endl;

    return 0;
}
