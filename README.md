# O(n) Palindrome Check

![Python Version](https://img.shields.io/badge/Python-3.6-green?style=flat)

| Param            | Complexity (worst-case) |
|------------------|:-----------------------:|
| Time Complexity  |          O(n)           |
| Space Complexity |          O(1)           |

### When to Use
* Whenever there's a situation where you must find the longest palindrome in a body of text in the quickest possible manner 

## How this Palindrome Check Works
This script checks a string or substring for any sequence that is a palindrome (reads the same forwards
and backwards).  The longest sequence that is a valid palindrome will be returned.

> **Note:** A string containing one character is considered palindromic.  So as long as your
> search text contains at least one character, it will return a positive match.

This algorithm iterates through each character and makes, at most, two comparisons per pass.  Whenever
a longer palindromic sequence is discovered, `j` is updated with the length of said sequence.  Both
future `index + j` and past `index - j` indices are evaluated in subsequent passes so as `j` increases,
the search range increases with it.

Unfortunately, I cannot claim full credit for this algorithm as I wrote this from my memory of a similar
algorithm I came across a while back.  If anyone knows the origins of this algorithm feel free to let me 
know so I can give credit.