"""sorting the passenger list"""
import streamlit as st


"""choose"""
def get_pass_list(data, save, sex):
    if sex =='мужчины':
        sex ='male'
    else:
        sex ='female'
    out_list = []
    for line in data:
        if line.split(',')[1] == save and line.split(',')[5] == sex:
            out_list += [line]
    return out_list

with open('data.csv') as file:
    data =file.readlines()


"""enter parameters"""    
def makarnv_code():
    sex = st.selectbox('Выберите пол пассажира:', ['мужчины', 'женщины'])
    save = st.selectbox("Спасен?", ['0', '1'])
    st.table({"Спасенные пассажиры:": get_pass_list(data, save, sex)})
    
mararnv_code()
