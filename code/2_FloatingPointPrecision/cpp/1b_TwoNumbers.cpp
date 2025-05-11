#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// Program calculating the value of \delta^{-1} * (y - x)
// where x = 1 and y = 1. + \delta * \sqrt{2}
// The value should be equal to $\sqrt{2} = 1.41421356237...$
// but for small values of \delta the result can be inaccurate due to
// large round-off error
// Here we use \delta = 10^{-14} but feel free to try other values

int main(int argc, char* argv[]) {
    double delta = 1.e-14;
    double x = 1.;
    double y = 1. + delta * sqrt(2.);

    cout.precision(17);
    double val = (1./delta) * (y - x);
    cout << delta << " * (y-x) = " << val << endl;
    cout << "The accurate value is sqrt(2) = " << sqrt(2.) << endl;
    cout << "The difference is " << val - sqrt(2.) << endl;

    return 0;
}
