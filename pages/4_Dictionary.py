import streamlit as st

st.title("Dictionaries (Hash Maps) in Python")

st.divider()

st.markdown("""
### 📊 Dictionaries 
            
A dictionary in Python is a collection of key-value pairs, where each key is unique and is used to access the corresponding value.
Dictionaries preserve insertion order, but their conceptual behavior does not rely on order. (See example for better understanding.)   
Dictionaries are defined using curly braces `{}`, with each key-value pair separated by a colon `:` and pairs separated by commas.
We can create an empty dictionary with an empty set of braces`{}` or using the built-in `dict()` function.
            
For example:
""")
code_dict = '''
emp_dict1 = {}
emp_dict2 = dict()
print(emp_dict1, emp_dict2)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 3, "a": 1, "b": 2}

print(dict1)
print(dict2)
print(dict1 == dict2)  # Order doesn't matter in dictionaries
'''
st.code(code_dict, language="python")
st.markdown("""
Output: 
`{} {}`

`{'a': 1, 'b': 2, 'c': 3}`  
`{'c': 3, 'a': 1, 'b': 2}`             
`True`
            
---
            
### Dictionary Operations
            
- **Accessing Values** –>
        - We can access the values in a dictionary using the keys.  
        - `.get()` –> we pass in the key as an argument to access the value, and if the key is not found, instead of throwing an error, it returns None or a default value if specified  
        - `.keys()` –> returns all the keys in the dictionary.  
        - `.values()` –> returns all the values in the dictionary.  
        - `.items()` –> returns all the key-value pairs in the dictionary as tuples.  
""")
st.info("""
_.keys()_, _.values()_, _.items()_ present us the **view** of the dictionary and dictionary views are **dynamic**, meaning they are  not static snapshots of the data; they are live, real-time reflections of the underlying dictionary.   
if the dictionary changes, the view also changes.
        
##### **What even is a "view"?**

A view is just like a window. Assume that you're at a hillstation, and you're looking outside from a window.  
Whatever is outside can be accessed (seen) at any time, with the help of the window. That's the essence of it.
        
#### **How is a view different from a copy?**
        
A view gives us the real time access, but a copy is like a snapshot.  
Using the previous analogy, if you take a picture of the scenery from your window, it is a copy. No matter, if the outside scenery changes, the picture has that one moment captured. 
That's where lies all the difference.
""")
code_access = '''
my_dict = {"Isack Hadjar": "Red Bull Racing", "Kimi Antonelli": "Mercedes"}
print(my_dict["Kimi Antonelli"])   
print(f"In 2026, Isack Hadjar is driving for {my_dict['Isack Hadjar']}")   

print(my_dict.get("Lewis Hamilton"))   
print(my_dict.get("Lewis Hamilton", "No value assigned."))

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
'''
st.code(code_access, language="python")
st.markdown("""
Output:  
`Mercedes`  
`In 2026, Isack Hadjar is driving for Red Bull Racing`  
            
`None`  
`No value assigned.`  

`Keys: dict_keys(['Isack Hadjar', 'Kimi Antonelli'])`  
`Values: dict_values(['Red Bull Racing', 'Mercedes'])`  
`Items: dict_items([('Isack Hadjar', 'Red Bull Racing'), ('Kimi Antonelli', 'Mercedes')])`  

---

- **Modifying Values** –>
        - A new item can be added or an existing item can be modified by specifying the key and assigning a value to it.  
        - `del` keyword –> permanently removes an item from the dictionary using its key  
        - `pop` –> if exists, it returns the value against the provided key. If the key does not exist, we can provide None value along with it it, to avoid `KeyError`
        - `popitem()` –> it removes the last inserted item
""")
code_modify = '''
my_dict = {"Isack Hadjar": "Red Bull Racing", "Lewis Hamilton": "Mercedes"}
print(f"Original dictionary: {my_dict}")

my_dict["Oscar Piastri"] = "McLaren"
print(my_dict)

my_dict["Lewis Hamilton"] = "Ferrari"
print(my_dict)

del my_dict["Lewis Hamilton"]
print(my_dict)

my_dict["Yuki Tsunoda"] = "Red Bull Racing"
print(my_dict.pop("Yuki Tsunoda"))     
print(my_dict.pop("Max Verstappen", None))     

print(my_dict.popitem())
print(my_dict)
'''
st.code(code_modify, language="python")
st.markdown("""
Output:  
`Original dictionary: {'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Mercedes'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Mercedes', 'Oscar Piastri': 'McLaren'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Ferrari', 'Oscar Piastri': 'McLaren'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Oscar Piastri': 'McLaren'}`

`Red Bull Racing`   
`None`   
            
`('Oscar Piastri', 'McLaren')`   
`{'Isack Hadjar': 'Red Bull Racing'}`   
--- 
            
- **Looping through all key-value pairs** –>
""")
code_loop = '''
my_dict = {"Isack Hadjar": "Red Bull Racing", "George Russell": "Mercedes", "Kimi Antonelli": "Mercedes", "Oscar Piastri": "McLaren"}
for driver, team in my_dict.items():
    print(f"{driver} drives for {team}")

for driver in sorted(my_dict.keys()):
    print(driver)

for team in set(my_dict.values()):
    print(team)
'''
st.code(code_loop, language="python")
st.markdown("""
Output:  
`Isack Hadjar drives for Red Bull Racing`  
`George Russell drives for Mercedes`  
`Kimi Antonelli drives for Mercedes`  
`Oscar Piastri drives for McLaren`  
            
`George Russell`  
`Isack Hadjar`  
`Kimi Antonelli`  
`Oscar Piastri`   
            
`Red Bull Racing`  
`Mercedes`  
`McLaren`  
""")

