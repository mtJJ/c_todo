import streamlit as st
import todo_functions

todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    todo_functions.write_todos(todos)

col1, col2 = st.columns(2)

with col1: 
    st.title("Cedar's Todo App")
    st.subheader("This is my todo app.")

with col2: 
    st.image('PXL_20240707_185155158.MP.jpg')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()   

st.text_input(label="Enter a todo:", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')

# st.session_state