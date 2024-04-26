#include <iostream>

using namespace std;

int main()
{
  cout << "*********** TEMPRETURE  CALCULATOR ***********\n\n";
  cout << "Please enter the temprechure unit (Please enter eather F or C) = " << '\n';
  
  char tempU;
  float tempF, tempC;
  cin >> tempU;

  if(tempU == 'F' || tempU == 'f'){
    cout << "Please enter the temprechure in Fahrenheit = " << '\n';
    cin >> tempF;
    float tempC = (tempF - 32) * 1.8;
    cout << "The tempreture in Celsius is = " << tempC << '\n';
  }
  else if(tempU == 'C' || tempU == 'c'){
    cout << "Please enter the temprechure in Celsius = " << '\n';
    cin >> tempC;
    float tempF = (tempC * 1.8) + 32;
    cout << "The tempreture in Fahrenheit is = " << tempF << '\n';
  }
  else{
    cout << "ERROR_INVALID_UNIT_ID_";
  }
  cout << "\n**********************************************";
  
 return 0;
}