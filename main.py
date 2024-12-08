import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas

# Initialisation des états pour suivre l'interaction
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'firstname' not in st.session_state:
    st.session_state.firstname = ""
if 'contact' not in st.session_state:
    st.session_state.contact = ""
if 'appointment_date' not in st.session_state:
    st.session_state.appointment_date = None

# Fonction pour créer le ticket PDF
def create_pdf(name, firstname, contact, appointment_date):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 800, "🎟️ Ticket de Rendez-vous")
    
    c.setFont("Helvetica", 14)
    c.drawString(50, 750, f"Nom : {name}")
    c.drawString(50, 730, f"Prénom : {firstname}")
    c.drawString(50, 710, f"Contact : {contact}")
    c.drawString(50, 690, f"Date de Rendez-vous : {appointment_date}")
    
    c.drawString(50, 650, "Merci d'avoir utilisé notre service ! 😊")
    c.save()
    buffer.seek(0)
    return buffer

# Titre et bienvenue
st.title("🤖 Bienvenue dans notre Chatbot Entreprise")
st.write("Salut ! Je suis votre assistant personnel de prise de rendez-vous. 🎉")
st.write("Pas d’inquiétude, je suis un chatbot sympa... et je promets de ne pas trop blaguer ! 😄")

# Étape 1 : Collecter le nom
if st.session_state.step == 1:
    st.write("👋 Comment vous appelez-vous ?")
    st.session_state.name = st.text_input("Entrez votre **nom** :")

    if st.session_state.name:
        st.session_state.step = 2

# Étape 2 : Collecter le prénom
if st.session_state.step == 2:
    st.write(f"Ravi de vous rencontrer, {st.session_state.name}! 😊 Maintenant, quel est votre **prénom** ?")
    st.session_state.firstname = st.text_input("Entrez votre **prénom** :")

    if st.session_state.firstname:
        st.session_state.step = 3

# Étape 3 : Collecter le contact
if st.session_state.step == 3:
    st.write(f"Génial, {st.session_state.firstname}! Maintenant, donnez-moi un moyen de vous joindre. 📞")
    st.session_state.contact = st.text_input("Entrez votre **contact** (téléphone ou email) :")

    if st.session_state.contact:
        st.session_state.step = 4

# Étape 4 : Sélectionner la date
if st.session_state.step == 4:
    st.write(f"Parfait, {st.session_state.firstname}! 🎯 Choisissez une date pour votre rendez-vous.")
    st.session_state.appointment_date = st.date_input(
        "📅 Sélectionnez une date :",
        min_value=datetime.today()
    )

    if st.session_state.appointment_date:
        st.session_state.step = 5

# Étape 5 : Afficher le ticket et générer le PDF
if st.session_state.step == 5:
    st.success("🎉 Rendez-vous confirmé ! Voici votre ticket :")
    
    # Générer le PDF
    pdf_buffer = create_pdf(
        st.session_state.name,
        st.session_state.firstname,
        st.session_state.contact,
        st.session_state.appointment_date
    )

    # Afficher les informations
    st.write("### 🗓️ Ticket de Rendez-vous")
    st.write(f"**Nom** : {st.session_state.name}")
    st.write(f"**Prénom** : {st.session_state.firstname}")
    st.write(f"**Contact** : {st.session_state.contact}")
    st.write(f"**Date de rendez-vous** : {st.session_state.appointment_date}")
    st.write("Merci d'avoir utilisé notre service ! 🚀")

    # Télécharger le ticket en PDF
    st.download_button(
        label="📥 Télécharger le ticket (PDF)",
        data=pdf_buffer,
        file_name="ticket_rendez_vous.pdf",
        mime="application/pdf"
    )

    # Terminer la conversation
    st.write("C'est tout pour moi ! À bientôt 👋")
