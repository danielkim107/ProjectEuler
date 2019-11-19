# Solution

Open main for solution.
<br/>
```
units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
special_tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
```
<br/>
Have those lists ready, and iterate through.
1. If number / 100 is greater than or equal to 1, then it must have "hundred" in the string representation of the number. If it has a remainder of 0 when divided by 100, it doesn't require an "and".
2. If the remainder of number / 10 divided by 10 equals 1, then it must be a number with tens/units digits in between 10 ~ 19. Otherwise, add the proper units and tens digit representation and calculation length.
3. Add the length of "one thousand" at the end.

The solution is 21124.