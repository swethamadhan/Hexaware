Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3]
a
[1, 2, 3]
a.append(4)
a
[1, 2, 3, 4]
>>> a.append(20)
>>> a
[1, 2, 3, 4, 20]
>>> a.append("Swe")
>>> a
[1, 2, 3, 4, 20, 'Swe']
>>> a.append(True)
>>> a
[1, 2, 3, 4, 20, 'Swe', True]
>>> a.append(3)
>>> a
[1, 2, 3, 4, 20, 'Swe', True, 3]
>>> print(a[2])
3
>>> a.insert(0,2,/)
SyntaxError: invalid syntax
>>> a.insert(0,2)
>>> a
[2, 1, 2, 3, 4, 20, 'Swe', True, 3]
>>> a[0]=11
>>> a
[11, 1, 2, 3, 4, 20, 'Swe', True, 3]
>>> a.pop(3)
3
>>> a
[11, 1, 2, 4, 20, 'Swe', True, 3]
>>> a.pop()
3
>>> a
[11, 1, 2, 4, 20, 'Swe', True]
>>> a.pop()
True
>>> a
[11, 1, 2, 4, 20, 'Swe']
>>> a=[11,12,13]
>>> b=[14,15,16]
>>> a.extend(b)
>>> print(a)
[11, 12, 13, 14, 15, 16]
