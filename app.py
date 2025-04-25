import os
import streamlit as st


# Adding a new row for more URLs
def add_row():
    st.session_state.size = min(10, st.session_state.size + 1)

# Delete entry based on index provided
def del_row(idx: int):
    st.session_state.size = max(0, st.session_state.size - 1)
    del st.session_state.url_entry[idx]
    del st.session_state.url_del_button[idx]


st.title("Equity Research Tool 📈")

# URL input section
with st.sidebar:
    st.title("News Article URLs")

    # If the session state does not exist, variables are constructed
    if "size" not in st.session_state:
        st.session_state.size = 1
        st.session_state.url_entry = []
        st.session_state.url_del_button = []

    # Rendering the entry feild and the deletion button in a 2*1 grid
    for idx in range(st.session_state.size):
        col1, col2 = st.columns(2, vertical_alignment="bottom")
        with col1:
            st.session_state.url_entry.append(st.text_input(f'URL {idx + 1}', key=f'text{idx}'))
        with col2:
            st.session_state.url_del_button.append(st.button("❌", key=f'delete{idx}', on_click=del_row, args=(idx, )))

    # Button to add new feild for additional urls
    st.button("➕ Add field", on_click=add_row)
