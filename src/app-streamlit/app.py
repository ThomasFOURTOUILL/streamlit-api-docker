import requests
import streamlit as st

def main():
    st.title("Mon application Streamlit")
    st.write("Bienvenue sur mon application !")

    # Bouton pour appeler l'API
    if st.button("Appeler l'API"):
        url = "http://localhost:8000/items/5?q=somequery"
        response = requests.get(url)
        st.write(response.json())

if __name__ == "__main__":
    main()
