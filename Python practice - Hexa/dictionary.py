Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={"name":"emc"}
>>> a
{'name': 'emc'}
>>> a["name"]
'emc'
>>> a={"name":"emc","age":1,"loc":"trk","stud":["swe","pat"]}
>>> a
{'name': 'emc', 'age': 1, 'loc': 'trk', 'stud': ['swe', 'pat']}
>>> a.keys()
dict_keys(['name', 'age', 'loc', 'stud'])
>>> a.values()
dict_values(['emc', 1, 'trk', ['swe', 'pat']])
>>> a["age"]=2
>>> a
{'name': 'emc', 'age': 2, 'loc': 'trk', 'stud': ['swe', 'pat']}
>>> a["color"]="red"
>>> a
{'name': 'emc', 'age': 2, 'loc': 'trk', 'stud': ['swe', 'pat'], 'color': 'red'}
>>> a.update({"loc":"san"})
>>> a
{'name': 'emc', 'age': 2, 'loc': 'san', 'stud': ['swe', 'pat'], 'color': 'red'}
>>> a.pop("age")
2
>>> a
{'name': 'emc', 'loc': 'san', 'stud': ['swe', 'pat'], 'color': 'red'}
>>> del a["loc"]
>>> a
{'name': 'emc', 'stud': ['swe', 'pat'], 'color': 'red'}
>>> a.clear()
>>> a
{}
