import streamlit as st

from PIL import Image
import time
import pandas as pd
import  numpy as np
import pickle


lista_bairros = ['Moema','Itaim Bibi', 'Vila Mariana']

model_Moema = pickle.load(open('Modelo_Bairros/RandonForestRegressor-Moema.sav','rb'))

model_Vila_Mariana = pickle.load(open('Modelo_Bairros/ExtraTreesRegressor-Vila_Mariana.sav','rb'))

model_Itaim_Bibi = pickle.load(open('Modelo_Bairros/KNeighborRegressor-Itaim_Bibi.sav','rb'))


def main():
    """ ExtraTreesRegressor - Imoveis """
    
    ## Titulo
    #st.sidebar.title("-> Regressão")
    
    #st.markdown("## Streamlit - Titanic")
 
    #html_page = """
    #<div style="background-color:tomato;padding=10px">
    #    <p style='text-align:center;font-size:20px;font-weight:bold'>Streamlit - Titanic</p>
    #</div>
    #          """
    #st.markdown(html_page, unsafe_allow_html=True)    

    image = Image.open("vende-se3.png")
    st.sidebar.image(image,caption="",use_column_width=True)

    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

         

    # Escolher o bairro para o qual o regressor deve fazer as previsões
    bairro_escolhido = st.sidebar.selectbox("Bairro",lista_bairros)
    
    

    #st.markdown("### Selecione as caracteristicas do apartamento")
    area_total = st.slider('Área Total',min_value=50, max_value=250, value=100, step=10)
    area_util = st.slider('Área Útil',min_value=30, max_value=200, value=100, step=10)

    quarto = st.radio('Quarto',(1 , 2, 3))
    banheiro = st.radio('Banheiro',(1,2,3))
    vaga = st.radio('Vaga',(1,2,3))

    
        
    
    # Choosen data
    data = {'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}

    print(data)

    data = np.array([area_total, area_util, quarto, banheiro, vaga]).reshape(1,5)
      
      
    st.sidebar.markdown(" ") 
    st.sidebar.markdown("#### 1- Selecione as caracteristicas")
    st.sidebar.markdown("#### 2- Veja o valor previsto do apartamento")
    st.sidebar.markdown(" ")

    if st.sidebar.button('Enviar consulta'):
        bar = st.progress(0)
        for i in range(11):
            bar.progress(i * 10)
            # wait
            time.sleep(0.1)

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

        print("Result:", result)
        
        status = str(result)
        status =  status.replace('[','')
        status =  status.replace(']','')
        status =  status.replace('.','')
       
        st.sidebar.markdown('## Previsão do modelo')
            
        if len(status) == 6:
            st.subheader("R$ "+status[0:3]+'.'+status[3:])
        elif len (status) == 7:  
            st.subheader("R$ "+status[0]+'.'+status[1:4]+'.'+status[4:])
        elif len (status) == 8:
            st.subheader("R$ "+status[0:2]+'.'+status[2:5]+'.'+status[5:])
        elif len (status) == 10:
            st.subheader("R$ "+status[0]+'.'+status[1:4]+'.'+status[4:7]+'.'+status[7:10])
            
        bar = st.progress(0)
        for i in range(11):
            bar.progress(i * 10)
            # wait
            time.sleep(0.1)

           



if __name__ == '__main__':
    main()

     
