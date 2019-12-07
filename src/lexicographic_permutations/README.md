# Solution

Open main for solution.
<br/>
This solution will for any lexicographic permutation. Have the possible digits set up in a list, and set the nth number as the target. We know that given these numbers, we can make out how many permutations will exist starting with 'a,' and so on.
<br/>
For our example, we know that the first lexicographic permutation with digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 is 0123456789. With the first digit being 0, we have up to 9! (362880) permutations. Thus, we can reduce the number of permutations we would have to go through this way, and if it goes over our current target, we know that the nth digit will be of that specific index.
<br/>
Thus, we just set up a simple for-loop, and set up a new temp every time we go through the loop. As soon as we go over our limit, we know that we are on the nth digit that is suppsed to be our 1 millionth permutation. We keep doing this for the first nine digits, and whatever is left in numbers will be the last digit to append.
<br/>
The solution is 2783915460.