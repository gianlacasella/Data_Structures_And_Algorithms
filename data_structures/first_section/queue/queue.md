# Queues
## Queues examples on C++ and Python
* [Queue on C++](queue.cpp)
* [Queue on Python](queue.py)
  
## Information

* FIFO
  
* Basic methods:
  1. Enqueue: adds element to the queue
  2. Dequeue: removes element from the queue and returns it
  3. Top/Peek: returns the first element of the queue
  4. IsEmpty: returns True if it is empty and False if it is not
  5. IsFull: returns True if it is full and False if it is not
   
* Some uses:
  1. When a resource is shared among multiple consumers
  2. When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes

* Limitations:
  1. Only elements at the head of the queue can be dequeued
  2. A new element can only be enqueued at the end of the queue
  3. Is not indexed and we can't access to every element
   
* Examples:
  1. CPU scheduling, Disk Scheduling
  2. IO Buffers, pipes, file IO