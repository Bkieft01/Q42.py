Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Brenna Q42
>>> def hash_spam(string):
...     index=0
...     total=0
...     while index<len(string):
...         if string[index]=="#":
...             total+=1
...             index+=1
...         else:
...             index+=1
...     if total>=4:
...         print("this tweet will be considered as a spam")
...     else:
