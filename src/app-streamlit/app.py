import requests
import streamlit as st

def call_api(item, user_query):
    url = f"http://api:8000/items/{item}"
    params = {'q': user_query}
    headers = {'accept': 'application/json'}

    response = requests.get(url, params=params, headers=headers)
    return response

def main():
    st.title("Mon application Streamlit")
    st.write("Bienvenue sur mon application !")

    # Input field for the user to enter a query
    user_query = st.text_input("Entrez votre requête", "test")

    # Utilisation d'une variable de session pour `item`
    if 'item' not in st.session_state:
        st.session_state['item'] = 0

    # Bouton pour appeler l'API
    if st.button("Appeler l'API"):
        # Incrémentation de `item`
        st.session_state['item'] += 1

        # Appel de la fonction API
        response = call_api(st.session_state['item'], user_query)
        
        # Afficher la réponse
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error(f"Erreur lors de l'appel de l'API: Status {response.status_code}")

if __name__ == "__main__":
    main()
