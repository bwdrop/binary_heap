#!/usr/bin/env python3

import operator

class binaryHeap:
    """
    Tas binaire
    heap est le tas. heap[1] est l'indice de l'élément à la racine
    size est la taille du tas
    comparator est l'opérateur utilisé pour ordonner le tas. Tas-max (>=) par défaut
    """
    def __init__(self, list=[], comparator=operator.ge):
        """
        Initialisation du tas binaire.
        """
        self.heap = [0] + list[:]
        self.size = len(list)
        self.comparator = comparator
        for i in range(self.size // 2, 0, -1):
            self.__percolateDown(i)
    
    def __repr__(self):
        return str(self.list())

    def __percolateUp(self, i):
        """
        Réorganise le tas de bas en haut en comparant le noeud i avec ses parents
        """
        while i // 2 > 0 and self.comparator(self.heap[i // 2], self.heap[i]) == False:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def __percolateDown(self, i):
        """
        Réorganise le tas de haut en bas en comparant le noeud i avec ses enfants
        """
        while 2 * i <= self.size:
            childToSwap = self.__highestChild(i)
            if self.comparator(self.heap[i], self.heap[childToSwap]) == True:
                return
            self.heap[i], self.heap[childToSwap] = self.heap[childToSwap], self.heap[i]
            i = childToSwap

    def __highestChild(self, i):
        """
        Pour un noeud i donné, retourne son fils avec la plus grande priorité
        """
        left = 2 * i
        right = 2 * i + 1
        if right <= self.size and self.comparator(self.heap[left], self.heap[right]) == False:
            return right
        return left

    def push(self, value):
        """
        Ajoute un élément au tas binaire
        """
        self.size += 1
        self.heap.append(value)
        self.__percolateUp(self.size)

    def pop(self):
        """
        Renvoie et retire la racine du tas
        """
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.__percolateDown(1)
        return root

    def root(self):
        return self.heap[1]

    def list(self):
        return self.heap[1:]
