import pickle

modeloLikes = pickle.load(open('modeloLikes.sav', 'rb'))
modeloCompartilhamentos = pickle.load(open('modeloCompartilhamentos.sav', 'rb'))
modeloComentarios = pickle.load(open('modeloComentarios.sav', 'rb'))

tipo = int(input('Informe o número do tipo da postagem Foto[0]|Link[1]|Status[2]|Video[3]: '))
mes = int(input('Mês: '))
dia = int(input('Dia da semana: D[1]|S[2]|T[3]|Q[4]|Q[5]|S[6]|S[7]: '))
hora = int(input('Hora: '))
pago = int(input('Pago: SIM[1]|NÃO[0]: '))

novoModelo =[[
    tipo, mes, dia, hora, pago
]]

resultadoLikes = modeloLikes.predict(novoModelo)
resultadoCompartilhamentos = modeloCompartilhamentos.predict(novoModelo)
resultadoComentarios = modeloComentarios.predict(novoModelo)

print('Média de Likes: ', int(resultadoLikes[0]))
print('Média de Compartilhamento: ', int(resultadoCompartilhamentos[0]))
print('Média de Comentários: ', int(resultadoComentarios[0]))