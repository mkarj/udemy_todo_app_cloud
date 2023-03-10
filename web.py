# terminal: streamlit run web.py -> selaimessa localhost sivu...
#
# deployment to cloud:
# - pip freeze > requirements.txt
# - in project (repository) only files: web.py, functions.py, todos.txt, requirements.txt, pages/about.py
# - streamlit local host sivulta -> deploy
# - login github tunnuksilla

import streamlit as st
import functions

todos = functions.get_todos()

# callback function
def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo", on_change=add_todo, key='new_todo')

# for develoment and debugging purposes
# st.session_state

