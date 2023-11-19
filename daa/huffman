#include <iostream>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

struct Node;

struct CompareNodes;

Node *createTree(const unordered_map<char, int> &freq);

void writeCodes(const unordered_map<char, int> &freq, const Node *root, unordered_map<char, string> &codes, string current_code = "");

string encode(const string &input, const unordered_map<char, string> &codes);

string decode(const string &encoding, const Node *root);

template <typename Key, typename Value> 
void print(const unordered_map<Key, Value> &umap);

int main(int argc, char **argv) {
	
    // 1. Get the input from user
    string input;
    cout<<"Enter a string to encode: ";
    getline(cin, input);

	// 2. Calculate frequency for each character
    unordered_map<char, int> frequency;
    for(int i=0; i<input.size(); i++)
        frequency[input[i]]++;

    // 3. Create the huffman tree
    Node *root = createTree(frequency);

    // 4. Calculate codes for each character
    unordered_map<char, string> codes;
    writeCodes(frequency, root, codes);

    // 5. Create the Huffman encoding
    string encoding = encode(input, codes);

    // 6. Decode the encoded string with the help of huffman tree
    string decoding = decode(encoding, root);

    // 7. Print the decoded output
    cout<<"Code mapping: "<<endl;
    print(codes);
    cout<<"encoded string (size = "<<encoding.size()/8<<" bytes) "<<endl;
    cout<<encoding<<endl;
    cout<<"Decoded string (size = "<<decoding.size()<<"bytes) "<<endl;
    cout<<decoding<<endl;
    
}

struct Node 
{
    int freq;
    bool leaf;
    char ch;
    Node *left, *right;

    Node(int freq, char ch = '$', Node *l = nullptr, Node *r = nullptr) {
        this->freq = freq;
        this->ch=ch;
        left = l;
        right = r;
        leaf = (l == nullptr && r == nullptr) ? true : false;
    }

    bool isLeaf() const {
        return leaf;
    }
};

struct CompareNodes
{
    bool operator()(const Node *node1, const Node *node2) const {
        return node1->freq > node2->freq;
    }
};

Node *createTree(const unordered_map<char, int> &freq) {

    // 1. Create node for each character and put it into priority queue
    priority_queue<Node*, vector<Node*>, CompareNodes> pque;
    for(unordered_map<char, int>::const_iterator itr = freq.begin(); itr != freq.end(); itr++)
        pque.push(new Node(itr->second, itr->first));


    // 2. While this size of priority queue is greater than 1, do the following:- 
    // 2.1. Pick the two elements with smallest frequency
    // 2.2. Create a new node with frequency of their sum, and attach them to its left or right
    // 2.3. Push the new Node back into priority queue
    while(pque.size() > 1)
    {
        Node *first, *second;
        first = pque.top();
        pque.pop();
        second = pque.top();
        pque.pop();

        pque.push(new Node(first->freq+second->freq, '$', first, second));
    }
    // 3. Pop the only node from priority queue and return it
    return pque.top();

}

void writeCodes(const unordered_map<char, int> &freq, const Node *root, unordered_map<char, string> &codes, string current_code) {
    
    if(root == nullptr)
        return;
    
    if(root->isLeaf())
    {
        codes[root->ch] = current_code;
        return;
    }

    writeCodes(freq, root->left, codes, current_code+'0');
    writeCodes(freq, root->right, codes, current_code+'1');
}

string encode(const string &input, const unordered_map<char, string> &codes) {
    string output;

    for(int i=0; i<input.size(); i++)
        output += codes.at(input[i]);

    return output;
}

string decode(const string &encoding, const Node *root) {
    string output;

    const Node *curr = root;

    for(int i=0; i<encoding.size(); i++)
    {
        if(curr->isLeaf())
        {
            output += curr->ch;
            curr = root;
        }
        if(encoding[i] == '0')
            curr = curr->left;
        else 
            curr = curr->right;
    }

    if(curr->isLeaf())
        output += curr->ch;


    return output;
}

template <typename Key, typename Value> 
void print(const unordered_map<Key, Value> &umap) {
    typename unordered_map<Key, Value>::const_iterator itr;
    for(itr = umap.begin(); itr != umap.end(); itr++)
        cout<<itr->first<<": "<<itr->second<<endl;
    cout<<endl;
}
