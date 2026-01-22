import streamlit as st

st.set_page_config(page_title="Lists", layout="wide")
st.title("📃 Lists in Python")

st.divider()

st.markdown("""
### 📚 A Brief Introduction
            
In python, lists are **a collection of items _in a particular order_**. A list can be heterogeneous, meaning it can contain items of different data types (like integers, strings, and even other lists).
You define a list using square brackets `[]`, with items separated by commas. Also, a list can have repetitive elements or no elements as well. It does not throw an error.
            
For example:
""")

code_list = '''
sample_list = [1, "hello", 3.14, True, [2, 4, 3.9, "world"]]
print(sample_list)
'''
st.code(code_list, language="python")
st.markdown("""
Output: `[1, 'hello', 3.14, True, [2, 4, 3.9, 'world']]`
            
We can access elements in a list using their `index` (which is a pythonic work for position). 
Python uses zero-based indexing, so the first item is at index `0`, the second at index `1`, and so on. And indexes range from 0 to length(sequence)-1. We will deep dive into it in the "**memory**" section.   

For example:""")
code_index = '''
print(sample_list[0])  # Accessing the first element
print(sample_list[-1])  # Accessing the last element
print(sample_list[4][2])  # Accessing the second element of the last element
print(sample_list[4][-1][4])  # Accessing the fourth element of the last element of the last element
'''
st.code(code_index, language="python")
st.markdown("""
Output:
`1`  
`[2, 4, 3.9, 'world']`  
`3.9`  
`d`
            
Yes, we can access elements using negative indices starting from -1, from the end, and also the elements of nested lists can be accessed using multiple indices.
""")

st.divider()

st.markdown("""
### 🔬 List Operations

In python, lists are dynamic and mutable, meaning they can be changed after creation. We can add, remove, or modify elements in a list.

Here are some basic list operations:
- **Modifying list elements** –>
        - In order to change an element, we just need to specift it's location.
""")
code_modify = '''motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles[0] = 'ducati' 
print(motorcycles)'''
st.code(code_modify, language="python")
st.markdown("""
Output: `['honda', 'yamaha', 'suzuki']`   
`['ducati', 'yamaha', 'suzuki']`

---
            
- **Finding length of a list** –>  
        - `len()` function –> returns the number of elements in a list

- **Adding elements to a list** –>  
        - `.append()` –> adds an element to the end of the list  
        - `.insert()` –> adds an element at a specific index and shifts every other value to the right  
        - `.extend()` –> adds elements from another list to the end of the current list   
""")
code_add = '''motorcycles = ['honda', 'yamaha', 'suzuki']
new_motorcycles = ['ducati', 'bmw']

print(f"Original length of the list: {len(motorcycles)}")

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'bmw')
print(motorcycles)

motorcycles.extend(new_motorcycles)
print(motorcycles)

print(f"New length of the list: {len(motorcycles)}")
'''
st.code(code_add, language="python")
st.markdown("""
Output: `Original length of the list: 3`  
        `['honda', 'yamaha', 'suzuki', 'ducati']`  
        `['honda', 'bmw', 'yamaha', 'suzuki']`  
        `['honda', 'bmw', 'yamaha', 'suzuki', 'ducati', 'bmw']`  
        `New length of the list: 6`  

---
            
- **Removing elements from a list** –>  
        - `del` statement –> removes an element at a specific index permanently  
        - `.pop()` –> removes the last element (or an element at a specific index) and returns it  
        - `.remove()` –> removes the first occurrence of a specific value  
""")
code_remove='''
motorcycles = ['honda', 'bmw', 'yamaha', 'suzuki', 'ducati', 'ducati', 'bmw']
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"Popped motorcycle: {popped_motorcycle}")

motorcycles.remove('ducati')
print(motorcycles)
'''
st.code(code_remove, language="python")
st.markdown("""
Output: `['bmw', 'yamaha', 'suzuki', 'ducati', 'ducati', 'bmw']`  
        `['bmw', 'yamaha', 'suzuki', 'ducati', 'ducati']`  
        `Popped motorcycle: bmw`    
        `['bmw', 'yamaha', 'suzuki', 'ducati']`  

---
                  
- **Sorting a list** –>  
        - `.sort()` –> sorts the list permanently, in ascending order by default   
        - `sorted() function` –> returns a new sorted list without modifying the original list –> it accept a reverse=True argument if you want to
display a list in reverse-alphabetical order

- **Reversing a list** –>    
        - `.reverse()` –> reverse the order of the list permanently
""")
code_sort = '''
motorcycles = ['honda', 'bmw', 'yamaha', 'suzuki', 'ducati']

print(f"Here is the sorted list: {sorted(motorcycles)}")
print(sorted(motorcycles, reverse=True))
print(f"Here is the original list: {motorcycles}")

motorcycles.sort()
print(f"Permanently sorted list: {motorcycles}")

motorcycles.reverse()
print(f"Reversed list: {motorcycles}")
'''
st.code(code_sort, language="python")
st.markdown("""
Output:  
        `Here is the sorted list: ['bmw', 'ducati', 'honda', 'suzuki', 'yamaha']`  
        `['yamaha', 'suzuki', 'honda', 'ducati', 'bmw']`  
        `Here is the original list: ['honda', 'bmw', 'yamaha', 'suzuki', 'ducati']`  
        
`Permanently sorted list: ['bmw', 'ducati', 'honda', 'suzuki', 'yamaha']`  
        
`Reversed list: ['yamaha', 'suzuki', 'honda', 'ducati', 'bmw']`    
            
""")

