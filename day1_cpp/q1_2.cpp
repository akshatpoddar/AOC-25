#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  ifstream InputFile("inputs/q1.txt");
  string lineText;
  int count = 0;
  int pos = 50;

  while(getline(InputFile, lineText)) {
    int sign = 1;
    if(lineText[0] == 'L') sign = -1;
    pos = pos + sign * stoi(lineText.substr(1));
    if(pos < 0 || pos > 99){
      if(pos < 0 && pos > -100){
        count++;
      }
      int quotient = abs(pos) / 100;
      count += quotient;
    }
    pos = pos % 100; 
  }
  cout << count << endl;
}
