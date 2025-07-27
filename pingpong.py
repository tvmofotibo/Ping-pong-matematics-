import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
def aumentar(x,y):
	sinalx=1
	sinaly=1
	if(x<0):
		sinalx=-1
		x=x*-1
	if(y<0):
		sinaly=-1
		y=y*-1
	porcentagemx=random.uniform(5,50)
	porcentagemy=random.uniform(5,50)
	aumentox=x * (porcentagemx/100)
	finalx=x+aumentox
	finalx=finalx*sinalx
	aumentoy=y * (porcentagemy/100)
	finaly=y+aumentoy
	finaly=finaly*sinaly
	return finalx, finaly

# Configurações iniciais
L_x, L_y = 500, 500  # Tamanho da tela
barra_x = 0          # Posição X fixa da barra
barra_y = L_y / 2     # Posição Y inicial da barra
largura_barra = 10
altura_barra = 50

l_barra_x_i = barra_x - largura_barra / 2 # esquerda da barra
l_barra_x_f = barra_x + largura_barra / 2  # direita da barra

a_barra_y_i = barra_y - altura_barra / 2   # topo da barra
a_barra_y_f = barra_y + altura_barra / 2   # base da barra


bola_x, bola_y = L_x / 2, L_y / 2  # Posição inicial da bola
tamanho_bola = 10

largura_bola_x_i = bola_x - tamanho_bola / 2
largura_bola_x_f = bola_x + tamanho_bola / 2

altura_bola_y_i = bola_y - tamanho_bola / 2
altura_bola_y_f = bola_y + tamanho_bola / 2

V_x, V_y =1, 1# Velocidade da bola
V_x_o, V_y_o=V_x, V_y
# Configuração da figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, L_x)
ax.set_ylim(0, L_y)
ax.set_aspect('equal')
ax.axis('on')  # Remove os eixos

# Cria os objetos gráficos
barra = Rectangle((barra_x - largura_barra/2, barra_y - altura_barra/2),
                  largura_barra, altura_barra, fc='blue')
bola = Rectangle((bola_x - tamanho_bola/2, bola_y - tamanho_bola/2),
                 tamanho_bola, tamanho_bola, fc='red')

ax.add_patch(barra)
ax.add_patch(bola)


# Função de animação
def update(frame):
    global bola_x, bola_y, V_x, V_y, V_x_o, V_y_o
    
    # Atualiza posição da bola
    bola_x += V_x
    bola_y += V_y
    
    # Verifica colisões com as bordas
    if bola_x - tamanho_bola/2 <= 0 or bola_x + tamanho_bola/2 >= L_x:
        V_x *= -1
        V_x, V_y=aumentar(V_x, V_y)
    if bola_y - tamanho_bola/2 <= 0 or bola_y + tamanho_bola/2 >= L_y:
        V_y *= -1
        V_x, V_y=aumentar(V_x, V_y)
    
    # Verifica colisão com a barra
    barra_esq = barra_x - largura_barra/2
    barra_dir = barra_x + largura_barra/2
    barra_topo = barra_y - altura_barra/2
    barra_base = barra_y + altura_barra/2
    
    bola_esq = bola_x - tamanho_bola/2
    bola_dir = bola_x + tamanho_bola/2
    bola_topo = bola_y - tamanho_bola/2
    bola_base = bola_y + tamanho_bola/2
    
    
    if (bola_esq <= barra_dir and 
        bola_dir >= barra_esq and
        bola_base >= barra_topo and
        bola_topo <= barra_base):
        V_x *= -1
        V_x, V_y=aumentar(V_x, V_y)
    #verifica se o valor da velocidade esta maior que o valor original
    if(V_x >= 5 or V_y >= 5):
    	V_x=V_x_o
    	V_y=V_y_o
    
    # Atualiza posição gráfica da bola
    bola.set_xy((bola_x - tamanho_bola/2, bola_y - tamanho_bola/2))
    return barra, bola

# Controle da barra com o mouse
def on_mouse_move(event):
    global barra_y
    if event.inaxes == ax:
        barra_y = event.ydata
        # Mantém a barra dentro da tela
        barra_y = max(altura_barra/2, min(L_y - altura_barra/2, barra_y))
        barra.set_y(barra_y - altura_barra/2)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

# Inicia a animação
ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True)
plt.title('Jogo de Ping Pong')
plt.tight_layout()
plt.show()