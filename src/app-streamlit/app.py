import requests
import streamlit as st

def main():
    st.title("Mon application Streamlit")
    st.write("Bienvenue sur mon application !")

    # Input field for the user to enter a query
    user_query = st.text_input("Entrez votre requête", "test")

    # item
    item = 0

    # Bouton pour appeler l'API
    if st.button("Appeler l'API"):

        # item
        item += 1

        # URL de l'API avec la requête de l'utilisateur
        url = f"http://localhost:8000/items/{item}"
        
        # Paramètres de la requête
        params = {'q': user_query}

        # En-têtes de la requête
        headers = {'accept': 'application/json'}

        # Effectuer la requête GET
        response = requests.get(url, 
                                params=params, 
                                headers=headers)
        
        # Afficher la réponse
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error(f"Erreur lors de l'appel de l'API: Status {response.status_code}")

if __name__ == "__main__":
    main()
