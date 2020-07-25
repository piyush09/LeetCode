#include <iostream>
using namespace std;

int getSum(int a, int b) {
    int sum = a;
    
    while (b != 0)
    {
        sum = a ^ b;    //calculate sum of a and b without thinking the carry 
        b = (a & b) << 1;   //calculate the carry
        a = sum;        //add sum(without carry) and carry
    }
    
    return sum;  
}

int main(){
    int a =  -2;
    int b = 3;
    std::cout <<"Sum of Two Integers is:" << getSum(a,b);
    
}
