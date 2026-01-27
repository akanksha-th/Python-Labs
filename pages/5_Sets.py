import streamlit as st

st.title("Sets in Python")

st.divider()

st.markdown("""
### Sets Overview - Hash-Based Collections  

        Lists ––> ordered containers   
        Dictionaries ––> key-value mappings   
        Sets ––> keys without values   
A set is basically a dictionary where the values do not matter.

A set is an unordered collection (meaning the order of elements is not retained) of unique, immutable elements. It can be created using `set()` or using curly brackets `{}`, with items separated by commas.
            
Which implies, 
    - sets reinforce hashing i.e. **set elements must be immutable**.   
    - as dictionaries were used for fast lookup, sets are used for **fast membership check**.   
    - it contains unique elements only.
""")
code_set = '''
# creating a set
s = {1, 2, 3}   # method 1
print(s)

s = set()       # method 2
print(s)

s = {"apple", "zebra", "poor", "beatles", "zinc"}
print(s)      # the order is not retained
'''
st.code(code_set, language="python")

st.markdown("""
Output:   
`{1, 2, 3}`   
`set()`    
`{'poor', 'apple', 'zinc', 'beatles', 'zebra'}`      
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
      
""")