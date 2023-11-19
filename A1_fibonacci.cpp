#include <iostream>

using namespace std;

int fibonacci_recursive(const int index, int &count);
int fibonacci_iterative(const int index, int &count);

int main(int argc, char **argv) {

    int index; 
    cout<<"Enter the index number to find the fibonacci: ";
    cin>>index;

    int rec_count = 0, itr_count = 0;
    
    // get the fibonacci number at index 'index', starting from 1
    int fib_r = fibonacci_recursive(index, rec_count);
    int fib_i = fibonacci_iterative(index, itr_count);

    cout<<"The fibonacci number is "<<fib_r<<endl;
    cout<<"The recursive algorithm took "<<rec_count<<" comparisons."<<endl;
    cout<<"The iterative algorithm took "<<itr_count<<" comparisons."<<endl;

}


int fibonacci_recursive(const int index, int &count) {
    if(index <= 2)
        return 1;

    count++;
    return fibonacci_recursive(index-1, count)+fibonacci_recursive(index-2, count);   

}


int fibonacci_iterative(const int index, int &count) {

    int arr[3] = {1, 1, 0};

    for(int i=2; i<index; i++)
    {
        count++;
        arr[i%3] = arr[(i-1)%3] + arr[(i-2)%3];
    }

    return arr[(index-1)%3];

}


// Problem Statement: Write a program non-recursive and recursive program to calculate Fibonacci numbers and
// analyze their time and space complexity.
