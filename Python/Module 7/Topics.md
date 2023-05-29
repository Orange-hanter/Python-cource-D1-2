
- multitasking, concurrency vs parallelism 
- thread vs process definition, detailed compete comparison list, pros/cons, how all of this in Python, cpu-bound vs IO bound task s
- sync primitives in Python threading(multiprocessing) module usage: Lock, Condition etc. usage/use cases, deadlocks, race condition 
- IPC in Python in multiprocessing module, multiprocessing.Managers, picklable object 
- what is GIL, how GIL works internally (see also [https://dabeaz.com/python/UnderstandingGIL.pdf](https://dabeaz.com/python/UnderstandingGIL.pdf "https://dabeaz.com/python/UnderstandingGIL.pdf")) 
- garbage collector: 2 parts of it, GC generations, gc module overview

### Task 
Image - Write a Python script `my_thread_sync.py` which will have two threads (apart from main thread) printing numbers from 1 to 100 (inclusively).    
The first thread must print only even numbers, the second thread must print only odd numbers. They must print numbers one after another so you will get correct sequence:

```bash
python my_thread_sync.py    
1    
2    
3    
4    
5  
#etc.
```
