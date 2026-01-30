import streamlit as st

st.title("Tuples and Immutability")

st.divider()
st.markdown("""
|  | MUTABLE | IMMUTABLE |
|---|---|---|
| ORDERED | list | tuple |
| UNORDERED | set | frozenset | 

""")

st.divider()
st.markdown("""
### What are *tuples*? 
            
A tuple looks just like a list, except we use parentheses `()` instead of square brackets `[]`.   
The individual elements of a tuple can be accessed using each item's index.  

The tuples are technically defined by the presence of a comma `,`; the parentheses make them look more readable and neater.   
_To define a tuple with just one element, we need to include a trailing comma. Without it, it'd just be an `int` type._
""")
code_tup = '''
a = 3
b = 3,

print(type(a), type(b))

a1, b1 = (3), (3,)
print(type(a1), type(b1))

print(b == b1)
'''
st.code(code_tup, language="python")

st.divider()
st.markdown("""
Output:   
`<class 'int'> <class 'tuple'>`   
        
`<class 'int'> <class 'tuple'>`   
            
`True`   
            
---

### More Facts about Tuples
- A tuple can have heterogeneous elements.   
- We can loop over all the values of a tuple using a loop.     
- Once defined, the elements of a tuple can be accessed, but cannot be changed or modified in place. Although we can assign new values to a variable that represents a tuple.
""")
code_tup2 = '''
a = ("hi", 3, 40.0)
print(a, type(a))

demo_tuple = (100, 200, 300, 400)
for item in demo_tuple:
    print(item)

print(demo_tuple[3])

try: 
    demo_tuple[2] = 150     # TypeError
except Exception:
    print("'tuple' object does not support item assignment")

demo_tuple = ("new", "tuple", "values")
print(demo_tuple)
demo_tuple = ({2: 'hi'}, {3: 'new'})
print(demo_tuple)
'''
st.code(code_tup2, language="python")
st.markdown("""
Output:   
`('hi', 3, 40.0) <class 'tuple'>`    

`100`   
`200`   
`300`   
`400`   
            
`400`   
            
`'tuple' object does not support item assignment`

`('new', 'tuple', 'values')`   
`({2: 'hi'}, {3: 'new'})`  

_The tuple is immutable, but it can contain mutable objects._
""")

st.divider()
st.markdown("""
### Tuple Unpacking

Tuples are heavily used for unpacking values into multiple variables.
This is one of the most Pythonic features.
""")
code_unpack = '''
point = (10, 20)
x, y = point
print(x, y)

a, b, *rest = (1, 2, 3, 4, 5)
print(a, b, rest)

# swapping values
x, y = y, x
print(x, y)
'''
st.code(code_unpack, language="python")
st.markdown("""
Output:   
`10 20`   
            
`1 2 [3, 4, 5]`   
            
`20 10`  
""")

st.divider()
st.markdown("""
### Common Tuple Operations

- **Basic Operations**:   
        - `len()` –> returns the number of items in the tuple
        - for homogeneous, numeric tuples:   
            - `min() / max()` –> returns the smallest / largest element
            - `sum()` –> returns the sum of numeric elements            
""")
code_basic = '''
demo_tup = ("hi", "people", 23, 4.7)
print(len(demo_tup))

num_tup = (23, 46, 29, 46.9, 17)
print(f"Max: {max(num_tup)}, Min: {min(num_tup)}")
print(f"Sum: {sum(num_tup)}")
'''
st.code(code_basic, language="python")

st.markdown("""
Output:   
`4`   

`Max: 46.9, Min: 17`   
            
`Sum: 161.9`   
              
---

- **Searching / Counting**:   
        - `.index()` –> returns the index of first occurrence
        - `.count()` –> returns the total number of occurrences of the specified element    
""")
code_search = '''
num_tup = (23, 46, 29, 23, 46.9, 17)

print(num_tup.index(23))
print(num_tup.count(23))
'''
st.code(code_search, language="python")

