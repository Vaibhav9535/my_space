//tring to learn cpp 

#include <iostream>
#include <string>
int main (int argc, char *argv[]) {
  std::cout<<"Enter your string"<<std::endl;
  std::string str;
  std::getline(std::cin, str);
  std::cout<<"Entered string is --> "<<str;
  return 0;
}

