import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Labirinto:
    def __init__(self):
        plt.rcParams['toolbar'] = 'None'
        self.TAMANHO_MATRIZ = 10
        self.labirinto = np.random.randint(-100, 101, size=(self.TAMANHO_MATRIZ, self.TAMANHO_MATRIZ, self.TAMANHO_MATRIZ))
        self.visitados = []
        self.max_coletas = 1000
        self.maior_valor = -float('inf')
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def coletar_backtracking(self, xi, yi, zi, xf, yf, zf):
        stack = [(xi, yi, zi, 0, 0)]  # (x, y, z, valor_atual, coletas)

        while stack:
            xi, yi, zi, valor_atual, coletas = stack.pop()

            if coletas >= self.max_coletas or (xi, yi, zi) in self.visitados:
                continue

            if xi == xf and yi == yf and zi == zf:
                if valor_atual > self.maior_valor:
                    self.maior_valor = valor_atual
                    self.visitados.append((xi, yi, zi))
                continue

            if 0 <= xi < self.TAMANHO_MATRIZ and 0 <= yi < self.TAMANHO_MATRIZ and 0 <= zi < self.TAMANHO_MATRIZ:
                self.visitados.append((xi, yi, zi))
                valor_atual += self.labirinto[xi][yi][zi]
                coletas += 1

                if valor_atual > self.maior_valor:
                    self.maior_valor = valor_atual

                self.ax.clear()

                self.ax.scatter(xf, yf, zf, c='green', marker='D')

                for x, y, z in self.visitados:
                    self.ax.scatter(x, y, z, c='black', marker='.')
                self.ax.scatter(xi, yi, zi, c='red', marker='o')
                self.ax.set_xlabel('X')
                self.ax.set_ylabel('Y')
                self.ax.set_zlabel('Z')
                self.ax.set_title(f'Total coletado até agora: {valor_atual}\nTotal de coletas até agora: {coletas}')
                plt.pause(0.1)

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        for dz in [-1, 0, 1]:
                            nx, ny, nz = xi + dx, yi + dy, zi + dz
                            stack.append((nx, ny, nz, valor_atual, coletas))
                            if nx == xf and ny == yf and nz == zf:
                                stack = []  # Limpa a pilha para sair do loop

    def plotar_labirinto(self):
        plt.show()

if __name__ == '__main__':
    lab = Labirinto()
    xf, yf, zf = np.random.randint(0, 10, size=3)
    print(f"Posição final: ({xf}, {yf}, {zf})")
    lab.coletar_backtracking(0, 0, 0, xf, yf, zf)
    print("Maior valor coletado:", lab.maior_valor)
    lab.plotar_labirinto()
