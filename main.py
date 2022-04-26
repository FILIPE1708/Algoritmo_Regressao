import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import pickle

csv = pd.read_csv('dados.csv', sep=";")
labEnc = LabelEncoder()
csv['Tipo'] = labEnc.fit_transform(csv['Tipo'])

dados = csv.values
atributos = dados[:,0:5]
likes = dados[:,6]
compartilhamento = dados[:,7]
comentario = dados[:,5]

modeloLikes = LinearRegression()
modeloLikes.fit(atributos, likes)

modeloCompartilhamentos = LinearRegression()
modeloCompartilhamentos.fit(atributos, compartilhamento)

modeloComentarios = LinearRegression()
modeloComentarios.fit(atributos, comentario)

pickle.dump(modeloLikes, open('modeloLikes.sav', 'wb'))
pickle.dump(modeloCompartilhamentos, open('modeloCompartilhamentos.sav', 'wb'))
pickle.dump(modeloComentarios, open('modeloComentarios.sav', 'wb'))

