import streamlit as st

st.title("Dictionaries (Hash Maps) in Python")

st.divider()

st.markdown("""
### 📊 Dictionaries 
            
A dictionary in Python is an unordered collection of key-value pairs, where each key is unique and is used to access the corresponding value.  
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
'''
st.code(code_modify, language="python")
st.markdown("""
Output:  
`Original dictionary: {'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Mercedes'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Mercedes', 'Oscar Piastri': 'McLaren'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Lewis Hamilton': 'Ferrari', 'Oscar Piastri': 'McLaren'}`  
`{'Isack Hadjar': 'Red Bull Racing', 'Oscar Piastri': 'McLaren'}`

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
### The Hash Map Intuition

""")

st.divider()

st.markdown("""


""")

st.divider()

st.markdown("""


""")

st.divider()

st.markdown("""


""")

st.divider()

st.markdown("""


""")