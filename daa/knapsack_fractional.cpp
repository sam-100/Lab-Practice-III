#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Item
{
    double price, weight;

    Item(double p, double w) {
        price = p;
        weight = w;
    }

    double effective_cost() const {
        return price/weight;
    }

    friend ostream &operator<<(ostream &out, const Item &item);
        
};

struct CompareItems
{
    bool operator()(const Item &item1, const Item &item2) const {
        return item1.effective_cost() < item2.effective_cost();
    }
};

ostream& operator<<(ostream &out, const Item &item);



int main(int argc, char **argv) {
    
    vector<Item> items;
    int count;
    double capacity;
    double profit = 0, weight = 0;

    // 1. Get the inputs from the user
    cout<<"Enter the total count of items: ";
    cin>>count;
    cout<<"Enter the item price followed by its weight below, each item on new line. "<<endl;
    for(int i=0; i<count; i++)
    {
        double price, weight;
        cin>>price>>weight;
        items.push_back(Item(price, weight));
    }
    cout<<"Enter the capacity of your bag (weight in kg): ";
    cin>>capacity;

    // 2. Put the items in priority queue with proper comparator type
    priority_queue<Item, vector<Item>, CompareItems> pque;
    for(int i=0; i<items.size(); i++)
        pque.push(items[i]);

    // 3. Now calculate the profit
    while(weight < capacity && !pque.empty())
    {
        Item item = pque.top();
        pque.pop();


        if(weight+item.weight >= capacity)
        {
            profit += (capacity-weight)/item.weight*item.price;
            weight = capacity;
            continue;
        }

        profit += item.price;
        weight += item.weight;

    }

    // 4. return the profit
    cout<<"The maximum profit that can be made is "<<profit<<endl;

    return 0;
}


ostream& operator<<(ostream &out, const Item &item) {
    out<<"{"<<item.price<<", "<<item.weight<<"}";
    return out;
}



// Write a program to solve a fractional Knapsack problem using a greedy method.
