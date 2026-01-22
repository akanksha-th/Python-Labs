import streamlit as st

st.set_page_config(page_title="Variables", layout="wide")
st.title("Variables and Simple Data Types")

st.divider()

st.markdown("""
This section is just to build some familiarity, so you can understand what's written. This is gonna be like learning the alphabets for python language.
            
## 🧮 Variables

A **variable** is just a **name** that points to a value in memory, defined using the assignment operator -> "=".  

Firstly, some basic rules:
- variable name can start with a letter (a-z, A-Z) or an underscore(_), cannot start with a number or spaces.
- spaces are not allowed in a variable name (e.g., user name is invalid; use user_name).
- python is case-sensitive. age, Age, and AGE are treated as three completely different variables.

While Python allows many naming styles, following these conventions makes your code "Pythonic" and readable:
- Use all lowercase letters with underscores for multi-word variables (e.g., multi_word_variable)
- Use all uppercase letters with underscores for values that should not change (e.g., MAX_RETRY_LIMIT = 5).
- Choose concise but meaningful names (e.g., student_list is better than s_l).

""")

code_1 = '''message = "Hello, Python!"
print(message)'''
st.code(code_1, language="python")

st.markdown("""
Here, `message` is the variable.  
The string `"Hello, Python!"` is the value.
""")

st.divider()

st.info("""
🧠 **Quick Insight: `type()`**

If you're ever unsure what kind of data a variable is holding,
Python gives you a built-in function called `type()`.

It tells you the **data type** of any value.
""")

code_type = '''x = 10
y = 3.14
z = "hello"

print(type(x))
print(type(y))
print(type(z))'''
st.code(code_type, language="python")

st.markdown("""
Output: 
            `<class 'int'>`
            `<class 'float'>`
            `<class 'str'>`    respectively.       
This becomes extremely useful when debugging.""")

st.divider()

st.markdown("""
### 🔡 Strings
            
A string in python is a series of characters. Anything written within quotes ("" or '') is a string.

There's one very interesting catch though - in statements that have the use of quotes or apostophes in them.

**For Example:**
            
`message = 'There's one very interesting catch though'`
    This will throw a SyntaxError because Python thinks the string ends at `There`.

    To fix this, either:
    - use double quotes, 
    - escape the apostrophe using `\`
            
`message = "There's one very interesting catch though"` or \n
`message = 'There\\'s one very interesting catch though'`
            
--
    
`message = 'Albert Einstein once said, "Education is what remains after one has forgotten everything he learned in school."'`
    Similarly here, we use the single quotes to avoid any confusion for the python interpreter.
            
#### **Some basic string functions**

- change case –> `.upper()`, `.lower()`, `.title()`
- remove prefix/suffix –> `.removeprefix("prefix")`, `.removesuffix("suffix")`
- use of f-strings –> 
""")

code_f = '''first_name = "John"
last_name = "Mayer"
message = f"Hi, {first_name} {last_name}"
print(message)'''
st.code(code_f, language="python")

st.markdown("""
Output: `Hi, John Mayer`
- add whitespaces (use \t, \n) –> 
            `print("Languages:\\n\\tPython\\n\\tC\\n\\tJavaScript")`
- remove whitespaces (\t, \n, spaces) –> `.lstrip()`, `.rstrip()`, `.strip()`
""")

st.divider()

st.markdown("""
### 🔢 Numbers
            
We can add (+), subtract (-), multiply (*), and divide (/)
integers in Python. We won’t go deep into integer vs float operations here.
            
""")

st.warning("""
⚠️ **Floating Point Precision (Very Important)**

Computers do **not** store decimal numbers exactly.
They store them in binary approximations.
""")

code_float = '''print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)'''
st.code(code_float, language="python")

st.markdown("""
Output:
`0.30000000000000004`
`False` 

You might *expect* `0.3`, but Python shows something slightly different.

This is **normal behavior**, not a bug.

📌 **Why this matters later:**  
In Deep Learning, small numerical differences can affect:
- loss values
- thresholds
- comparisons
""")

st.markdown("""           
Now let's talk about defining numbers. There are the correct ways and then a few that might throw an error. Let me break it done for you.

**Correct ways**
            - `num = 10000` or `num = 10_000`
            But interestingly enough, the use of underscore is insignificant for the interpreter. It is only for the user's clarity. The python interpreter ignores this underscore.
""")

code_num = '''num1 = 1000
num2 = 1_000
num3 = 10_00
num4 = 1_0_0_0

print(num1 == num2 == num3 == num4)'''
st.code(code_num, language="python")

st.markdown("""
Output : `True`

**Wrong ways**
            - Do not use commas to define a number ever. It does something really interesting.
            
You may have heard about the tuple data structure in Python. So, when I define something like `num = 12,345,678` it creates a tuple with values `(12, 345, 678)`
Similarly, let's say you do `num2 = 10,000,000` it creates the tuple `(1, 0, 0)`.
But this too, won't always be correct.

Let's say you define `num3 = 10,020,000`. Now this is problematic. It will throw an error.
Maybe you'd reckon that a tuple `(10, 20, 0)` should have been created but look at `020` - leading zeros in decimal integer literals are not permitted.
Hence the error.   


We can also do multiple assignments, by ensuring that number of variables matches the number of values.
        Here are the examples of some valid multiple assignments.
            - `x, y, z = 10, 20, 48`
            - `a, b, c = "John", 23, 18.97`

And as discussed above, constants can be defined like this: `NUM_RETRIES = 50` or `LENGTH = 200`. 
        
""")

st.divider()

st.markdown("""
### 🤫 Comments and Docstrings
            
Comments are extremely important and the most underrated features in most programming languages.
In Python, **comments are ignored completely by the interpreter**.
They exist **only for humans** reading the code. Docstrings also serve a similar function, but let's know the distinction here.
            
    - # → comments → ignored by Python
    - ''' docstring '''  → stored as documentation

_Both triple single quotes ('''...''') and triple double quotes (\"""...\""") are valid for defining docstrings in Python because a docstring is simply a regular string literal that happens to be the first statement within a function, class or module._

--   
While **comments** are ignored by Python,  **docstrings** are actually stored as part of the code.
Docstrings are used to **document what a function, class, or module does**.

Neither comments nor docstrings affect program output.
""")

code_comm = '''# Comment: Say hello to everyone.
def greet(name):
    """
    Docstring:
    This function greets a user by name.

    Parameters:
        name (str): The name of the user

    Returns:
        None
    """
    print(f"Hello, {name}!")

greet("John Mayer")'''
st.code(code_comm, language="python")

st.markdown("""Output: `Hello, John Mayer`""")

st.divider()

st.info("""
#### 🧘 **It's Fun o'clock**

Python has a philosophy - literally.👀

Open your terminal (not here) and run:
`python` or `python3`

Then type:
`import this`

I don't know what happens. Maybe you should find out (and read it).😁
""")

st.markdown("""
## We are all set to move ahead.
""")