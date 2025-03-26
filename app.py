import streamlit as st
#import sklearn
from PIL import Image
import time
import pandas as pd
import  numpy as np

import pickle
import joblib 

import warnings
warnings.filterwarnings('ignore')

# Html link
from bokeh.models.widgets import Div



#@st.cache(allow_output_mutation=True)
def load(model_path):
    with open(model_path, 'rb') as pickle_file:
      content =   joblib.load(pickle_file)
    #print('load ok')
    return content

lista_bairros = ['Moema','Itaim Bibi', 'Vila Mariana']

#file_path = './Modelo_Bairros/ExtraTreesRegressor-Moema.sav'
#with open(file_path , 'rb') as f:
#    model.Vila_Mariana = pickle.load(f)

#from sklearn.exceptions import InconsistentVersionWarning
#warnings.simplefilter("error", InconsistentVersionWarning)

#try:
   #est = pickle.loads(file_path)
#   with open(file_path , 'rb
   
#   ') as f:
#    model.Vila_Mariana = pickle.load(f)
    #model_Vila_Mariana = load(open('Modelo_Bairros/ExtraTreesRegressor-Vila_Mariana.sav','rb'))

#except InconsistentVersionWarning as w:
#   print(w.original_sklearn_version)

#with open(file_path, 'rb') as pickle_file:
#    content = pickle.load(pickle_file)


model_Moema = load('./Modelo_Bairros/RandomForestRegressor-Moema.joblib')

model_Vila_Mariana = load('./Modelo_Bairros/RandomForestRegressor-Vila_Mariana.joblib')

model_Itaim_Bibi = load('./Modelo_Bairros/RandomForestRegressor-Itaim_Bibi.joblib')



def main():
    """ ExtraTreesRegressor - Imoveis """
    
 
    html_page1 = """
    <div style="background-color:blue;padding=10px">
        <p style='color:white;text-align:center;font-size:28px;>Predicting the Sale Price of Apartments by Neighborhood</p>
    </div>
              """
    st.markdown(html_page1, unsafe_allow_html=True)   

    image = Image.open("for-sale.png")
    st.sidebar.image(image,caption="",use_column_width=True)

    #st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center}</style>', unsafe_allow_html=True)

    #st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

    #st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

    

    activities = ["Search","About"]
    choice = st.sidebar.selectbox("Menu",activities)

    if choice == "Home":
        html_page = """
    <div style="background-color:blue;padding=10px">
        <p style='color:white;text-align:center;font-size:28px;font-family:'Times New Roman'>Predicting the Sale Price of Apartments by Neighborhood</p>
    </div>
              """
        st.markdown(html_page, unsafe_allow_html=True)  

        st.markdown("### Choose:")
        st.markdown("### - neighborhood and  characteristics")
        st.write(" ")
        image1 = Image.open("chaves3.png")
        st.image(image1,caption="",use_column_width=True)
    

    if choice == "Search":    
        #st.title('Predicting the Sale Price of Apartments by Neighborhood')
        html_page_title = """
<div style="background-color:black;padding=60px">
        <p style='text-align:center;font-size:50px;font-weight:bold; color:red'>Predicting the Sale Price of Apartments by Neighborhood'</p>
</div>
"""               
        st.markdown(html_page_title, unsafe_allow_html=True)

        st.write(" ")
        image1 = Image.open("chaves3.png")
        st.image(image1,caption="",use_column_width=True)
        
        # Escolher o bairro para o qual o regressor deve fazer as previsões
        bairro_escolhido = st.sidebar.selectbox("Neighborhood",lista_bairros)
    
    

        #st.markdown("### Selecione as caracteristicas do apartamento")
        area_total = st.slider('Total Area',min_value=50, max_value=250, value=100, step=10)
        area_util = st.slider('Useful Area',min_value=30, max_value=200, value=100, step=10)
        st.write(" ")
        quarto = st.radio('Bedroom',(1 , 2, 3))
        banheiro = st.radio('Bathroom',(1,2,3))
        vaga = st.radio('Parking spaces',(1,2,3))
        
    
        # Choosen data
        data = {'Total area': area_total, 'Useful area': area_util, 'Bedroom':quarto, 'Bathroom': banheiro, 'Parking spaces': vaga}
        st.markdown("### Characteristics")
        table = pd.DataFrame([data])
        #st.write(data)
        st.table(table)

        data = np.array([area_total, area_util, quarto, banheiro, vaga]).reshape(1,5)
      
      
        st.sidebar.markdown(" ") 
        #st.sidebar.markdown("#### 1- Selecione as caracteristicas")
        #st.sidebar.markdown("#### 2- Veja o valor previsto do apartamento")
        #st.sidebar.markdown(" ")
        
        if st.sidebar.button('Submit'):
            #bar = st.progress(0)
            #for i in range(11):
            #    bar.progress(i * 10)
            #    # wait
            #    time.sleep(0.1)

            if  bairro_escolhido == 'Moema':
                reg = model_Moema
                #print("Model Moema:", model_Moema)

            if bairro_escolhido == "Vila Mariana":
               reg = model_Vila_Mariana
               #print("Model Vila Mariana:", model_Vila_Mariana)

            if bairro_escolhido == "Itaim Bibi":
               reg = model_Itaim_Bibi
               #print("Model Itaim Bibi:", model_Itaim_Bibi)
           

         
            result = reg.predict(data)
            result = np.expm1(result)
            result = int(result)

            #print("Result:", result)
        
            pred = str(result)
            pred =  pred.replace('[','')
            pred =  pred.replace(']','')
            pred =  pred.replace('.','')

            #print("Numero de casas:", len(pred))
            
            st.sidebar.markdown('## Forecast')
            if reg == model_Moema:
                st.sidebar.markdown("### Score R2: 93%")
            if reg == model_Itaim_Bibi:
                st.sidebar.markdown("### Score R2: 87%")
            if reg == model_Vila_Mariana:
               st.sidebar.markdown("### Score R2: 85%")
            
            col1,col2,col3 = st.columns(3)
            if len(pred) == 6:
                #print("6 casas")
                #st.subheader("R$ "+pred[0:3]+'.'+pred[3:])
                with col2:
                  st.subheader("R$ "+pred[0:3]+'.'+pred[3:])

            if len (pred) == 7:
                #print("7 casas")
                #st.subheader("R$ "+pred[0]+'.'+pred[1:4]+'.'+pred[4:])
                with col2:
                  st.subheader("R$ "+pred[0]+'.'+pred[1:4]+'.'+pred[4:])
                  
            bar = st.progress(0)
            for i in range(11):
                bar.progress(i * 10)
                # wait
                time.sleep(0.1)
            
    if choice == 'About':
        st.markdown("### Process:")
        st.markdown("##### - First I did a scrap in 2k pages and gathered 4k apartment sale announcements in São Paulo, Brazil")
        st.markdown("##### - It became only 3k unique lines")
        st.markdown("##### - Dataset had 299 neighborhoods, only neighborhoods with more than 50 announcements was used")
        st.markdown("##### - The first neighborhood in this list was Moema with 161 ")
        st.markdown("##### - The third was Itaim Bibi with 124 and the eighth was Vila Mariana with 77 ")
        #st.write(" - The model was built using the data present in each neighborhood")
        st.markdown("##### Supported by Streamlit from github")
        st.subheader("by Silvio Lima")
        st.write('https://www.linkedin.com/in/silviocesarlima/')
        #if st.button("Linkedin"):
        #    js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
        #    html = '<img src onerror="{}">'.format(js)
        #    div = Div(text=html)
        #    st.bokeh_chart(div)      
       

    

if __name__ == '__main__':
    main()

     
