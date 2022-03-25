"""Prime Mail Reads
Problem Description
A mathematician reads her emails in a unique way. She numbers her unread emails serially and after reading the prime numbered emails, renumbers the remaining unread mails serially. She repeats this process of reading prime numbered emails and renumbering unread emails. Only when the number of unread emails reaches 1 (and this counts as a new renumbering) does she allow herself to read this unique, non-prime numbered email! Given the initial number of unread emails, determine the number of times the mathematician would need to renumber emails till all her emails have been eventually read.

Constraints
1 <= N <= 10 ^ 4

Input
Input consists of a single integer N which denotes the initial number of unread emails.

Output
Calculate and output the number of times renumbering is required to read all the emails.

Time Limit (secs)
1

Examples
Example 1

Input

10

Output

4

Explanation

We have 10 unread emails initially.

Renumbering 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

After reading emails numbered 2, 3, 5 and 7, we have 6 unread emails left.

Renumbering 2: 1, 2, 3, 4, 5, 6

After reading emails numbered 2, 3 and 5, we have 3 emails left.

Renumbering 3: 1, 2, 3

After reading emails 2 and 3, we have 1 email left.

Final renumbering 4: 1

Renumbering is required 4 times to read all the 10 emails. Hence, output is 4.

Example 2

Input

50

Output

8

Explanation

Renumbering 1: 1..50: 15 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.

Renumbering 2: 1..35: 11 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31

Renumbering 3: 1..24: 9 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23

Renumbering 4: 1..15: 6 primes: 2, 3, 5, 7, 11, 13

Renumbering 5: 1..9: 4 primes: 2, 3, 5, 7

Renumbering 6: 1..5: 3 primes: 2, 3, 5

Renumbering 7: 1, 2: 1 prime: 2

Renumbering 8: 1

We have renumbered 8 times. Hence output is 8."""

N=int(input())
c=1
from math import sqrt
 
def isPrime(n):
 
    
    if (n <= 1):
        return False
 
    
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

while N>1:
    for i in range(1,N+1):
        if isPrime(i):
            N=N-1
    c+=1
print(c)
