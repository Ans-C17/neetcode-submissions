/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode*& node, int target) {
        if (!node) return;
        
        if (!node->left and !node->right) {
            if (node->val == target) {
                delete node;
                node = nullptr;
            }

            return;
        }

        dfs(node->left, target);
        dfs(node->right, target);
        if (!node->left and !node->right) {
            if (node->val == target) {
                delete node;
                node = nullptr;
            }
        }
    }

    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        dfs(root, target);
        return root;
    }
};