st.markdown("""
Output:   
`0`   
`2`  

---

- **Concatenation and Repetition**:   
        - `+` –> two tuples can be concatenated using the `+` operator
        - `*n` –> a tuple can be repeated n times using `*` operator
""")
code_concat = '''
tup1 = (23, 46, 29)
tup2 = (23, 46.9, 17)

print(tup1 + tup2)
print(tup1*2)
'''
st.code(code_concat, language="python")

st.markdown("""
Output:   
`(23, 46, 29, 23, 46.9, 17)`   
`(23, 46, 29, 23, 46, 29)`   
             
---
            
- **Membership check**:   
        - `in` –> we can check if value `in` tuple or value `not in` tuple
""")
code_memb = '''
num_tup = (23, 46, 29, 23, 46.9, 17)

print("Present" if 23 in num_tup else "Not Present")
print("Not Present" if 56 not in num_tup else "Present")
'''

st.markdown("""
Output:   
`Present`   
`Not Present`   
            
---

- **Conversion**:     
        - `list(tuple)` –> convert to list for mutability
        - `tuple(list)` –> convert list into tuple
""")
code_conversion = '''
demo_list = [3, 5, 7, 8]
demo_tuple = (2, 4, 6, 8)

new_list = list(demo_tuple)
print(new_list, type(new_list))

new_tuple = tuple(demo_list)
print(new_tuple, type(new_tuple))
'''
st.code(code_conversion, language="python")

st.markdown("""
Output:   
`[2, 4, 6, 8] <class 'list'>`   

`(3, 5, 7, 8) <class 'tuple'>`   

---
            
- **Slicing**:   
        - `tuple[start:end:step]` –> access parts of tuple
""")
code_slice = '''
num_tup = (23, 46, 29, 23, 46.9, 17)

print(num_tup[1::2])
'''
st.code(code_slice, language="python")

st.markdown("""
Output:      
`(46, 23, 17)`   
""")

st.divider()
st.markdown("""
### The Idea of Immutability
            
We have talked few times about "immutability" now. Let's understand what it actually is, and why is it important to us?   
            
Immutability means **the object itself cannot be changed after creation**.     
            
- We cannot add, remove or replace elements in an immutable object.   
- We can reassign the variable to point to a new object.   
      
Now there are one important thing to understand - the difference between an "item" and an "object".   
            
An **object** is the actual data structure created in memory.   
While an **item** is a reference to something stored **inside** that object.   
            
It is very important to understand that Immutability applies to the **object itself**, not necessarily to the items it contains.

Look at the examples for better intuition of the above statements:       
""")
code_immut = '''
t = (1, [2, 3])
print(t)

# 't' itself being a tuple is immutable, but the items it contains can be mutable
# look at t[1] - it is a list -> mutable data type

t[1].append(4)      # allowed
print(t)

try: 
    t[0] = 12       # not allowed
except TypeError:
    print("Cannot modify tuple structure")
'''
st.code(code_immut, language="python")

st.markdown("""
Output:   
`(1, [2, 3])`   
            
`(1, [2, 3, 4])`   
            
`Cannot modify tuple structure`  

_The tuple structure is immutable, but it still points to the same mutable list._ 
""")

st.divider()
st.markdown("""
### Why Immutability Matters?
            
Immutability guarantees that:   
- an object's identity stays stable   
- its internal structure does not change unexpectedly
            
This stability is **required for "hashing"**. We will learn more about hashing in the upcoming sections.
            
### A Brief Introduction to Tuple Hashability

A tuple is hashable **only if all of its elements are hashable**.
""")
code_hash = '''
print(hash((1, 2, 3)))

try:
    hash((1, [2, 3]))
except TypeError:
    print("Tuple is unhashable due to mutable element")
'''
st.code(code_hash, language="python")
st.markdown("""
Output:   
`529344067295497451`   
_The specific output integer will be different each time the program runs due to hash randomization in Python 3, but it will be consistent within a single execution_

`Tuple is unhashable due to mutable element`
""")

st.divider()
st.markdown("""
A long way to go ahead, but your pace is great. See ya in the next section.
""")