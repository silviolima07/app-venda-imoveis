import streamlit as st

from PIL import Image
import time
import pandas as pd
import  numpy as np
import pickle
# Html link
from bokeh.models.widgets import Div


lista_bairros = ['Moema','Itaim Bibi', 'Vila Mariana']

model_Moema = pickle.load(open('Modelo_Bairros/ExtraTreesRegressor-Moema.sav','rb'))

model_Vila_Mariana = pickle.load(open('Modelo_Bairros/ExtraTreesRegressor-Vila_Mariana.sav','rb'))

model_Itaim_Bibi = pickle.load(open('Modelo_Bairros/RandonForestRegressor-Itaim_Bibi.sav','rb'))


def main():
    """ ExtraTreesRegressor - Imoveis """
    
 
    html_page = """
    <div style="background-color:red;padding=10px">
        <p style='color:white;text-align:center;font-size:20px;font-weight:bold'>IMÓVEIS</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)    

    image = Image.open("vende-se.png")
    st.sidebar.image(image,caption="",use_column_width=True)

    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    activities = ["Home", "Pesquisar","About"]
    choice = st.sidebar.selectbox("Menu",activities)


    if choice == "Home":
        st.markdown("### Previsão de valor de apartamento a venda por bairro")
        st.markdown("### Escolha:")
        st.markdown("### - bairro e caracteristicas")
        st.write(" ")
        image1 = Image.open("chaves3.png")
        st.image(image1,caption="",use_column_width=False)
    

    if choice == "Pesquisar":    

        # Escolher o bairro para o qual o regressor deve fazer as previsões
        bairro_escolhido = st.sidebar.selectbox("Bairro",lista_bairros)
    
    

        #st.markdown("### Selecione as caracteristicas do apartamento")
        area_total = st.slider('Área Total',min_value=50, max_value=250, value=100, step=10)
        area_util = st.slider('Área Útil',min_value=30, max_value=200, value=100, step=10)

        quarto = st.radio('Quarto',(1 , 2, 3))
        banheiro = st.radio('Banheiro',(1,2,3))
        vaga = st.radio('Vaga',(1,2,3))

    
        
    
        # Choosen data
        #data = {'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}

        #print(data)

        data = np.array([area_total, area_util, quarto, banheiro, vaga]).reshape(1,5)
      
      
        st.sidebar.markdown(" ") 
        #st.sidebar.markdown("#### 1- Selecione as caracteristicas")
        #st.sidebar.markdown("#### 2- Veja o valor previsto do apartamento")
        #st.sidebar.markdown(" ")

        if st.sidebar.button('Enviar consulta'):
            #bar = st.progress(0)
            #for i in range(11):
            #    bar.progress(i * 10)
            #    # wait
            #    time.sleep(0.1)

            if  bairro_escolhido == 'Moema':
                reg = model_Moema
                print("Model Moema:", model_Moema)

            if bairro_escolhido == "Vila Mariana":
               reg = model_Vila_Mariana
               print("Model Vila Mariana:", model_Vila_Mariana)

            if bairro_escolhido == "Itaim Bibi":
               reg = model_Itaim_Bibi
               print("Model Itaim Bibi:", model_Itaim_Bibi)
           

         
            result = reg.predict(data)
            result = np.expm1(result)
            result = int(result)

            print("Result:", result)
        
            pred = str(result)
            pred =  pred.replace('[','')
            pred =  pred.replace(']','')
            pred =  pred.replace('.','')

            print("Numero de casas:", len(status))
       
            st.sidebar.markdown('## Previsão do modelo')
            if reg == model_Moema:
                st.sidebar.markdown("### Score R2: 95%")
            if reg == model_Itaim_Bibi:
                st.sidebar.markdown("### Score R2: 87%")
            if reg == model_Vila_Mariana:
               st.sidebar.markdown("### Score R2: 88%")
            
            if len(status) == 6:
                print("6 casas")
                st.subheader("R$ "+status[0:3]+'.'+status[3:])

            if len (status) == 7:
                print("7 casas")
                st.subheader("R$ "+status[0]+'.'+status[1:4]+'.'+status[4:])
            
            bar = st.progress(0)
            for i in range(11):
                bar.progress(i * 10)
                # wait
                time.sleep(0.1)

    if choice == 'About':
        st.markdown("### Process")
        st.write(" - First I did a scrap in 2k pages and gather 4k apartment sale announcements")
        st.write(" - It became only 3k unique lines")
        st.write(" - Dataset had 299 neighborhoods, only neighborhoods with more than 50 announcements was used")
        st.write(" - The first neighborhood in this list was Moema with 161 ")
        st.write(" - The third was Itaim Bibi with 124 and the eighth was Vila Mariana with 77 ")
        st.write(" - The model was built using the data present in each neighborhood")
        st.subheader("by Silvio Lima")
        
        if st.button("Linkedin"):
            js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)      



if __name__ == '__main__':
    main()

     
