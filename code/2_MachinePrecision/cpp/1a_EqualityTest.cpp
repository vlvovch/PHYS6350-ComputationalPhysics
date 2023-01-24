#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// Consider x computed as a sum x = 1.1 + 2.2
// The answer should be x = 3.3 but due to round-off error
// this is only true to a certain precision
// As a consequence, an equality test x == 3.3 may lead to some
// unexpected outcomes...

int main(int argc, char* argv[]) {
    double x = 1.1 + 2.2;

    cout.precision(18);
    cout << "x = " << x << endl;

    if (x == 3.3) {
        cout << "x == 3.3 is True" << endl;
    } else {
        cout << "x == 3.3 is False" << endl;
    }

    double eps = 1.e-12;
    if (abs(x - 3.3) < eps) {
        cout << "x == 3.3 to a precision of " << eps << " is True" << endl;
    } else {
        cout << "x == 3.3 to a precision of " << eps << " is False" << endl;
    }

    return 0;
}
