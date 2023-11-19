#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

int getRandom(int min, int max);
void getInput(vector<int> &arr);
void copyVector(const vector<int> &src, vector<int> &dst);
void swap(int &num1, int &num2);
void print(const vector<int> &arr, string name = "");
void print(const vector<int> &arr, int start, int end);
int partition(vector<int> &arr, const int start, const int end, int pivotIndex, int &count);
int quickSort(vector<int> &arr, const char mode = 'd', int start = 0, int end = -1);
bool isSorted(const vector<int> &arr);

int main(int argc, char **argv) {
    // 1. Get an array as input from the user
    vector<int> arr;
    getInput(arr);

    // 2. Make two copies of it
    vector<int> arr1, arr2;
    copyVector(arr, arr1);
    copyVector(arr, arr2);

    int count1, count2;
    // 3. Sort with deterministic Quicksort
    count1 = quickSort(arr1, 'd');

    // 4. Sort with randomized Quicksort
    count2 = quickSort(arr2, 'r');

    // 5. Check the output here
    if(!isSorted(arr1) || !isSorted(arr2))
    {
        cout<<"Error sorting the arrays!"<<endl;
        return 1;
    }

    // 5. Compare the time complexity in terms of no. of comparisons
    cout<<"Number of comparisons in deterministic quicksort = "<<count1<<endl;
    cout<<"Number of comparisons in randomized quicksort= "<<count2<<endl;
    return 0;
}

int getRandom(int min, int max) {
    srand(time(0));
    return min + rand()%(max-min+1);
}

void getInput(vector<int> &arr) {
    int n;
    cout<<"Enter size of array to sort: ";
    cin>>n;
    arr.resize(n);

    cout<<"Enter the elements of array below seperated by space: "<<endl;
    for(int i=0; i<n; i++)
        cin>>arr[i];
}

void copyVector(const vector<int> &src, vector<int> &dst) {
    dst.clear();
    for(int i=0; i<src.size(); i++) 
        dst.push_back(src[i]);
}

void swap(int &num1, int &num2) {
    int temp = num1;
    num1 = num2;
    num2 = temp;
}

void print(const vector<int> &arr, string name) {
    if(name.size() != 0)
        cout<<name<<": ";
    for(int i=0; i<arr.size(); i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}

void print(const vector<int> &arr, int start, int end) {
    for(int i=start; i<end; i++)    
        cout<<arr[i]<<" ";
    cout<<endl;
}

int partition(vector<int> &arr, const int start, const int end, int pivotIndex, int &count) {
    int pivot = arr[pivotIndex];
    swap(arr[pivotIndex], arr[end-1]);

    int left = start, right = end-2;
    while(true) 
    {
        while(arr[left] < pivot) 
        {
            left++;
            count++;
        }

        while(right >= start && arr[right] > pivot)
        {
            right--;
            count++;
        }

        if(left >= right)
            break;
        
        swap(arr[left], arr[right]);
        left++;
        right--;
    }

    swap(arr[left], arr[end-1]);
    return left;
}

int quickSort(vector<int> &arr, const char mode, int start, int end) {
    // set default end
    if(end == -1)
        end = arr.size();

    // termination condition
    if(end <= start+1)
        return 0;
    
    // 1. Select a pivot 
    int p;
    if(mode == 'r')
        p = getRandom(start, end-1);
    else 
        p = end-1;

    int count = 0;
    // 2. Partition according to pivot
    p = partition(arr, start, end, p, count);

    // 3. recursively quickSort on left and right  side of the pivot
    return quickSort(arr, mode, start, p) + quickSort(arr, mode, p+1, end) + count;
    
}

bool isSorted(const vector<int> &arr) {
    for(int i=0; i<arr.size()-1; i++)
        if(arr[i] > arr[i+1])
            return false;
    return true;
}


// Write a program for analysis of quick sort by using deterministic and randomized variant.
