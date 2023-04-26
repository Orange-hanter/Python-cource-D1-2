
инкапсуляция - метод + сокрытие данныхъ
<hr>
двойное подчёркивание
**Private name mangling:** When an identifier that textually occurs in a class definition begins with two or more underscore characters and does not end in two or more underscores, it is considered a _private name_ of that class. Private names are transformed to a longer form before code is generated for them. The transformation inserts the class name, with leading underscores removed and a single underscore inserted, in front of the name. For example, the identifier `__spam` occurring in a class named `Ham` will be transformed to `_Ham__spam`. This transformation is independent of the syntactical context in which the identifier is used. If the transformed name is extremely long (longer than 255 characters), implementation defined truncation may happen. If the class name consists only of underscores, no transformation is done.

<hr>
mro - для чего было сделано
посчитать mro

<hr>
super - его достоинство

proc:
+ The attribute is dynamic and can change whenever the inheritance hierarchy is updated.
+ при линейном наследовании можно использовать как ссылку на родительский класс

cons:
+ only god nkow who will be called

<hr>

repr - str