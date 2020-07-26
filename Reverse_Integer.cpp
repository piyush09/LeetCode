#include<iostream>
using namespace std;

int reverse(int x) {
    long long result = 0;
    while(x) {
        result = result*10 + x%10;
        x = x/10;        
    }
    
    if (result < INT_MIN || result > INT_MAX)
        return 0;
    else
        return result;
        
    
}

int main(){
    int x = -123;
    cout << "Reversed Input Integer is:" << reverse(x);
}