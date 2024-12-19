import streamlit as st
from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'lebenslauf..pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)
with right:
    st.title("Constantin Adrian", anchor=None)
    st.markdown(f"<em> <p>Ich bin davon überzeugt, dass der Beruf des Kfz Mechanikers gut zu mir passt,weil ich mich sehr für Technik intressiere und mich darauf freue praktische erfahrung zu sammeln. </p> </em>", unsafe_allow_html=True)
    # Der Download-Button, der die Datei zur Verfügung stellt
    st.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
st.write("📩", "constantinadrian10.10@gmail.com")


left.image("png.png")


st.header ("IT-Kompetenzen", anchor=False, divider="blue")

st.write("""
- 🌍Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)   
- 💻Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
- 📊Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
- 🚀Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
- 🎓Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
                         """, unsafe_alow_html=True)
st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)
st.header ("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse, Wien", anchor=False)
st.write("""
    ► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft       
    ► Zeitraum: September 2024 - Juli 2025         
    ► Derzeitiger Notenschnitt: 1,5
        
         
         
         
        """ )

st.subheader("Herzgasse 27, Wien", anchor=False)
st.write("""
► Zeitraum: September 2020 – Juli 2024     
► Abschluss-Notendurchschnitt: 1,7
         """)
st.header ("Arbeitserfahrung", anchor=False, divider="blue")
st.write("""
💼 Berufspraktische Tage 1: Bei XYZ von 18. bis 22. Nov. 2024       
💼 Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025

        """)
st.header ("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.write("""
💻 Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien         
✨ Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich         
✨Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten      
    """) 
st.header ("Interessen und Hobbys", anchor=False, divider="blue")
st.write("""
         
 Fußball: Mitglied in einem Fußball-Klub         
📖 Lesen: Begeisterte Leserin verschiedenster Literatur      
♟️  Schach: Engagiert im Schachklub
""")



