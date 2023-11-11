#include <iostream>
#include <string>
using namespace std;



int main (int argc, char *argv[]) {

  int vowels,spaces;
  string str,word;
  cout<<"Enter the string"<<endl;
  getline(cin,str);

  for(char chr:str) {
    if(chr=='a'||chr=='e'|| chr=='i'||chr=='o'|| chr=='u') {
      vowels++;
    }
    else if(chr==' ')
    {
      spaces++;
    }
  }
  cout<<"Number of vowels = "<<vowels<<endl;
  cout<<"Number of constonantes = "<<(str.length()-(vowels+spaces))<<endl;

  return 0;
}

