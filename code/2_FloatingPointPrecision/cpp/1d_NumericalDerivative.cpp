#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// Let us calculate the derivative of a function f(x) = x*(x-1)
// numerically with finite differences
// and analyze the accuracy of the method
// as a function of the step size h
// For very small h the calculation may
// become inaccurate due to round-off error

double f(double x) {
  return x*(x-1.);
}

double df_exact(double x) {
  return 2.*x - 1.;
}
  
double df_numerical(double x, double h) {
  return (f(x+h) - f(x)) / h;
} 


int main(int argc, char* argv[]) {
    // Prepare the output
    cout << setw(15) << "h" << " ";
    cout << setw(15) << "df(1)" << " ";
    cout << setw(15) << "rel. error" << " ";
    cout << endl;
    //cout << scientific;

    double x0 = 1.0;
    double h = 1.0;
    // Loop over values of h
    for(int i = 0; i <= 16; ++i) {
      double df_val = df_numerical(x0, h);
      double df_err = abs(df_val - df_exact(x0)) / df_exact(x0);

      // Output
      cout << setw(15) << h << " ";
      cout << setw(15) << df_val << " ";
      cout << setw(15) << df_err << " ";
      cout << endl;

      // Decrease the step size by factor 10
      h /= 10.;
    }

    return 0;
}
