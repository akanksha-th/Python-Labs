import streamlit as st

st.title("Hello, Python!")

st.markdown("""
### 📖Context            

For context, I have been following the book **_Python Crash Course, 3rd Edition - A Hands-On, Project Based Introduction To Programming_** by **_Eric Matthes_**
I always use this book for revision. It is just so clear and easy to understand. I recommend this to EVERYONE.

""")

st.divider()

st.markdown("""
### 🛠️Setup            

In this section, as the name indicates, I am gonna discuss the same old, getting prepared to code in python.

**Python is a cross-platform programming language**, which
means it runs on all the major operating systems. But it doesn't usually come pre-installed with them, except on Linux. We need to install it and then install VS Code also (or any IDE). Since I started coding, I have always used VS Code. No specific reasons - I also read it somewhere to install it, so I did.💀 You will find a thousand different tutorials telling the steps, so I'll skip explaining them here.
""")

st.info("""
📌 **Tip**  
Choose one editor and stick to it. Consistency matters more than the “best” tool.
""")

st.markdown("""
### 🐍 Python Versions
            
Python is an ever-evolving programming language. As of writing this, the latest version is 3.14. You can verify your installed version using `python --version` or `python3 --version` on CLI or terminal.

            
### ⚠️ Common Confusion
            
Now the most confusing part is to be addressed here. 
            
Historically:
- `python` → Python 2.x  
- `python3` → Python 3.x  

This separation was done to prevent accidental breakage of system scripts. 
            
In 2026, because Python 2 is long-dead (EOL since 2020), most modern systems have simply made python a shortcut to python3. 
    
            
**Best Practice:**
            
    - When we activate a virtual environment, both 'python' and 'python3' are automatically mapped to that environment's specific version. 
    - But if you are writing a script or tutorial for others, use 'python3' to be safe across all platforms. 

So, basically, it's all cool. Just stick to good coding practices.
""")

st.divider()

st.markdown("""
### ▶️ The Ritual
            
Now follows the ever necessary **Running a hello world program on terminal**
""")

code = '''print("Hello, Python world!")'''

st.code(code, language="python")

if st.button("▶ Run code"):
    st.write("Output:")
    st.success("Hello, Python world!")

st.divider()

st.markdown("""
## We are all set to learn now. Let's go!!
""")