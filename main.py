import numpy as np
import matplotlib.pyplot as plt
import random

# Parâmetros
N = 40                      # tamanho do tabuleiro
power = 2                   # poder do anjo
max_turns = 200             # limite de jogadas

# Inicialização
board = np.zeros((N, N))
angel_pos = [N//2, N//2]
trajectory = [tuple(angel_pos)]
blocked_cells = []

def valid_moves(pos, power):
    moves = []
    for dx in range(-power, power+1):
        for dy in range(-power, power+1):
            if abs(dx) + abs(dy) <= power:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx, ny] == 0:
                        moves.append((nx, ny))
    return moves

for turn in range(max_turns):
    # Diabo bloqueia uma casa aleatória livre
    free_cells = list(zip(*np.where(board == 0)))
    free_cells.remove(tuple(angel_pos))
    if free_cells:
        block = random.choice(free_cells)
        board[block] = -1
        blocked_cells.append(block)
    
    # Movimento do Anjo
    moves = valid_moves(angel_pos, power)
    if not moves:
        print("O Diabo venceu!")
        break
    
    angel_pos = list(random.choice(moves))
    trajectory.append(tuple(angel_pos))
    
    print(f"Turno {turn+1}:")
    print(f"  Posição do Anjo: {angel_pos}")
    print(f"  Casas bloqueadas: {len(blocked_cells)}")
    print("-"*30)

else:
    print("O Anjo sobreviveu ao limite de turnos!")

# =======================
# Visualização Gráfica
# =======================

# =======================
# Visualização Gráfica
# =======================

plt.figure()
plt.title("Simulação do Problema do Anjo (k=2)")
plt.xlim(0, N)
plt.ylim(0, N)

# Plotar bloqueios (Diabo) em preto
if blocked_cells:
    bx, by = zip(*blocked_cells)
    plt.scatter(by, bx, color='black', marker='s', label='Bloqueios (Diabo)')

# Plotar trajetória do Anjo em vermelho
tx, ty = zip(*trajectory)
plt.plot(ty, tx, color='red', linewidth=2, label='Trajetória do Anjo')

# Posição final do Anjo
plt.scatter(angel_pos[1], angel_pos[0], color='red', s=100)

plt.gca().invert_yaxis()
plt.legend()
plt.show()
