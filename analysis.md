# Algorithmic Efficiency & Recursion Toolkit (AERT)

This brief report outlines the complexity and paradigms demonstrated by the toolkit.

## Components and Paradigms

1. **Stack ADT**
   - *Implementation*: Array-backed (Python list).  Supports push, pop, peek, is_empty, size.
   - *Paradigm*: Abstract data type demonstrating encapsulation; operations are **O(1)** time.
   - *Use case*: Foundation for iterative algorithms and can be used for recursion simulation.

2. **Recursive Algorithms**
   - **Factorial**
     - Definition: `n! = n * (n-1)!` with base case `0! = 1`.
     - Complexity: **O(n)** calls, linear in `n`; each call does constant work.
     - Paradigm: *Simple recursion / mathematical recurrence*.

   - **Fibonacci**
     - Definition: `F(0)=0`, `F(1)=1`, `F(n)=F(n-1)+F(n-2)`.
     - Complexity: **O(2^n)** time due to repeated subproblems; exponential growth.
     - Paradigm: *Recursive divide-and-conquer*; demonstrates inefficiency without memoization.

   - **Tower of Hanoi**
     - Moves `n` disks between pegs, moving one at a time and never placing a larger on a smaller.
     - Recurrence: `T(n) = 2*T(n-1) + 1`, leading to **O(2^n)** moves.
     - Trace for `n=3` illustrates call structure and move order.
     - Paradigm: *Recursive problem decomposition / divide-and-conquer*.

   - **Binary Search**
     - Operates on a sorted list, halving the search interval each step.
     - Complexity: **O(log n)** time, with each recursive call reducing the range by half.
     - Paradigm: *Binary divide-and-conquer*; efficient search illustration.

## Summary of Complexity

| Algorithm             | Time Complexity | Space Complexity | Notes                        |
|-----------------------|-----------------|------------------|------------------------------|
| Stack operations      | O(1)            | O(n) (storage)   | Constant-time methods        |
| Factorial             | O(n)            | O(n) (call stack)| Linear recursion             |
| Fibonacci (naive)     | O(2^n)          | O(n)             | Exponential recursion        |
| Tower of Hanoi        | O(2^n)          | O(n)             | Exponential moves            |
| Binary search         | O(log n)        | O(log n)         | Logarithmic recursion        |


> The toolkit is intended as a learning aid, illustrating both efficient and inefficient recursive patterns as well as a basic ADT.
