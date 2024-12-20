import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# https://technobrice.com/tech/satine/getting-started-with-streamlit/

# Chemin d'accès
# cd "C:\Users\clegu\Desktop\DATA\2 - Exercices\Streamlit"

# Exécution du script
# streamlit run "Exo 2 - Streamlit partie 2 - Manipuler des graphiques.py"

# Affichage du site
# http://localhost:8501


# Affichage du titre
st.title('Tu vas pouvoir choisir parmi ces datasets, celui que tu souhaites analyser :')

# Création de ma liste de datasets présents dans seaborn
liste_datasets = sorted(sns.get_dataset_names())
# je crée une variable et stock et les données de ma df

# Creation de la selectbox qui contient la liste des datasets
choix_liste_datasets = st.selectbox("Choisissez le dataset que vous souhaitez analyser :",
                                     liste_datasets)

st.write(f'Tu as choisi : {choix_liste_datasets}')

# Chargement du dataset choisi (en off)
dataset_choisi = sns.load_dataset(choix_liste_datasets)

# Creation de la liste des colonnes du dataset choisi
colonnes_dataset = dataset_choisi.columns.tolist()

# Création de ma select box dans laquelle sera listée les colonnes liées au dataset choisi pour l'axe X
choix_liste_colonne_dataset_x = st.selectbox("Choisissez la colonne pour votre axe x :",
                                            colonnes_dataset)

st.write(f'Tu as choisi en axe x : {choix_liste_colonne_dataset_x}')

# Création de ma select box dans laquelle sera listée les colonnes liées au dataset choisi pour l'axe X
choix_liste_colonne_dataset_y = st.selectbox("Choisissez la colonne pour votre axe y :",
                                            colonnes_dataset)

st.write(f'Tu as choisi en axe y : {choix_liste_colonne_dataset_y}')

# Création de ma liste de graphiques présents dans matplotlib
liste_graphiques = ['bar_chart','scatter_chart','line_chart']

# Creation de la selectbox qui contient la liste des graphiques
choix_liste_graphiques = st.selectbox("Choisissez le graphique que vous souhaitez utiliser pour l'analyse des données que vous venez de sélectionner:",
                                        liste_graphiques)

st.write(f'Tu as choisi comme graphique le : {choix_liste_graphiques}')

# Affichage du graphique
if choix_liste_graphiques == 'bar_chart': # si le graphique choisi est 'bar_chart'
    st.bar_chart(dataset_choisi.set_index(choix_liste_colonne_dataset_x)[choix_liste_colonne_dataset_y])
    # Je selectionne l'axe x comme index et y seraont les valeurs

# Pour les autres graphiques, je renseigne uniquement mes axes x et y
elif choix_liste_graphiques == 'scatter_chart':
    st.scatter_chart(dataset_choisi[[choix_liste_colonne_dataset_x, choix_liste_colonne_dataset_y]])

elif choix_liste_graphiques == 'line_chart':
    st.line_chart(dataset_choisi[[choix_liste_colonne_dataset_x, choix_liste_colonne_dataset_y]])

# Création de la checkbox  et affichage de la matrice si la checkbox est cochée
if st.checkbox('Afficher la matrice de corrélation'):
    st.write('Ma matrice de corrélation')
    dataset_selectionne = dataset_choisi[[choix_liste_colonne_dataset_x, choix_liste_colonne_dataset_y]]
    correl_num = dataset_selectionne.select_dtypes(include=[float, int]) # Je prends en compte que des données numériques pour le calcul de la corrélation
    corr_matrix = correl_num.corr() # j'applique la corrélation
    
    if correl_num.empty : # si les données numériques sont vides
        st.warning("Les données selectionnées ne sont pas numériques, l'affichage de la matrice ne peut donc se faire")

    else : # dans le cas contraire j'affiche ma matrice
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)

