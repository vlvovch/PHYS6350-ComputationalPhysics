// To compile
// On Unix: g++ -fopenmp rectanglerule_multi_openmp.cpp -o rectanglerule_multi_openmp
// On Mac:  clang++ -Xpreprocessor -std=c++11 -Xclang -fopenmp -L/opt/homebrew/opt/libomp/lib -I/opt/homebrew/opt/libomp/include -lomp rectanglerule_multi_openmp.cpp -o rectanglerule_multi_openmp

#include <iostream>
#include <cmath>
#include <omp.h>

using namespace std;

double a = 0., b = M_PI / 2.;
int Ndim = 3;

double f(double x1, double x2, double x3) {
    double xsum = x1 + x2 + x3;
    return sin(xsum);
}

double rectangle_rule_multi(double a, double b, int N) {
    double h = (b - a) / N;
    double sum = 0.;

    #pragma omp parallel for reduction(+:sum) collapse(3)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                double x1 = a + i * h + h / 2.;
                double x2 = a + j * h + h / 2.;
                double x3 = a + k * h + h / 2.;
                sum += f(x1, x2, x3);
            }
        }
    }

    return pow(h, Ndim) * sum;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <integration_points> <num_threads>" << std::endl;
        return 1;
    }

    // Parse command-line arguments for matrix size and number of threads
    int integration_points = std::stoi(argv[1]);
    int num_threads = std::stoi(argv[2]);

    // Set the number of threads to use for the parallel region
    omp_set_num_threads(num_threads);

    // Start measuring the wall time
    auto start_time = std::chrono::high_resolution_clock::now();

    // Compute the integral using the trapezoidal rule
    double result = rectangle_rule_multi(a, b, integration_points);

        // Stop measuring the wall time
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    //std::cout << std::scientific;
    std::cout.precision(16);
    cout << "Integral: " << result << endl;

    // Print the elapsed time
    std::cout << "Numerical integration took  " << elapsed_time << " milliseconds." << std::endl;


    return 0;
}
