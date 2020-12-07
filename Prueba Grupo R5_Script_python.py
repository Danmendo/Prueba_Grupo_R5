#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importamos los módulos necesarios para realizar el proceso
import pandas as pd


# In[4]:


#Creamos la base de datos
Base = pd.DataFrame({"Producto": ["Cascos", "Guantes"], '2019': [17000, 8100], '2018': [15700, 5400], '2017': [14301, 2100]})


# In[5]:


#Miramos la base de datos
Base


# In[6]:


#Realizamos la reestructuración de la base en el formato especificado en la prueba.
BaseR = pd.melt(Base, id_vars=['Producto'], value_vars=['2019', '2018', '2017'],
        var_name='Año', value_name='Unidades').sort_values("Producto")


# In[7]:


#Miramos el resultado de la reestructuración
BaseR

