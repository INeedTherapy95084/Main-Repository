#include <iostream>
#include <ctime>

using namespace std;

int main() 
{

  int num;
  int guess;
  int tries = 0;
  
srand(time(NULL));
  num = (rand() % 100) + 1;

  cout << "******* GUESSING THE NUMBER GAME *******" << '\n' << '\n';

  do{
    
    cout << "Enter a guess (1-100): ";
    cin >> guess;
    tries++;

    if(guess > num){
      cout << "Too high" << '\n';
    }
    else if(guess < num){
      cout << "Too low" << '\n';
    }
    else{
      cout << "\nCorrect! You got it in " << tries << " tries!" << '\n' << '\n';
    }
  }while(guess != num);

  cout << "**************************************";
  
  return 0;
}