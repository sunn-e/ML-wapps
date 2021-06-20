import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import requests

#    https://www.newscientist.com/article/dn22545-dna-imaged-with-electron-microscope-for-the-first-time/

imageUrl = "https://images.newscientist.com/wp-content/uploads/2012/11/dn22545-1_300.jpg?width=800"

image = Image.open(requests.get(imageUrl, stream=True).raw)

st.image(image, use_column_width=True)

st.write("""
         # DNA Nucleotide Count Web App
         Count the nucleotide composition of query DNA
         ***""")

st.header("Enter DNA sequence")

# https://www.genomatix.de/online_help/help/sequence_formats.html

seq_input = ">DNA Query\nGACTCGTAGACTTAGCCTGACTTGCCTT"
seq = st.text_area("Sequence input", seq_input, height=35)
seq = seq.splitlines()
seq = seq[1:]  # skip name
seq = "".join(seq)

st.write("""
         ***
         """)

st.header("INPUT (DNA Query)")
seq

st.header("OUTPUT (DNA Nucleotide Count)")
st.subheader("Print dictionary")


def dna_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")), ("T", seq.count("T")),
        ("G", seq.count("G")), ("C", seq.count("C"))
    ])
    return d


X = dna_nucleotide_count(seq)
X_label = list(X)
X_values = list(X.values())
X

st.subheader("Print TXT")
st.write("Adenine:"+str(X["A"]))
st.write("Thymine:"+str(X["T"]))
st.write("Guanine:", str(X["G"]))
st.write("Cytosine:", str(X["C"]))

st.subheader("Dataframe")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "Nucleotide"})
st.write(df)


st.subheader("Bar Cart")
p = alt.Chart(df).mark_bar().encode(
    x="Nucleotide", y="count"
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)
