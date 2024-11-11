import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama
from protein import generate_search_urls

# Streamlit UI
st.title("AI Web Scraper")
protein_name = st.text_input("Give Protein name:")
urls = []

# Step 1: Scrape dbs for protein information
if st.button("Scrape Now"):
    if protein_name:
        st.write("Scraping the databases for protein information...")
        urls = generate_search_urls(protein_name)
        if 'dom_content' not in st.session_state:
            st.session_state.dom_content = {}
        for url in urls:
            st.write(f"Scraping {url['name']}...")
            dom_content = scrape_website(url["url"])
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the DOM content in Streamlit session state
            st.session_state.dom_content[url['name']] = cleaned_content

# Step 2: Iterate through dbs
validity_check = {}
if 'dom_content' in st.session_state:
    parse_description = st.text_area("Describe anything specific to parse")
    if st.button("Parse Content"):
        st.write("Parsing the content from all the databases...")
        for name, content in st.session_state.dom_content.items():
            dom_chunks = split_dom_content(content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            validity_check[name] = parsed_result

# Display the results
st.write("Validity Check Results:")
st.write(validity_check)

#valid_dbs = [name for name in validity_check.keys() if name == "Valid"]
#for url in urls:
#    if url["name"] in valid_dbs:
#        st.write(f"Database: {url['name']} - Go to: {url['url']}")
#    else:
#        st.write(f"Database: {url['name']} - Invalid")