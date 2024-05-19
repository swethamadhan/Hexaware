Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> a[0]=10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[0]=10
TypeError: 'tuple' object does not support item assignment
>>> a=(1,2,3,4)
>>> b=list(a)
>>> a
(1, 2, 3, 4)
>>> b
[1, 2, 3, 4]
>>> b.append(10)
>>> b
[1, 2, 3, 4, 10]
>>> b.insert(0,11)
>>> b
[11, 1, 2, 3, 4, 10]
>>> b.pop(0,1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.pop(0,1)
TypeError: pop expected at most 1 argument, got 2
>>> b.pop(0)
11
>>> b
[1, 2, 3, 4, 10]
