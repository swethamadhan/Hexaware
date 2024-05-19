Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={1,2,3,4,1)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={1,2,3,4,1}
>>> a
{1, 2, 3, 4}
>>> a.add(11)
>>> a
{1, 2, 3, 4, 11}
>>> a.update(12)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update(12)
TypeError: 'int' object is not iterable
>>> 
>>> a.remove(4)
>>> a
{1, 2, 3, 11}
>>> a.pop()
1
>>> a
{2, 3, 11}
>>> list1 = [1, 2, 3, 4]
... list2 = [1, 4, 2, 3, 5]
... alphabet_set = {'a', 'b', 'c'}
... set1 = set(list2)
... set2 = set(list1)
... set1.update(set2)
... print(set1)
... set1.update(alphabet_set)
... print(set1)
SyntaxError: multiple statements found while compiling a single statement
>>> l1=[1,2,3]
>>> l2=[4,5,6]
>>> a={"a","b","c"}
>>> s1=set(list2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s1=set(list2)
NameError: name 'list2' is not defined. Did you mean: 'list'?
