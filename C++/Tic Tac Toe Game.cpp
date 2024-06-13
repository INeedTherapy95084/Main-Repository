#include <iostream>
#include <ctime>

using namespace std;

void drawBored(char *spaces){
  cout << "\n\n     |     |     " << '\n';
  cout << "  " << spaces[0] << "  |  " << spaces[1] << "  |  " << spaces[2] << "  ";
  cout << "\n_____|_____|_____";
  cout << "\n     |     |     " << '\n';
  cout << "  " << spaces[3] << "  |  " << spaces[4] << "  |  " << spaces[5] << "  ";
  cout << "\n_____|_____|_____";
  cout << "\n     |     |     " << '\n';
  cout << "  " << spaces[6] << "  |  " << spaces[7] << "  |  " << spaces[8] << "  ";
  cout << "\n     |     |     " << '\n' << '\n';
}

void playerMove(char *spaces, char playerC){
  int num;
  do{
    cout << "Enter the space you want to place your marker(1-9): \n";
    cin >> num;
    if(isalnum(num)){
      cout << num;
      num--;
      if(spaces[num] == ' ' && num >! 0 && num <! 8 && num != num/1){
        spaces[num] = playerC;
        break;
      }
    }
    else{
        cin.clear();
      }
  }while(true);
}

void computerMove( char *spaces, char compC){
  int num;
  srand(time(NULL));
  while(true){
    num = rand() % 9;
    if(spaces[num] == ' '){
      spaces[num]  = compC;
      break;
    }
  }

}

bool checkWinner(char *spaces, char playerC, char compC, int &score){

  if(spaces[0] != ' ' && spaces[0] == spaces[1] && spaces[1] == spaces[2]){
    if(spaces[0] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else if(spaces[3] != ' ' && spaces[3] == spaces[4] && spaces[4] == spaces[5]){
    if(spaces[3] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else if(spaces[6] != ' ' && spaces[6] == spaces[7] && spaces[7] == spaces[8]){
    if(spaces[6] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else if(spaces[0] != ' ' && spaces[0] == spaces[3] && spaces[3] == spaces[6]){
      if(spaces[0] == playerC){
        score++;
        cout << "You win!";
      }
      else{
        cout << "You lose";
      }
    }
  else if(spaces[1] != ' ' && spaces[1] == spaces[4] && spaces[4] == spaces[7]){
    if(spaces[1] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else if(spaces[2] != ' ' && spaces[2] == spaces[5] && spaces[5] == spaces[8]){
    if(spaces[2] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else if(spaces[0] != ' ' && spaces[0] == spaces[4] && spaces[4] == spaces[8]){
    if(spaces[0] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    };
  }
  else if(spaces[6] != ' ' && spaces[6] == spaces[4] && spaces[4] == spaces[2]){
    if(spaces[6] == playerC){
      score++;
      cout << "You win!";
    }
    else{
      cout << "You lose";
    }
  }
  else{
    return false;
  }

  return true;
}


bool checkTie(char *spaces, char playerC, char compC){
  for(int i = 0; i < 9; i++){
    if(spaces[i] == ' '){
      return false;
    }
  }
  cout << "Its a tie!";
  return true;
  
}

int main() {

  char spaces[9]{' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
  char playerC = 'X';
  char compC = 'O';
  char playAgain;
  bool running = true;
  int score = 0;

  drawBored(spaces);
  cout << "Player(X), Computer(O)\n";

  do{
    while(running){
      playerMove(spaces, playerC);
      drawBored(spaces);

      if(checkWinner(spaces, playerC, compC, score)){
        running = false;
        break;
      }
      else if(checkTie(spaces, playerC, compC)){
        running = false;
        break;
      }

      computerMove(spaces, compC);
      drawBored(spaces);

      if(checkWinner(spaces, playerC, compC, score)){
        running = false;
        break;
      }
      else if(checkTie(spaces, playerC, compC)){
        running = false;
        break;
      }
    }
    cout << "\nScore: " << score << '\n';
    cout << "\nDo you want to play again? (y/n) ";
    cin >> playAgain;

    playAgain = tolower(playAgain);
    if(playAgain == 'y' || playAgain == 'Y'){
      running = true;
      for(int i = 0; i < 9; i++){
        spaces[i] = ' ';
      }
      drawBored(spaces);
    }
    else{
      running = false;
    }

  }while(running);

  return 0;
}