A _scope_ defines the visibility of a name within a block. If a local variable is defined in a block, its scope includes that block. If the definition occurs in a function block, the scope extends to any blocks contained within the defining one, unless a contained block introduces a different binding for the name.

When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes visible to a code block is called the block’s _environment_.

When a name is not found at all, a [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError") exception is raised. If the current scope is a function scope, and the name refers to a local variable that has not yet been bound to a value at the point where the name is used, an [`UnboundLocalError`](https://docs.python.org/3/library/exceptions.html#UnboundLocalError "UnboundLocalError") exception is raised. [`UnboundLocalError`](https://docs.python.org/3/library/exceptions.html#UnboundLocalError "UnboundLocalError") is a subclass of [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError").

If a name binding operation occurs anywhere within a code block, all uses of the name within the block are treated as references to the current block. This can lead to errors when a name is used within a block before it is bound. This rule is subtle. Python lacks declarations and allows name binding operations to occur anywhere within a code block. The local variables of a code block can be determined by scanning the entire text of the block for name binding operations. See [the FAQ entry on UnboundLocalError](https://docs.python.org/3/faq/programming.html#faq-unboundlocalerror) for examples.

If the [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) statement occurs within a block, all uses of the names specified in the statement refer to the bindings of those names in the top-level namespace. Names are resolved in the top-level namespace by searching the global namespace, i.e. the namespace of the module containing the code block, and the builtins namespace, the namespace of the module [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace."). The global namespace is searched first. If the names are not found there, the builtins namespace is searched. The `global` statement must precede all uses of the listed names.

The [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) statement has the same scope as a name binding operation in the same block. If the nearest enclosing scope for a free variable contains a global statement, the free variable is treated as a global.

The [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement causes corresponding names to refer to previously bound variables in the nearest enclosing function scope. [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") is raised at compile time if the given name does not exist in any enclosing function scope.

The namespace for a module is automatically created the first time a module is imported. The main module for a script is always called [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.").

Class definition blocks and arguments to [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") and [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") are special in the context of name resolution. A class definition is an executable statement that may use and define names. These references follow the normal rules for name resolution with an exception that unbound local variables are looked up in the global namespace. The namespace of the class definition becomes the attribute dictionary of the class. The scope of names defined in a class block is limited to the class block; it does not extend to the code blocks of methods – this includes comprehensions and generator expressions since they are implemented using a function scope. This means that the following will fail:

```python
class A:
    a = 42
    b = list(a + i for i in range(10))
```