st.divider()

st.markdown("""
### Dictionary Comprehensions
            
Just an elegant way to create a dictionary. The basic syntax to create a dictionary comprehension is a single line of code enclosed in curly brackets `{}`.
""")
code_comp = '''
nums = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in nums if x%2 == 0}

print(squares)
'''
st.code(code_comp, language="python")
st.markdown("""
Output:   
        `{2: 4, 4: 16}`   
""")

st.divider()

st.markdown("""
### Nesting
            
The core idea of nesting is pretty simple, if you start seeing a data type as a **container**.  
Here, anything that is allowed to exist as a value in Python can be stored inside a dictionary. 
This may include other dictionaries, lists, sets, tuples, and even custom objects. And this is the foundational concept of **nesting**. It is just containers inside containers.
            
- **A List of Dictionaries** –>  
        - We use a list of dictionaries to store many objects of the same type, where each dictionary represents one object.

For example:""")
code_nest1 = '''
drivers = [
    {"name": "Isack Hadjar", "team": "Red Bull Racing", "number": 6},
    {"name": "Kimi Antonelli", "team": "Mercedes", "number": 12},
    {"name": "Oscar Piastri", "team": "McLaren", "number": 81}
]'''
st.code(code_nest1, language="python")

st.info("""
**Why this matters?**

This structure is how:
        
    - JSON APIs work
    - databases return rows
    - ML datasets are often structures/represented
""")

st.markdown("""
- **A List in a Dictionary** –>  
        - It is used when one category holds multiple items.
            
For example:""")
code_nest2 = '''
drivers = {
    "Red Bull Racing": ["Isack Hadjar", "Liam Lawson"],
    "Mercedes": ["Kimi Antonelli", "George Russell"],
    "McLaren": ["Oscar Piastri", "Lando Norris"]
}
'''
st.code(code_nest2, language="python")

st.markdown("""
- **A Dictionary in a Dictionary** –>  
        - This represents hierarchical relationships.

For example:
""")
code_nest3 = '''
drivers = {
    "Isack Hadjar": {"team": "Red Bull Racing", "number": 6},
    "Kimi Antonelli": {"team": "Mercedes", "number": 12},
    "Oscar Piastri": {"team": "McLaren", "number": 81}
}
'''
st.code(code_nest3, language="python")

st.info("""
**Why this matters?**
        
This structure is how:
        
    - JSON responses are nested
    - configuration files are structured
    - complex data models are represented
""")

st.divider()

