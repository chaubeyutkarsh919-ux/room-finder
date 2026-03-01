"""
Algorithmic Efficiency & Recursion Toolkit (AERT)

This module provides:
- A simple Stack ADT implementation.
- Recursive implementations of factorial, fibonacci, Tower of Hanoi, and binary search.
- A small demonstration in the main guard.
"""

from __future__ import annotations
from typing import List, Any, Optional


class Stack:
    """A minimal stack abstract data type using a Python list internally."""

    def __init__(self) -> None:
        self._data: List[Any] = []

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack.  Raises IndexError on empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """Return the top item without removing it.  Raises IndexError on empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def size(self) -> int:
        """Return the number of items on the stack."""
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


def factorial(n: int) -> int:
    """Return n! recursively.  Defined for n >= 0."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number using the classic recursive definition.

    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
    """
    if n < 0:
        raise ValueError("fibonacci() not defined for negative values")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def tower_of_hanoi(n: int,
                     source: str,
                     target: str,
                     auxiliary: str,
                     moves: Optional[List[str]] = None) -> List[str]:
    """Solve Tower of Hanoi recursively and optionally record moves.

    - n : number of disks
    - source, target, auxiliary : labels for pegs
    - moves : if provided, a list to which move descriptions will be appended
    """
    if moves is None:
        moves = []
    if n <= 0:
        return moves
    # move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target, moves)
    move = f"move disk {n} from {source} to {target}"
    moves.append(move)
    # move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves


def binary_search(arr: List[int], target: int, low: int = 0, high: Optional[int] = None) -> int:
    """Recursive binary search on a sorted list.

    Returns the index of target in arr or -1 if not found.
    """
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


if __name__ == "__main__":
    # demonstration of toolkit features
    print("Stack ADT demo")
    s = Stack()
    for i in range(1, 5):
        s.push(i)
    print(s, "size=", s.size())
    while not s.is_empty():
        print("popped", s.pop())
    
    print("\nFactorial and Fibonacci")
    for k in range(6):
        print(f"{k}! =", factorial(k))
        print(f"fib({k}) =", fibonacci(k))
    
    print("\nTower of Hanoi trace for n=3")
    moves = tower_of_hanoi(3, "A", "C", "B")
    for m in moves:
        print(m)
    
    print("\nBinary search examples")
    array = [1, 3, 5, 7, 9]
    for x in [7, 2]:
        idx = binary_search(array, x)
        print(f"search {x} -> {idx}")
