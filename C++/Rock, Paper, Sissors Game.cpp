#include <iostream>
#include <ctime>

using namespace std;

char getUserChoice(){
  char player;
  cout << "\n******** ROCK PAPER SISSORS ********\n" << endl;
 do{
  cout << "Choose from the following: \n";
  cout << "'r' for rock\n'p' for paper\n's' for sissors\n";
  cin >> player;

   if(player != 'r' && player != 'p' && player != 's' ){ 
     cout << "ERROR_INVALID_INPUT_TRY_AGAIN_\n\n";
   }

 }while(player != 'r' && player != 'p' && player != 's' );

  return player;
}

char getCompChoice(){

  srand(time(NULL));
  int num = rand() % 3 + 1;  

  switch(num){
    case 1: return 'r';
    case 2: return 'p';
    case 3: return 's';
  }
  return 0;
}

void showChoice(char choice){
  switch(choice){
    case 'r' : cout << "rock";
      break;
    case 'p': cout << "paper";
      break;
    case 's': cout << "sissors";
      break;
  }
}

double chooseWinner(char player, char comp, char playAg, int &points){
  switch(player){
    case 'r':
      if(comp == 'r'){
        cout << "\nTIE" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 'p'){
        cout << "\nPlayer wins!" << endl;
        points++;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 's'){
        cout << "\nComputer wins!" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      break;
    case 'p':
      if(comp == 'r'){
        cout << "\nPlayer wins!" << endl;
        points++;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 'p'){
        cout << "\nTIE" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 's'){
        cout << "\nComputer wins!" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      break;
    case 's':
      if(comp == 'r'){
        cout << "\nComputer wins!" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 'p'){
        cout << "\nPlayer wins!" << endl;
        points++;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      else if(comp == 's'){
        cout << "\nTIE" << endl;
        cout << "\nYour score is " << points;
        cout << "\n\nDo you want to play again? (y/n) ";
        cin >> playAg;
      }
      break;
    
  } 
  return playAg;
  return points;
}


int main() {
  char comp;
  char player;
  char playAg;
  int points = 0;

 do{

    player = getUserChoice();
    cout << "\nYour choice is: ";
    showChoice(player);

    comp = getCompChoice();
    cout << "\nComputer's choice is: ";
    showChoice(comp);
    chooseWinner(player, comp, playAg, points);

  }while(playAg != 'y');

  cout << "\n************************************";

  return 0;
}