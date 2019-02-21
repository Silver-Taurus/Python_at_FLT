#! /usr/bin/env python3

''' Python script for providing little info about multi-threading in python '''
import threading
import os

# In computing, a process is an instance of a computer program that is being executed.
# Any process has 3 basic components:
#   --> An executable program
#   --> The associated data needed by the program (variables, workspace, buffers, etc.)
#   --> The execution context of the program (State of process).

# A thread is an entity within a process that can be scheduled for execution. Also, it is
# the smallest unit of processing that can be performed in an OS.
# In simple words, a thread is a sequence of such instructions within a program that can be
# executed independently of other code.

# A thread contains all this information in a Thread Control Block (TCB):
#   --> Thread Identifier: Unique id (TID) is assigned to every new thread.
#   --> Stack pointer: Points to thread's stack in the process. Stack contains the
#                      local variables under thread's scope.
#   --> Program counter: A register which stores the address of the instruction
#                        currently being executed by thread.
#   --> Thread state: It can be running, ready, waiting, start or done.
#   --> Thread's register state: Registers assigned to thread for computations.
#   --> Parent process Pointer: A pointer to the Process control block (PCB) of the
#                               process that the thread lives on.


# Multi-threading
# Multiple threads can exist within one process where:
#   --> Each thread contains its own register set and local variables (stored in stack).
#   --> All thread of a process share global varaiables (stored in heap) and the program code.

# Multi-threading is defined as the abiltiy of a processor to execute multiple threads concurrently.

# In a simple, single-core CPU, it is achieved using frequent switching between threads. This is
# termed as Context Switching. In context switching the state of a thread is saved and state of
# another thread is loaded whenever any interrupt (due to i/o or manually set) takes place.
# Context Switching takes place so frequently that all threads appear to be running parallely,
# this is termed as Multi-Tasking.


# In Python, the threading module provides a very simple and intutive API for spawing multiple
# threads in a program.


# Example-1:
def print_cube(num):
    ''' function to print cube of given number '''
    print('Cube: {}'.format(num**3))

def print_square(num):
    ''' function to print square of given number '''
    print('Cube: {}'.format(num**2))


if __name__ == '__main__':
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    
    # both threads completely executed
    print('Done')

# Let's try to understand the above code:
#   --> To import the threading module, we do:
#           import threading
#   --> To create a new thread, we create an object of class Thread class. It takes the following
#       arguments:
#           - target: the function to be executed by thread
#           - args: the arguments to be passed to the target function.
#       In above example, we created 2 threads with different targer functions:
#           t1 = threading.Thread(target=print_square, args=(10,))
#           t2 = threading.Thread(target=print_cube, args=(10,))
#   --> To start a thread, we use start method of Thread class.
#           t1.start()
#           t2.start()
#   --> Once a thread start, the current program also keeps on executing. In order to stop execution
#       of current program until a thread is complete, we use join method.
#           t1.join()
#           t2.join()
#       As a result, the current program will first wait for the completion of t1 and t2. Once, they
#       are finished, the remaining statements of current program are executed.


# Example-2: Python program to illustrate the concept of threading
def task1():
    print('Task1 assigned to thread: {}'.format(threading.current_thread().name))
    print('Id of process running tasks 1: {}'.format(os.getpid()))

def task2():
    print('Task1 assigned to thread: {}'.format(threading.current_thread().name))
    print('Id of process running tasks 2: {}'.format(os.getpid()))


if __name__ == '__main__':
   
    # print id of current process
    print('Id of process running main program: {}'.format(os.getpid()))
    
    # print name of main thread
    print('Main thread name: {}'.format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()

# Let us try to understand the above code:
#   --> We use os.getpid() function to get ID of current process.
#           print("ID of process running main program: {}".format(os.getpid()))
#       As it is clear from the output, the process ID remains same for all threads. 
#   --> We use threading.main_thread() function to get the main thread object. In normal
#       conditions, the main thread is the thread from which the Python interpreter was
#       started. name attribute of thread object is used to get the name of thread.
#           print("Main thread name: {}".format(threading.main_thread().name))
#   --> We use the threading.current_thread() function to get the current thread object.
#           print("Task 1 assigned to thread: {}".format(threading.current_thread().name))



# Synchronization between Multiple Threading
#   - Thread synchronization is defined as a mechanism which ensures that two or more concurrent
#   threads do not simultaneously execute some particular program segment. 