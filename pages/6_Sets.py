import streamlit as st

st.title("Sets in Python")

st.divider()

st.markdown("""
### Sets Overview - Hash-Based Collections  

        Lists ––> ordered containers   
        Dictionaries ––> key-value mappings   
        Sets ––> keys without values   
A set is basically a dictionary where the values do not matter.

A set is an unordered collection of unique elements (meaning the order of elements is not retained), where each element must be **hashable (typically immutable)**.   
It can be created using `set()`, with items separated by commas.   
_Note that `{}` creates an empty dictionary, not an empty set._

Which implies,    
- sets reinforce hashing i.e. **set elements must be immutable**.   
- as dictionaries were used for fast lookup, sets are used for **fast membership check**.   
- it contains unique elements only.   
- **No indexing or slicing**:   
        - sets do not support indexing (`s[0]`), because elements are unordered   

""")
code_set = '''
# creating a set
s = {1, 2, 3}   # method 1
print(s)

s = set()       # method 2
print(s)

s = {"apple", "zebra", "poor", "beatles", "zinc"}
print(s)      # the order is not retained

s = {10, 20, 30}
# print(s[0])   # TypeError
'''
st.code(code_set, language="python")

st.markdown("""
Output:   
`{1, 2, 3}`   
`set()`    
`{'poor', 'apple', 'zinc', 'beatles', 'zebra'}`   
`TypeError`        
""")

st.info("""
#### What Exactly is mutable in a set?
        
As I said earlier, set elements have to be immutable. But, as a fact, _set objects_ are unhashable, meaning 'set' is mutable.  
WHAT????? Confused, right??? I too, was.   
        
But let me clear up the fog.
        
**A set is unhashable because its contents can change, not because its elements are mutable.**
""")
            
st.divider()

st.markdown("""
### Core Set Operations
            
- **add**:   
        - adds new elements to a set
""")
code_add = '''
s = {1, 2, 3}
print(f"Original set: {s}")

s.add(4)
print(f"After addition: {s}")

s.add(2)    # duplicate element
print(f"After adding duplicate: {s}")
'''
st.code(code_add, language="python")

st.markdown("""
Output:
`Original set: {1, 2, 3}`   
`After addition: {1, 2, 3, 4}`   
`After adding duplicate: {1, 2, 3, 4}`   
Sets automatically ignore duplicates, and no error is raised when adding an existing element.

---
            
- **remove**:  
        - removes the element, but if the element is missing, it raises error

- **discard**:   
        - removes the element and does nothing if element is missing        
""")
code_removal = '''
s = {"apple", "banana", "kiwi", "grape"}

s.remove("banana")
print(s)

s.discard("kiwi")
print(s)

s.discard("dragonfruit")
print(s)

try:
    s.remove("orange")      # KeyError
except KeyError:
    print("Key not found")
'''
st.code(code_removal, language="python")

st.markdown("""
Output:   
`{'apple', 'grape', 'kiwi'}`   
`{'apple', 'grape'}`   
`{'apple', 'grape'}`   
`Key not found`   

---

- **membership (in)**:   
        - checks if an element exists in the set       
""")
code_mem = '''
visited = {"zoo", "palace", "lake"}
print("zoo" in visited)
print("beach" in visited)
'''
st.code(code_mem, language="python")

st.markdown("""
Output:   
`True`   
`False`

---            

- **iteration**:   
        - we can iterate over the set element-wise.
""")
code_iter = '''
teams = {"Mercedes", "Williams", "Audi"}

for team in teams:
    print(team)
'''
st.code(code_iter, language="python")
st.markdown("""
Output:   
`Audi`               
`Mercedes`   
`Williams`   
_Order is never guaranteed._
""")

st.divider()

st.markdown("""
### Set Algebra
            
Set algebra lets us compare, combine, and reason about relationships between groups of elements.
- **Union (|)**:   
        - merges unique values
            
- **Intersection (&)**:   
        - returns common items
            
- **Difference (-)**:   
        - used for filtering or removing exclusions
        - returns elements present in the first set but not the second
            
- **Symmetric Difference (^)**:  
        - returns elements present in either set, but not both
""")
code_basic_ops = '''
a, b = {1, 2, 3}, {3, 4, 5}

# Union
print(a | b)
print(a.union(b))

# Intersection
print(a & b)
print(a.intersection(b))

# Difference
print(a - b)
print(a.difference(b))

# Symmetric Difference
print(a ^ b)
print(a.symmetric_difference(b))
''' 
st.code(code_basic_ops, language="python")

st.markdown(""" 
Output:   
`{1, 2, 3, 4, 5}`   
`{1, 2, 3, 4, 5}`   
            
`{3}`  
`{3}`  
            
`{1, 2}`  
`{1, 2}`  
            
`{1, 2, 4, 5}`  
`{1, 2, 4, 5}`  

---
            
- **In-place Set Operations (Mutations)**   
- **Subset, Superset & Disjoint Set**   
        - these are logical relationship checks, not algebra.   
        - **subset** checks if one set is a subset to the other   
        - **superset** checks if one set contains the other set   
        - **disjoint** checks if the two given sets have any common elements.   

- **Frozen Sets**  
        - a frozenset is an immutable set, meaning its elements cannot be changed, added, or removed after it is created.   
        - the name `frozenset` highlights that the collection of elements is "frozen" in time once initialized
""")
code_more_ops = '''
a, b = {1, 2, 3}, {3, 4, 5}

# Mutations
# Each operation mutates a, so its value carries forward.
a |= b; print(a)        # Input: a = {1, 2, 3}
a -= b; print(a)        # Input: a = {1, 2, 3, 4, 5}
a &= b; print(a)        # Input: a = {1, 2}
a ^= b; print(a)        # Input: a = set() / {}

# ---------------------
a, b = {1, 2}, {1, 2, 3}

# Subset
print(a.issubset(b))

# Superset
print(b.issuperset(a))

# Disjoint
y = {3, 4}
print(a.isdisjoint(b))
print(a.isdisjoint(y))

# ---------------------
fs = frozenset([1, 2, 3])
print(fs)
try:
        fs.add(4)    # AttributeError
except Exception:
        print("Cannot add elements")

try:
        d = {
        {1, 2}: "a",
        {3, 4}: "b"
        }
except Exception:
        print("cannot use 'set' as a dict key, as it is unhashable")

d = {
frozenset({1, 2}): "group A",
frozenset({3, 4}): "group B"
}
print("This is valid")
print(d)
'''
st.code(code_more_ops, language="python")
st.markdown("""
Output:   
`{1, 2, 3, 4, 5}`   
`{1, 2}`  
`set()`  
`{3, 4, 5}`   

`True`   
            
`True`  
             
`False`   
`True`   
            
`frozenset({1, 2, 3})`  
`Cannot add elements`    
            
`cannot use 'set' as a dict key, as it is unhashable`   
`{frozenset({1, 2}): 'group A', frozenset({3, 4}): 'group B'}`   
""")

st.divider()
st.info('''
Sets are heavily used in algorithms for:
- visited tracking (graphs, DFS/BFS)
- duplicate elimination
- fast membership checks (O(1) average)
''')

st.divider()
st.markdown("""
#### Sets help us reason about presence, absence, overlap and exclusivity. They pair naturally with dictionaries and are foundational for graphs and algorithms.
#### Happy Learning Ahead (Going Great Already!!)            
""")