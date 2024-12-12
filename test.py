import streamlit as st 

st.title("Große Überschrift", anchor=False)
st.header("Kleiner", anchor=False,divider=True)
st.subheader("Das ein kleinere Text", anchor=False, divider=True)
st.write("Website von Adrian")
st.image("https://cdn.britannica.com/70/234870-050-D4D024BB/Orange-colored-cat-yawns-displaying-teeth.jpg")
st.video("https://www.youtube.com/watch?v=QO42LAU6KPs")

st.title("Website", anchor=False)
st.header("Web", anchor=False,divider=True)
st.subheader("Noch Kleiner", anchor=False, divider=True)
st.write("Ich mag Fortnite")
st.image("https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg")
st.video("https://www.youtube.com/watch?v=atvxr0w4hqg")


st.title("Überschrift", anchor=False)
st.header("Überschrift2", anchor=False,divider=True)
st.subheader("GGs", anchor=False, divider=True)
st.write("Ich mag Katzen")
st.image("https://www.cdc.gov/healthy-pets/media/images/2024/04/Cat-on-couch.jpg")
st.video("https://www.youtube.com/watch?v=l0e22J2MmSQ")


st.title("Lebenslauf", anchor=False)
st.header("Bewerbung", anchor=False,divider=True)
st.subheader("It", anchor=False, divider=True)
st.write("II ist spannend")
st.image("https://www.petplace.com/article/general/pet-care/media_1399cb2968b4c262eb5a859b60be330bbaba65f8b.jpeg?width=750&format=jpeg&optimize=medium")
st.video("https://www.youtube.com/watch?v=6jMkQooLNKc")

st.title("Überschrift", anchor=False)
st.header("Über3", anchor=False,divider=True)
st.subheader("Autos", anchor=False, divider=True)
st.write("Autos sind intressant")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREcm3YElzQgx62Ee5A3LQDcQ_XVNBAuCb9mLBtq-MhfgXBxs2I1uR_6JmTQPjjPNXg4HE&usqp=CAU")
st.video("https://www.youtube.com/watch?v=6vJASAKezMA")

left, right = st.columns(2)
with left:
    st.write("Hallo")
with right:
    st.write("Bye")

left, right = st.columns(2)
with left:
    st.title("Hallo")
with right:
    st.title("Bye")

left, right = st.columns(2)
with left:
    st.header("Hallo")
with right:
    st.header("Bye")

left, right = st.columns(2)
with left:
    st.subheader("Hallo")
with right:
    st.subheader("Bye")

left, right = st.columns(2)
with left:
    st.image("https://images.mein-mmo.de/medien/2020/07/fortnite-scar.jpg")
with right:

    st.image("https://static.wikia.nocookie.net/fortnite/images/f/f6/Fortnite_Schallged%C3%A4mpftes_Sturmgewehr.jpg/revision/latest?cb=20180914094454&path-prefix=de")

    left, right = st.columns(2)
with left:
    st.video("https://www.youtube.com/watch?v=Ro4B9levkco")
with right:
    st.video("https://www.youtube.com/watch?v=Mm0alAHdXHM")