st.divider()

st.markdown("""
### 🧪 Working with Lists  
            
- **Looping through lists** ->   
        - `for` or `while` loops can be used to iterate through each element in a list
            
""")
code_loop = '''
drivers = ['Max Verstappen', 'Charles Leclerc', 'Kimi Antonelli']

# for loop
for driver in drivers:
    print(driver)

# while loop
index = 0
while index < len(drivers):
    print(drivers[index])
    index += 1 
'''
st.code(code_loop, language="python")
st.markdown("""
Output:  
        `Max Verstappen`  
        `Charles Leclerc`  
        `Kimi Antonelli`  

`Max Verstappen`  
        `Charles Leclerc`  
        `Kimi Antonelli`  

---

- **Slicing Lists** –>
        - We can extract a portion of a list using slices. The syntax is `list_name[start_index:end_index]`, which returns a new list containing elements from `start_index` to `end_index - 1`. 
""")
code_slice = '''
fruits = ['apple', 'cherry', 'orange', 'grapes', 'kiwi', 'mango']
print(fruits[1:4])  # Slicing from index 1 to 3
print(fruits[:3])  # Slicing from start to index 2
print(fruits[2:])  # Slicing from index 2 to end
print(fruits[-4:-1])  # Slicing using negative indices
'''
st.code(code_slice, language="python")
st.markdown("""
Output:  
        `['cherry', 'orange', 'grapes']`  
        `['apple', 'cherry', 'orange']`  
        `['orange', 'grapes', 'kiwi', 'mango']`  
        `['orange', 'grapes', 'kiwi']`

---
            
- **Copying the list** –>  
        - We can create a copy of a list using slicing or the `list()` function to avoid modifying the original list when making changes to the copy.
""")
code_copy = '''
original = ['a', 'b', 'c']

copy1 = original[:]  # Using slicing
copy1.append('d')
print(f"Original list: {original}")
print(f"copy1 after modification: {copy1}")

copy2 = list(original)  # Using list() function
copy2.append('e')
print(f"Original list: {original}")
print(f"copy2 after modification: {copy2}")

false_copy = original  # This does NOT create a copy; both refer to the same list
false_copy.append('f')
print(f"Original list: {original}")
print(f"false_copy: {false_copy}")
'''
st.code(code_copy, language="python")
st.markdown("""
Output:  
`Original list: ['a', 'b', 'c']`  
`copy1 after modification: ['a', 'b', 'c', 'd']`  

`Original list: ['a', 'b', 'c']`  
`copy2 after modification: ['a', 'b', 'c', 'e']`  

`Original list: ['a', 'b', 'c', 'f']`  
`false_copy: ['a', 'b', 'c', 'f']`    

As evident, modifying `false_copy` will also modify `original`, while modifying `copy1` or `copy2` will not affect `original`.

---
            
- **Simple Statistics** –> 
""")
code_stats = '''
even_numbers = list(range(2, 11, 2))  # Generating a list using "range" function
print(f"Even numbers: {even_numbers}")

print(min(even_numbers))  # Minimum value
print(max(even_numbers))  # Maximum value
print(sum(even_numbers))  # Sum of all values
print(len(even_numbers))  # Length of the list
print(sum(even_numbers) / len(even_numbers))  # Average value
print(even_numbers.count(4))  # Count occurrences of 4
print(even_numbers.index(6))  # Index of first occurrence of 6
'''
st.code(code_stats, language="python")
st.markdown("""
Output:  
        `Even numbers: [2, 4, 6, 8, 10]`  
`2`  
`10`  
`30`  
`5`  
`6.0`  
`1`  
`2`  
            
---
            
- **List Comprehensions** –>  
        - A list comprehension is a concise way to create lists. 
""")
code_comp = '''
squares = [x**2 for x in range(1, 11)]
print(squares)
'''
st.code(code_comp, language="python")
st.markdown("""
Output:  
        `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
""")

st.divider()
st.markdown("""
### Yep!!! Easy-peasy and straightforward. Wasn't a problem for us, right? Let's move ahead now.😎
""")
