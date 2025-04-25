import streamlit as st
from src.helper import llm_construct, embeddings_construct, data_loader, retrieval_construct 

# Function for adding a new row for more URLs to be inputted maxed at 10
def add_row():
    st.session_state.size = min(10, st.session_state.size + 1)

# Function for deleting entry based on index provided
def del_row(idx: int):
    st.session_state.size = max(0, st.session_state.size - 1)
    del st.session_state.url_entry[idx]
    del st.session_state.url_del_button[idx]

# Main Function
def main():
    # Initializing LLM and Embeddings models by holding them in session_state so it is not re-run each time
    if "llm" not in st.session_state or "embeddings" not in st.session_state:
        st.session_state.llm = llm_construct()
        st.session_state.embeddings = embeddings_construct()

    # Title and markdown information for user
    st.title("Equity Research Tool 📈")
    st.markdown('''Input URLs in the sidebar to your left, which would like the chatbot to extract information from and assist you with your research.
                The bot can only process 10 URLs and will only be able to obtain information in english. Any pages hidden behind a paywall or other such
                methods, may not be properly extracted.''')

    st.markdown('''**Disclaimer:** This AI tool is for informational purposes only and may not always provide accurate or complete results. Please verify all
                information independently and do your own research before making any decisions.''')
    
    main_placeholder = st.empty()

    ### URL input section, i.e.
    with st.sidebar:
        st.title("News Article URLs")
        
        # If the session state does not exist, variables are constructed
        if "size" not in st.session_state:
            st.session_state.size = 1
            st.session_state.urls = []
            st.session_state.url_del_button = []
            st.session_state.process_url = False

        # Rendering the entry feild and the deletion button in a 2*1 grid
        for idx in range(st.session_state.size):
            col1, col2 = st.columns(2, vertical_alignment="bottom")
            with col1:
                st.session_state.urls.append(st.text_input(f'URL {idx + 1}', key=f'text{idx}'))
            with col2:
                if not st.session_state.process_url:
                    st.session_state.url_del_button.append(st.button('❌', key=f'delete{idx}', on_click=del_row, args=(idx, )))

        # Button to add new feild for additional urls
        if not st.session_state.process_url and st.session_state.size <= 9:
            st.button('➕ Add field', on_click=add_row)
        
            # Button to process all the URLs currently available
            st.session_state.process_url = st.button('Process URLs')

        # Reset button to kill the process_url
        if st.button('Reset Bot'):
            st.session_state.process_url = False
            del st.session_state.vector_index
            del st.session_state.chain

    ### Main application area
    if st.session_state.process_url:
        # Building vector_index using urls provided and retrival chain
        main_placeholder.markdown("**Loading Data.....**")
        if "vector_index" not in st.session_state:
            st.session_state.vector_index = data_loader(st.session_state.urls, st.session_state.embeddings)

        # Creating the retrieval chain
        main_placeholder.markdown("**Initializing Query Bot.....**")
        if "chain" not in st.session_state:
            st.session_state.chain = retrieval_construct(st.session_state.llm, st.session_state.vector_index)

        temp_placeholder = st.empty()
        # Querying the vector_index
        if query := main_placeholder.text_input("Questions: "):

            temp_placeholder.markdown("**Loading Answer.....**")
            query_result = st.session_state.chain({"question": query}, return_only_outputs=True)
            temp_placeholder = st.empty()

            # Outputing results
            st.markdown(f"**Question**: {query}")
            st.markdown(f"**Answer**: {query_result['answer']}")
            if query_result['sources']:
                st.markdown(f"**Sources**: {query_result['sources']}")


if __name__ == '__main__':
    main()
