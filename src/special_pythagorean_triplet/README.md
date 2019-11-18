# Solution

  

Open main for solution.

<br/>

Rather than coding up this problem, I simply thought of the simple ways to generate Pythagorean Triples for even and odd numbers. Given that $a$ is part of a Pythagorean Triple $(a, b, c)$,
<br/>
1. If $a$ is odd, the other two sides are floor($\frac{a^2}{2}$) and ceil($\frac{a^2}{2}$).
2. If $a$ is even, the other two sides are $(\frac{a^2}{4} + 1)$ and $(\frac{a^2}{4} - 1)$.
<br/>
Given this, we know that then given $a$,
1. If $a$ is odd, then $a + a^2$ must equal $1000$.
2. If $b$ is even, then $a + \frac{a^2}{2}$ must equal $1000$.
<br/>
However, rather checking for whether the sums equal exactly 1000, we can check whether the sum of the sides equal to a factor of 1000 since we can simply multiply by its corresponding factor for 1000.
<br/>
By checking the first couple of integers (starting from 3), we find that when $a = 8$, $8 + \frac{8^2}{2} = 40$. This means by multiplying all the sides of this Pythagorean Triple by $25$ must equal $1000$.
<br/>
The following triple is $(8, 15, 17)$, so the Pythagorean Triple that sums up to $1000$ is $(200, 375, 425)$, and the product of those numbers is $31875000$.