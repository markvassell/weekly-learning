# Algorithms

### Bubble Sort

### Insertion Sort

### Selection Sort

### Merge Sort

Merge sort is a efficient and elegant algorithm. It uses the concept of divide and conquer. By this I mean that it 
breaks down the task at hand into smaller and more manageable tasks and works it way back to the final goal.  This is 
a recursive algorithm that separates the the given list into equal portions (or as close to even as possible) until each
element is then considered to be its own list. It then recombines the those lists into sorted order as it goes back up 
the recursion stack. To clarify this ordered recombination is done at each step in the recursion stack.

In this algorithm the first thing I checked for is if the list has one element. If this is the case then the list is 
already considered to be sorted and I just return the same list that was provided as the input.  

![alt text](../Images/Merge%20Sort%20Images/1_element_condition.png "con1 One Element Condition")

The second step in this algorithm is to separate the list into two halves and do the same thing to each half of the list
until all the elements are separated into their own list.  
![alt text](../Images/Merge%20Sort%20Images/breakdown_code.PNG "con2 One Element Condition")

![alt text](../Images/Merge%20Sort%20Images/merge_sort_breakdown.PNG "con2 One Element Condition")

The Final Step is to recombine the separated lists into sorted list at each step of the recursion stack. There are many
ways to do this step.  In my approach I created an entirely new list to wish I append the sorted data to. I loop until 
one of the lists is empty and compare the first term in each list and the list that has the smallest element, get that 
element removed and appended to the results list. At the end of the loop one of the lists must be empty and in that case
the remain element of that list are already in sorted order and they get appended to the list  
![alt text](../Images/Merge%20Sort%20Images/recombine_algo.PNG "con4 One Element Condition")
![alt text](../Images/Merge%20Sort%20Images/recombine.PNG "con3 One Element Condition")

