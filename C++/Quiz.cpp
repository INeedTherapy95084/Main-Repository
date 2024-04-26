#include <iostream>

using namespace std;

int main() {
  
  string questions[] = {"1. What year was C++ created?: ", 
                     "2. Who invented C++?: ", 
                     "3. What is the predecessor of C++?: ", 
                     "4. Is the Earth flat?"};

  string options[][4] = {{"A. 1969", "B. 1975", "C. 1985", "D. 2000"},
                         {"A. Guido van Rossum", "B. Bjarne Stroustrup",
                            "C. John Carmack", "D. Mark Zuckerberg"},
                         {"A. C", "B. C+", "C. C--", "D. Java"},
                         {"A. Yes", "B. No", "C. Sometimes", "D. What's Earth?"}};

  char answerKey[] = {'C', 'B', 'A', 'B'};
  int size = sizeof(questions)/sizeof(questions[0]);
  char guess;
  int score = 0;

  for(int i = 0; i < size; i++){
    cout << "\n*****************************************\n";
    cout << questions[i] << '\n';
    cout << "*****************************************\n";

    for(int j = 0; j < sizeof(options[i])/sizeof(options[i][0]); j++){
      cout << '\n' << options[i][j] << '\n';
    }
    cin >> guess;
    guess = toupper(guess);
    if(guess == answerKey[i]){
      cout << "\nCORRECT!\n";
      score++;
    }
    else{
      cout << "\nWRONG!\n";
      cout << "\nCorrect answer: " << answerKey[i] << '\n';
    }
  }

  cout << "\n*****************************************\n";
  cout << "*               RESULTS                 *\n";
  cout << "*****************************************\n";
  cout << "You got " << score << " out of " << size << " correct\n";
  cout << "Your final result is: " << (score/(double)size) * 100 << "%\n"; 
  return 0;
}