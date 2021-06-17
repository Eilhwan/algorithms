#include <iostream>
#include <queue>

struct node
{
    std::string position;
    node* first;
    node* second;
};

struct org_tree
{
    node* root;

    static org_tree create_org_structrue(const std::string& pos)
    {
        org_tree tree;
        tree.root = new node(pos, NULL, NULL);
        return tree;
    }

    static node* find(node* root, const std::string& value)
    {
        if (root == NULL)
            return root;
        if (root->position == NULL)
    }
};

