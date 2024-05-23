#include <iostream>

using namespace std;

int main()
{
    char op;
    double firstnum;
    double secondnum;
    double result;

    cout << "***************** CALCULATOR *****************\n";

    do{

        cout << "Please enter the first number: \n";
        cin >> firstnum;
        
        if(cin.fail()){
           cout << "ERROR_INVALID_VALUE_";
           cin.clear();
        }

    }while(cin.fail());

    do{

        cout << "Please an operator(+ , -, /, *): \n";
        cin >> op;

    }while(op != '+' && op != '-' && op != '/' && op != '*');

    do{

        cout << "Please enter the first number: \n";
        cin >> secondnum;

        if(cin.fail()){
           cout << "ERROR_INVALID_VALUE_";
           cin.clear();
        }

    }while(cin.fail());

    switch(op){
        case '+':
            result = firstnum + secondnum;
            cout << "Answer: " << result << '\n';
            break;
        case '-':
            result = firstnum - secondnum;
            cout << "Answer: " << result << '\n';
            break;
        case '/':
            result = firstnum / secondnum;
            cout << "Answer: " << result << '\n';
            break;
        case '*':
            result = firstnum * secondnum;
            cout << "\nAnswer: " << result << '\n';
            break;
    }

    cout << "\n**********************************************";

    return 0;
}