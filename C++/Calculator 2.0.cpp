#include <iostream>

using namespace std;

int main()
{
  char op;
  double num1;
  double num2;
  double result;

  cout << "***************** CALCULATOR *****************\n";

  do
  {
    cout << "Enter the first number: \n";
    cin >> num1;

    if (cin.fail())
    {
      cout << "ERROR_INVALID_VALUE_" << endl;
      cin.clear();
    }
  } while (cin.fail());

  do
  {
    cout << "\nEnter operator ( +, -, *, / ): \n";
    cin >> op;
  } while (op != '+' && op != '-' && op != '*' && op != '/');

  do
  {
    cout << "\nEnter the second number: \n";
    cin >> num2;

    if (cin.fail())
    {
      cout << "ERROR_INVALID_VALUE_" << endl;
      cin.clear();
    }
  } while (cin.fail());

  switch (op)
  {
  case '+':
    result = num1 + num2;
    cout << "\nAnswer: " << result << '\n';
    break;
  case '-':
    result = num1 - num2;
    cout << "\nAnswer: " << result << '\n';
    break;
  case '*':
    result = num1 * num2;
    cout << "\nAnswer: " << result << '\n';
    break;
  case '/':
    result = num1 / num2;
    cout << "\nAnswer: " << result << '\n';
    break;
  }

  cout << "\n**********************************************";

  return 0;
}