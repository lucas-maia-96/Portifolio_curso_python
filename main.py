import streamlit as st 

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/luke.jpg")
    
with col2:
    st.title("Lucas Maia")
    content = """ Olá, meu nome é Lucas, tenho 26 anos e sou estudante de Sistemas de Informação, além de ser graduado em Matemática. Tenho uma profunda paixão por aprendizado contínuo e sou fascinado pelo poder da ciência dos dados. Meu interesse principal está na área de Ciência de Dados, abrangendo tópicos como Machine Learning, Redes Neurais, Inteligência Artificial e Deep Learning. Estou sempre em busca de oportunidades para aprimorar minhas habilidades e contribuir para projetos desafiadores nesse campo emocionante. """
    st.info(content)

content2 = """ Below you can find some of the apps I have built in Python. Feel free to contact me! """
 
st.write(content2)