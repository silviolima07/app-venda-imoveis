import streamlit as st
import requests
import ujson as json
from PIL import Image
import time

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

    image = Image.open("vende-se.png")
    st.sidebar.image(image,caption="",use_column_width=True)

    #st.sidebar.markdown("#### --> Streamlit") 
    #st.sidebar.markdown("#### > ExtraTreesRegressor (api Heroku)")
    #st.sidebar.markdown("#### --> Modelo alocado no Heroku")

    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)     

    #st.markdown("### Selecione as caracteristicas do apartamento")
    area_total = st.slider('Área Total',min_value=100, max_value=500, value=200, step=50)
    area_util = st.slider('Área Útil',min_value=100, max_value=500, value=250, step=50)
    quarto = st.slider('Quarto',min_value=1, max_value=6, value=2, step=1)
    banheiro = st.slider('Banheiro',min_value=1, max_value=6, value=2, step=1)
    vaga = st.slider('Vaga', min_value=1, max_value=5, value=1, step=1)
    #st.markdown("#### Caracteristicas selecionadas do passageiro")
    #st.write('Caracteristicas: '+ classe,'---', sexo, '---',embarque,'---',idade,"anos",'---','$$',passagem)

    #cloud = Image.open("cloud.png")
    #st.image(cloud,caption="",use_column_width=True)
    
    data = [{'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}]
        
    # Choosen data
    data = {'area_total_clean': area_total, 'area_util_clean': area_util, 'quarto_clean':quarto, 'banheiro_clean': banheiro, 'vaga_clean': vaga}
    
    # Formato json 
    data = json.dumps(data)

    print(data)
      
    # url da api no heroku 
    url = 'https://app-api-001.herokuapp.com/'
      
    st.sidebar.markdown(" ") 
    st.sidebar.markdown("#### Prever o valor do apartamento")
    st.sidebar.markdown(" ")

    if st.sidebar.button('Submit'):
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
            st.markdown('#### Previsão do modelo:')
            status = checar_retorno(send_request)
            
            #st.sidebar.markdown(" ")
            st.title("R$ "+status)

           



if __name__ == '__main__':
    main()

     
