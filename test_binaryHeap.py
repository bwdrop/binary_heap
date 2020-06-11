#!/usr/bin/env python3

import unittest
import operator
from binaryHeap import binaryHeap

class BinaryHeapTest(unittest.TestCase):
    def test_build_maxheap(self):
        """
        Test case 01 : Contruire un tas-max à partir d'une liste

            10           40           40
           / \\         / \\         / \\
          20  40  ->   20  10  ->   30  10
         / \\         / \\         / \\
        30  5        30  5        20  5
        """
        # Given
        # When
        maxHeap = binaryHeap([10, 20, 40, 30, 5])
        # Then
        assert maxHeap.size == 5
        assert maxHeap.list() == [40, 30, 10, 20, 5]
    
    def test_build_minheap(self):
        """
        Test case 02 : Construire un tas-min à partir d'une liste

            10           10           5
           / \\         / \\         / \\
          20  40  ->   5   40  ->   10  40
         / \\         / \\         / \\
        30  5        30  20       30  20
        """
        # Given
        # When
        minHeap = binaryHeap([10, 20, 40, 30, 5], operator.le)
        # Then
        assert minHeap.size == 5
        assert minHeap.list() == [5, 10, 40, 30, 20]
    
    def test_pop_binaryHeap(self):
        """
        Test case 03 : Retirer le max du tas binaire

            50          30          40
           / \\        / \\        / \\
          20  40  ->  20  40  ->  20  30
         / \\ / \\   / \\ /      / \\ /
        5  10 15 30  5 10 15    5  10 15
        """
        # Given
        binHeap = binaryHeap([50, 20, 40, 5, 10, 15, 30])
        # When
        max = binHeap.pop()
        # Then
        assert max == 50
        assert binHeap.list() == [40, 20, 30, 5, 10, 15]

    def test_push_binaryHeap(self):
        """
        Test case 04 : Ajouter des éléments au tas binaire

        10       20       20         42         60         60
                /        / \\       / \\       / \\       / \\
           ->  10   ->  10  5  ->  20  5  ->  42  5  ->  42  30
                                  /          / \\       / \\ /
                                 10         10 20      10 20 5
        """
        # Given
        binHeap = binaryHeap()
        # When
        binHeap.push(10)
        binHeap.push(20)
        binHeap.push(5)
        binHeap.push(42)
        binHeap.push(60)
        binHeap.push(30)
        # Then
        assert binHeap.size == 6
        assert binHeap.list() == [60, 42, 30, 10, 20, 5]

    def test_heap_sort(self):
        """
        Test case 05 : Tri par tas avec un tas binaire

            1          2          3          4          5     6
           / \\       / \\       / \\       / \\       /
          3   2  ->  3   5  ->  4   5  ->  6   5  ->  6  ->
         / \\ /     / \\       /
        6  4 5     6  4       6

        -> [   1,       2,       3,       4,       5,       6   ]
        """
        # Given
        minHeap = binaryHeap([3, 1, 2, 6, 4, 5], operator.le)
        sorted = []
        # When
        while minHeap.size > 0:
            sorted.append(minHeap.pop())
        # Then
        assert sorted == [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
    unittest.main()
