Стандартный интерпретатор питона (CPython) использует сразу два алгоритма, подсчет ссылок и generational garbage collector (далее GC), более известный как стандартный [модуль gc](https://docs.python.org/3.6/library/gc.html) из Python.

недостаток механизма подсчёта ссылок - неспособность разрешать циклические ссылки






# source

[[https://habr.com/ru/articles/417215/]]

[[https://devguide.python.org/internals/garbage-collector/index.html#collecting-the-oldest-generation]]
