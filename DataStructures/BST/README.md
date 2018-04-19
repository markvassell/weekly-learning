#Binary Search Tree Breakdown

###The init method: initializing<br>
1. The breakdown of this structure is a parent node with two child nodes (left and right node).
2. In my algorithm's case I made the left child any value less or equal to the parent in value.
3. The right child is anything greater than the parent in value.

###The contains method<br>
1. The structure of my BST algorithm dictates that anything node with a lesser or equal to that of a parent node goes to
the left and node with a value that is greater goes to the right.
2. My approach traverses the BST with the structure mentioned above in mind.
3. First it checks if the current parent is the value being searched for and if so returns that its found.
4. if the value wasn't found in step 3. Check if the value is less than or greater than the parent current nodes value
5. If its greater than the current node's value, check to make sure that the right node has a value then recursively 
call the contains methods with the right nodes as the parent node. The opposite is done if the value is less than the 
current node. 
6. If a left or right node comes up as Null or None in my case return that the value isn't in the BST

###The in-order method
1. In this method the values in the tree are printed in ascending order.  It's another recursive algorithm the check for
the left most node first then it parent second and repeat the process on its parent's right node if it available until the 
entire list is complete. In short, first print the left side, then the root, then the right side.

### The pre-order method
1. This method prints the values in the tree starting at the top and heads to the left and then to the right. Example:
if we have a list 1,3,4,5 and 4 is the parent then it would print 4,1,3,5 as the result.

### The post-order method
The method requires printing the left child nodes, then the right child nodes then the parents. 




 
