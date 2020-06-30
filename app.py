import streamlit as st
import requests
import ujson as json
from PIL import Image
import time
import pandas as pd

def checar_retorno(send_request):
  data = send_request.json()
  temp = str(data).split()[2]
  status = temp.replace('}}', '')
  return status



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

    image = Image.open("vende-se2.png")
    st.sidebar.image(image,caption="",use_column_width=True)

    #st.sidebar.markdown("#### --> Streamlit") 
    #st.sidebar.markdown("#### > ExtraTreesRegressor (api Heroku)")
    #st.sidebar.markdown("#### --> Modelo alocado no Heroku")

    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df_bairros = pd.read_csv("modelos_bairros.csv")     

    menu_bairro = [df_bairros.Bairro]
    bairro_escolhido = st.selectbox("Bairro",menu_bairro)
    
    

    #st.markdown("### Selecione as caracteristicas do apartamento")
    area_total = st.slider('Área Total',min_value=50, max_value=500, value=200, step=20)
    area_util = st.slider('Área Útil',min_value=50, max_value=500, value=250, step=20)

    quarto = st.radio('Quarto',(1 , 2, 3, 4, 5,6))
    banheiro = st.radio('Banheiro',(1,2,3,4,5,6,7))
    vaga = st.radio('Vaga',(1,2,3,4,5,6,7,8,9,10))

    #quarto = st.slider('Quarto',min_value=1, max_value=6, value=1, step=1)
    #banheiro = st.slider('Banheiro',min_value=1, max_value=6, value=1, step=1)
    #vaga = st.slider('Vaga', min_value=1, max_value=5, value=1, step=1)
    #st.markdown("#### Caracteristicas selecionadas do passageiro")
    #st.write('Caracteristicas: '+ classe,'---', sexo, '---',embarque,'---',idade,"anos",'---','$$',passagem)

    #cloud = Image.open("cloud.png")
    #st.image(cloud,caption="",use_column_width=True)
    
    #data = [{'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}]
        
    
    # Choosen data
    data = {'bairro': bairro_escolhido, 'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}
    
    # Formato json 
    data = json.dumps(data)

    print(data)
      
    # url da api no heroku 
    url = 'https://app-api-001.herokuapp.com/'
      
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

        send_request = requests.post(url, data)
        #st.text("Acessando a api no heroku...")
        if not send_request.ok:
            st.warning("Houston we have a problem.")
       
        elif send_request.ok:
            st.sidebar.markdown('### Previsão do modelo:')
            status = checar_retorno(send_request)
            
            #st.sidebar.markdown(" ")
            if len(status) == 6:
                st.sidebar.title("R$ "+status[0:3]+'.'+status[3:])
            elif len (status) == 7:  
                st.sidebar.title("R$ "+status[0]+'.'+status[1:4]+'.'+status[4:])
            else:
                st.sidebar.title("R$ "+status[0:2]+'.'+status[2:5]+'.'+status[5:])

           



if __name__ == '__main__':
    main()

     
