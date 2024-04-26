#include <iostream>
#include <iomanip>

using namespace std;

void showBalance(double balance){
  cout << setprecision(2) << fixed << "\nYou balance is  $" << balance << '\n';
}

double deposit(){
  double amount;
  cout << "\nEnter the amount you want to deposit: ";
  cin >> amount;
  if(amount > 0){
    return amount;
  }
  else{
    cout << "\nERROR_INVALID_AMOUNT_ENTERD_\n";
    return 0;
  }
}

double withdraw(double balance){
  double amount;
  cout << "\nEnter the amount you want to withdraw: ";
  cin >> amount;
  
  if(amount > balance){
    cout << "\nInsuficiant funds\n";
    return 0;
  }
   else if(amount < 0){
     cout << "\nERROR_INVALID_AMOUNT_ENTERD_\n";
     return 0;
  }
  else{
    return amount;
  }
}


int main() {

  double balance = 0;
  int choice;
  
 do{
    cout << "\n**************** ATM ****************" << '\n' << '\n';
    cout << "Welcome to the ATM \nPlease enter your choice: " << '\n';
    cout << "1. Show balance\n" << "2. Deposit\n" << "3. Withdraw\n" << "4. Exit\n" << "(Please enter a digit only)\n";
    cin >> choice;
   
    switch(choice){
     case 1: showBalance(balance);
       break;
     case 2: balance += deposit();
       showBalance(balance);
       break;
     case 3: balance -= withdraw(balance);
       showBalance(balance);
       break;
     case 4: cout << "\nThank you for using the ATM";
       break;
     default:
       cout << "ERROR_INVALID_CHOICE_ENTERED_\n";
   }
 }while(choice != 4);

  cout << '\n' << '\n' << "*************************************";
  
return 0;
}