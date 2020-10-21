import streamlit as st

from PIL import Image
import time
import pandas as pd
import  numpy as np
import pickle



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

    

if __name__ == '__main__':
    main()

     
