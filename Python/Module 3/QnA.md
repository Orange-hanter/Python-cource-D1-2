manq: `for ... else` подучить
A: else часть срабатывает когда мы естественным способом (не через break) заканчиваем итерироваться


<hr>

q: как выйти из из for без break
A: `return`, использовать условие для пропуска работы, `sys.exit()`. 
Но вопрос, зачем мне это?


<hr>

q: pattern matching


<hr>

q: расширеная распаковка последовательности a,\*b,c = 1,2,3,4,5,6
A: эквивалент
```python
l = [1,2,3,4,5,6]
a, b, c = l[0], l[1:-1], l[-1]
```


<hr>

q: def, import, class 
A: определяют namespace 


<hr>

q: fucntions arguments after \\ and \*
A:  answers keept here https://peps.python.org/pep-0570/#positional-only-parameters
```python
def name(positional_only_parameters, /, positional_or_keyword_parameters,
         *, keyword_only_parameters):
```


<hr>

q: enclosinc in case of function deeps > 2
```python
def foo():
    a = 42
    print(f"foo{a}")

    def bar():

        print(f"bar{a}")

        def baz():

            nonlocal a

            a += 24

            print(f"baz{a}")

            def far():

                print(f"far{a}")

                #a = 0 # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

            far()

        baz()

    bar()

    print(f"foo{a}")
```


<hr>

q: closure definition
A: Closure in Python is an inner function object, a function that behaves like an object, that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing

<hr>

Q: Namespace vs scope
A: scope - правило 

<hr>

Q: опишите все виды аргументов
```python
def f(pos1, pos2, /, pos_r_n1, pos_r_n2 = 42, *args, keyword_o1, keyword_o2, **kwargs):
	...
```
A:
* pos1, pos2 - позиционные аргументы
* pos_r_n1, pos_r_n2 - позиционные или именованные аргументы
* args - оставшиеся позиционные аргументы
* keyword_o1,  keyword_o2 - ключевые аргументы
* kwargs - оставшиеся ключевые аргументы

Демонстрационный пример:
```python
args = [500, "text", "text2"]
f(45, 34 400, *args, keyword_o1 = 5, keyword_o2 = 4, hello="hello")
```