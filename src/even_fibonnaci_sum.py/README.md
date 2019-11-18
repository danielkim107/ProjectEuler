# Solution

Simply generate the Fibonacci sequence recursively before 4,000,000. While generating, if the term is even, add to the final answer.
<br/><br/>

```python
answer = 0

def generateFibonacci(first, second, answer):
    next = first + second
    if next > 4000000:
        print(answer)
        return
    if next % 2 == 0:
        answer = answer + next
    generateFibonacci(second, next, answer)


first = 1
second = 1

generateFibonacci(first, second, answer)
```