import streamlit as st
import pandas as pd
import numpy as np
import glob
from stqdm import stqdm

po_names = pd.DataFrame()
acc = pd.DataFrame()
suits = pd.DataFrame()
trr = pd.DataFrame()
officer_id = 0

def get_officer_id(first_name, last_name):
    global po_names

    po_lookup = po_names.loc[(po_names['last_name'] == last_name) & (po_names['first_name'] == first_name)].copy()
    if len(po_lookup) == 1:
        uid = po_lookup['UID'].values[0]
    elif len(po_lookup) == 0:
        st.text('There is no officer that matches that name :(')
    else:
        uid = st.number_input('There are multiple officers with this name. Please type in the correct one\'s UID by looking at the table below')
        st.dataframe(po_lookup)
    return uid

def search_complaints(id):
    global acc

    acc_lookup = acc.loc[acc['UID'] == id].copy()
    st.caption('Complaint Results')

    if len(acc_lookup) == 0:
        st.text('No complaint results')
    else:
        st.dataframe(acc_lookup)

def search_trrs(df):
    global trr

    trr_lookup = trr.loc[trr['UID'] == id].copy()  
    st.caption('TRR Result')

    if len(trr_lookup) == 0:
        st.text('No TRR results')
    else:
        st.dataframe(trr_lookup)

def search_suits(df):
    global suits

    suits_lookup = suits.loc[suits['UID'] == id].copy()
    st.caption('Lawsuits Result')

    if len(suits_lookup) == 0:
        st.text('No lawsuit results')
    else:
        st.dataframe(suits_lookup)


# load_and_clean_data()
po_names = pd.read_csv('po_names.csv')
acc = pd.read_csv('acc.csv')
suits = pd.read_csv('suits.csv')
trr = pd.read_csv('trr.csv')

st.title('look up officer stuff in our data (plz keep this internal)')
first = st.text_input('Officer first name (all caps please)')
last = st.text_input('Officer last name (all caps please)')
officer_id = get_officer_id(first, last)
search_complaints(officer_id)
search_trrs(officer_id)
search_suits(officer_id)



