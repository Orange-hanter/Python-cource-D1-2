[4/18 3:37 PM] Mikhail Campos-Guadamuz

Topic python TODO:  
- @contextlib usage from cintextlib  
- decorators: usage, decorators with args, nested decorators, functools std module (partial, wraps, update_wrapper)  
- modules and packages: usage, how import works step by step(!) 3-4 steps, packages usage, relative imports, from ... as keywords, implicit namespace packages vs regular package

Task:

>  Write class Pushd supporting context manager protocol, working as of pushd/popd from Bash (see [https://en.wikipedia.org/wiki/Pushd_and_popd](https://en.wikipedia.org/wiki/Pushd_and_popd "https://en.wikipedia.org/wiki/pushd_and_popd"))

Task:

> Write the python code with the following requirements to be met: 
> 
>  a) write function which return sum of 2 int arguments, annotate args, write function docstring   
>   b) write 'double decorator', which returns function which doubles the return value of input_function   
>   c) write wraps2 function the similar as functools.wraps, with the following diffs:   
>      1) only match __annotations__, and __docs__ and no other attributes;   
>      2) in wraps2, perform additional logging print to stdout indicating wrapped function name and it's id   
>   d) rewrite (b) applying (c), so that decoration of function (a) with (b) preserves   
>      original attributes described in (c), test results

Examples to study:  

Pushd and popd

In computing, pushd and popd are commands used to work with the command line directory stack. They are available on command-line interpreters such as 4DOS

  

[4/18 3:37 PM]

Mikhail Campos-Guadamuz pinned a message.

  

[4/18 3:49 PM] Mikhail Campos-Guadamuz

кстати да, вот так я хотел показать касательно последнего примера, когда весь try лежит в блоке while и есть break

> def divide(x, y):   
>     while True:   
>         try:   
>             result = x / y   
>         except Exception as ex:   
>             raise   
>         finally:   
>             print("executing finally clause from divide()")   
>             break   
>   
> divide(2, 'kolobok')


[4/18 3:50 PM] Mikhail Campos-Guadamuz

такой ещё посмотри к той же опере

> def divide(x, y):   
>         try:   
>             return 0  
>         finally:   
>             return 1