st.markdown("""
### Advanced Dictionary Operations
            
- **setdefault()** –>   
        - if the key exists, it returns the existing value and doesn't change the dictionary
        - if the key does not exist, it inserts the new key with the default value and returns the default value
        - another use case for setdefault() is grouping items in a dictionary where each key's value is a list (or other mutable type)
""")
code_setdefault = '''
d = {"name": "Tom Riddle"}
name = d.setdefault("name", "Voldemort")
print(f"Name: {name}")
print(f"Dictionary: {d}")

age = d.setdefault("age", "21")
print(f"Age: {age}")
print(f"Dictionary: {d}")

d.setdefault("roll_number", []).append(103)
d.setdefault("roll_number", []).append(221)
print(f"Dictionary: {d}")

demo_data = [("a", 1), ("b", 2), ("a", 3), ("c", 3)]
grouped_data = {}
for k, v in demo_data:
    grouped_data.setdefault(k, []).append(v)
print(f"Grouped Data: {grouped_data}")
'''
st.code(code_setdefault, language="python")
st.markdown("""
Output:  
            `Name: Tom Riddle` 
            `Dictionary: {'name': 'Tom Riddle'}`   

            `Age: 21`
            `Dictionary: {'name': 'Tom Riddle', 'age': '21'}`   

            `Dictionary: {'name': 'Tom Riddle', 'age': '21', 'roll_number': [103, 221]}`   

            `Grouped Data: {'a': [1, 3], 'b': [2], 'c': [3]}`   
""")
st.info("""
### setdefault() vs get() 

*_setdefault()_* modifies the dictionary by adding the key-value pair if the key is missing,   
while *_get()_* only returns a default value without modifying the dictionary        
""")

st.markdown("""
- ** frequency map ** –>   
        - using .get() function   
        - using collections.Counter –> specifically designed for counting hashable objects   
        - using collections.defaultdict –> automatically initializes new keys with a default value (e.g., 0 for an int) when they are first accessed, eliminating the need to check if a key exists   
        - using explicit checking   
""")
code_freq_map = '''
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# method 1: .get()
freq = {}
for fruit in fruits:
    freq[fruit] = freq.get(fruit, 0) + 1
print(f"Freq Map: {freq}")

# method 2
from collections import Counter
freq_map = Counter(fruits)
print(freq_map)
print(f"Freq Map: {dict(freq_map)}")

# method 3
from collections import defaultdict
freq_map = defaultdict(int)
for fruit in fruits:
    freq_map[fruit] += 1
print(f"Freq Map: {freq_map}")

# method 4: explicit checking
freq_map = {}
for fruit in fruits:
    if fruit in freq_map:
        freq_map[fruit] += 1
    else:
        freq_map[fruit] = 1
print(f"Freq Map: {freq}")
'''
st.code(code_freq_map, language="python")

st.markdown("""
Output:   
        `Freq Map: {'apple': 2, 'banana': 3, 'orange': 1}`   
            
        `Counter({'banana': 3, 'apple': 2, 'orange': 1})`   
        `Freq Map: {'apple': 2, 'banana': 3, 'orange': 1}`   
            
        `Freq Map: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})`   
            
        `Freq Map: {'apple': 2, 'banana': 3, 'orange': 1}`   

--- 

- ** Dictionary Merging ** –>   
        - update()   
        - **|** (Union) operator –> cleaner than update() in Python   
        
""")
code_dict_merge = '''
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 1, "c": 4}

# method 1
merged_dict = dict1 | dict2
print(merged_dict)

# method 2
merged_dict = {**dict1, **dict2}
print(merged_dict)

# updating the existing dictionary in-place
dict1.update(dict2)
print(dict1)

# OR
dict1 = {"a": 1, "b": 2}
dict2 |= dict1
print(dict2)
'''
st.code(code_dict_merge, language="python")
st.markdown("""
Output:   
        `{'a': 1, 'b': 1, 'c': 4}`   

        `{'a': 1, 'b': 1, 'c': 4}`   

        `{'a': 1, 'b': 1, 'c': 4}`   
            
        `{'b': 2, 'c': 4, 'a': 1}`
""")

st.divider()
st.markdown("""
### Some Important Points to Remember about Dictionaries
            
Dictionaries exist to solve a different kind of problem than lists. While lists are good for storing ordered collections and accessing elements by position, real-world problems require fast lookup based on a key.
For example: Looking up a driver's team by their name is much faster with a dictionary than searching through a list of drivers.
            
Internally, Python dictionaries use a concept called **_hashing_**. When a key is used, Python applies a hash function to determine where that key-value pair should be stored. 
This allows Python to jump directly to the correct location instead of searching element by element.
We will explore hashing in more detail in later sections.

Because of this underlying mechanism, dictionary lookups are usually very fast and do not typically grow slower as the dictionary gets larger.
Keys in a dictionary must be immutable. This is because once a key is hashed and placed in a location, changing the key would change its hash and break the lookup mechanism.

""")

st.divider()

st.markdown("""
#### With dictionaries, we move beyond simple sequences. 
#### I hope we're thrilled to move further, to understand more complex data structures.

""")