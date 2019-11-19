# Solution

Open main for solution.
<br/>
Must run this in Python2 for specific packages/inherent functions used.
<br/>
We are going to create an iterator object using xrange, allowing us to save an enormous amount memory (in comparison to using range; read [here](https://www.geeksforgeeks.org/range-vs-xrange-python/) for explanation.) After doing so, we create a list of booleans, each index representing the specific prime. Then we iterate through each number using an alternative to Sieve of Eratosthenes, where we we check for the multiples of a specific number up to its square and make all the values of the boolean False.
<br/>
After going through the whole list, we are left with a list of booleans, which we can iterate/map through and find the sum of all primes less than 2,000,000.
<br/>
The solution is 142913828922.