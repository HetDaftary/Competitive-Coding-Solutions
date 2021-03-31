// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// Tree Node
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to Build Tree
Node *buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


 // } Driver Code Ends
/* A binary tree node

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;

    Node(int x){
        data = x;
        left = right = NULL;
    }
};
 */

class Solution{
  public:
    void storeInOrder(Node *root, vector<int> &inOrder) {
        if (!root) {
            inOrder.push_back(-1);
            return;
        }
        storeInOrder(root->left, inOrder);
        inOrder.push_back(root->data);
        storeInOrder(root->right, inOrder);
    }
    
    void storePreOrder(Node *root, vector<int> &preOrder) {
        if (!root) {
            preOrder.push_back(-1);
            return;
        }
        preOrder.push_back(root->data);
        storePreOrder(root->left, preOrder);
        storePreOrder(root->right, preOrder);
    }
    
    void computeLPSArray(vector<int> &pat, int M, vector<int> &lps) {
        int len = 0;
        lps[0] = 0;
        int i = 1;
        while (i < M) {
            if (pat[i] == pat[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
    }
    
    bool KMPSearch(vector<int> &txt, vector<int> &pat) {
        int M = pat.size();
        int N = txt.size();
        vector<int> lps(M);
    
        computeLPSArray(pat, M, lps);
    
        int i = 0; // index for txt[]
        int j = 0; // index for pat[]
        while (i < N) {
            if (pat[j] == txt[i]) {
                j++;
                i++;
            }
            if (j == M) {
                j = lps[j - 1];
                return true;
            } else if (i < N && pat[j] != txt[i]) {
                if (j != 0)
                    j = lps[j - 1];
                else
                    i = i + 1;
            }
        }
        return false;
    }
    
    
    void print(vector<int> &a) {
        for (int u : a) {
            cout << u << " ";
        }
        cout << "\n";
    }
    
    bool isSubTree(Node *T, Node *S) {
        if (S == nullptr)
            return true;
        if (T == nullptr)
            return false;
    
        vector<int> inOrderT, preOrderT, inOrderS, preOrderS;
        storeInOrder(T, inOrderT);
        storePreOrder(T, preOrderT);
    
        storeInOrder(S, inOrderS);
        storePreOrder(S, preOrderS);
    
    //    print(inOrderT);
    //    print(inOrderS);
    //
    //    print(preOrderT);
    //    print(preOrderS);
    //
    //    cout << KMPSearch(inOrderT, inOrderS) << "\n";
    //    cout << KMPSearch(preOrderT, preOrderS) << "\n";
    
        if (KMPSearch(inOrderT, inOrderS) && KMPSearch(preOrderT, preOrderS))
            return true;
    
        return false;
    }
};

// { Driver Code Starts.

int main() {
    int tc;
    scanf("%d ", &tc);
    while (tc--) {
        string strT, strS;
        getline(cin, strT);
        Node *rootT = buildTree(strT);
        getline(cin, strS);
        Solution obj;
        Node *rootS = buildTree(strS);
        cout << obj.isSubTree(rootT, rootS) << "\n";

    }


    return 0;
}  // } Driver Code Ends