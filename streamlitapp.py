# -*- coding: utf-8 -*-
"""StreamLitApp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GxgivGPiwof6XsxlY8j38l1PAMnxpnnK
"""

!curl ipecho.net/plain
#Gets ip address

!pip install streamlit --quiet
!pip install pyngrok --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ushousing.py
# import streamlit as st
# import pandas as pd
# import numpy as np
# 
# st.write("US Housing Dataset")
# 
# df_housing = pd.read_csv("USA_Housing.csv")
# st.dataframe(df_housing)
# 
# df = pd.DataFrame(np.random.randn(10, 2), columns=['Area Population', 'Price'])
# st.line_chart(df)

!streamlit run ushousing.py & npx localtunnel --port 8501

!pip freeze > requirements.txt