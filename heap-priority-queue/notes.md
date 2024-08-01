# heap and priority queue

## what is a priority queue
- queue that orders elements by priority
- reads return the element with the "best" current priority

## what is a heap
- implementation of a priority queue structured as a binary tree
- elements are ordered upon insertion and deletion

## what is the difference
- priority queue is the concept of what a data structure with this behaviour would look like
- heap is a possible implementation of a priority queue

## heapsort
heapsort is the algorithm used to maintain ordering upon inserting or extracting an item in a heap. it consists of two operations: sift up and sift down.

first consider the heap values stored in an array so that traversal is possible through an index.

index = current node
2 * index + 1 = left child
2 * index + 2 = right child
(index - 1) // 2 = parent

sift up consists of traversing the heap upwards checking if swaping the current node for the parent node satisfies the heap condition until it does. comparison may vary depending on which kind of heap is being used (max heap, min heap).

sift down consist of traversing the heap downwards in a similiar fashion, checking for smaler/larger children depending on the kind of heap.

when building a heap from an unordered array, start from the end of the array and aplly siftdown, since there are more elements at the bottom of a tree than at the top.

## heapify
heapify consists of applysing the heapsort in a hep so that the heap property is guaranteed/recovered.