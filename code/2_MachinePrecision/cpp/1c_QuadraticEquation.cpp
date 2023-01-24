#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

// One of the roots of the quadratic equation ax^2+bx+c = 0
// reads x1,2 = (-b +- \sqrt{b^2-4ac}/(2a))
// If b>0 and |ac|<<b^2, the evaluation of this expression 
// involves subtraction of two very similar large numbers
// with bad consequences for the round-off error
// Alternative expression for x1 is
// x1,2 = 2c/(-b -+ \sqrt{b^2-4ac}) which does not involve the subtraction of large numbers

double x1direct(double a, double b, double c) {
  return (-b + sqrt(b*b - 4.*a*c))/(2.*a);
}
double x2direct(double a, double b, double c) {
  return (-b - sqrt(b*b - 4.*a*c))/(2.*a);
}

double x1alternative(double a, double b, double c) {
  return 2.*c / (-b - sqrt(b*b - 4.*a*c));
}

double x2alternative(double a, double b, double c) {
  return 2.*c / (-b + sqrt(b*b - 4.*a*c));
}


int main(int argc, char* argv[]) {
    double a, b, c;
    cout << "Enter a: ";
    cin >> a;
    cout << "Enter b: ";
    cin >> b;
    cout << "Enter c: ";
    cin >> c;

    // First check the roots are real
    if (b*b < 4. * a * c) {
      cout << "The quadratic equation has no real roots!" << endl;
      exit(1);
    }

    cout << scientific;

    cout << endl;
    cout << "Using formula x_{1,2} = (-b +- \\sqrt{b^2-4ac}/(2a))" << endl;
    cout << "x1 = " << x1direct(a,b,c) << endl;
    cout << "x2 = " << x2direct(a,b,c) << endl;
    cout << endl;
    cout << "Using formula x_{1,2} = 2c/(-b -+ \\sqrt{b^2-4ac})" << endl;
    cout << "x1 = " << x1alternative(a,b,c) << endl;
    cout << "x2 = " << x2alternative(a,b,c) << endl;

    return 0;
}
