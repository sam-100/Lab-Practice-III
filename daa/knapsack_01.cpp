#include <iostream>
#include <vector>

using namespace std;

struct Item 
{
    double value, weight;

    Item(double v, double w) {
        value = v;
        weight = w;
    }
    
    friend ostream &operator<<(ostream &out, const Item &item);
};

ostream &operator<<(ostream &out, const Item &item);
void print(const vector<vector<double>> &arr);
double valueAt(const vector<vector<double>> &arr, int i, int j);
double dynamicProgramming(const vector<Item> &itemSet, const double capacity);

int main(int argc, char **argv) {

    // 1. Get the input 
    vector<Item> itemSet;
    int count;
    double capacity;
    cout<<"Enter the number of items: ";
    cin>>count;
    cout<<"Enter the value and weight of each item on a new line below:"<<endl;
    for(int i=0; i<count; i++)
    {
        double v, w;
        cin>>v>>w;
        itemSet.push_back(Item(v, w));
    }
    cout<<"Enter teh capacity of the knapsack: ";
    cin>>capacity;

    // 2. Solve using dynamic programming
    double result = dynamicProgramming(itemSet, capacity);

    // 3. Display the output
    cout<<"Maximum Value in Knapsack can be "<<result<<endl;

    return 0;
}

ostream &operator<<(ostream &out, const Item &item) {
    out<<"{"<<item.value<<", "<<item.weight<<"}";
    return out;
}

void print(const vector<vector<double>> &arr) {
    for(int i=0; i<arr.size(); i++)
    {
        for(int j=0; j<arr[0].size(); j++)
        {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
}

double valueAt(const vector<vector<double>> &arr, int i, int j) {
    if(i < 0 || j < 0)
        return 0;
    return arr[i][j];
}

double dynamicProgramming(const vector<Item> &itemSet, const double capacity) {
    // 1. Create a dp table 
    vector<vector<double>> table(capacity+1, vector<double>(itemSet.size(), 0));

    // 2. traverse the table and find the solution
    for(int i=0; i<=capacity; i++)
    {
        for(int j=0; j<itemSet.size(); j++)
        {
            int pick, leave;
            if(i >= itemSet[j].weight)
                pick = itemSet[j].value+valueAt(table, i-itemSet[j].weight, j-1);
            else 
                pick = 0;
            leave = valueAt(table, i, j-1);
            table[i][j] = max(pick, leave);
        }
        
    }
    print(table);
    // 3. return the result
    return table[capacity][itemSet.size()-1];

}


// Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and
// bound strategy.
