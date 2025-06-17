import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

def simult_toppling(C):
    D = np.empty_like(C)
    np.copyto(D,C)
    c_nodes = []
    for i in range(N):
        for j in range(N):
            if C[i+1][j+1]>3:
                c_nodes.append(i+1)
                c_nodes.append(j+1)


    m = 0
    while m<(len(c_nodes)-1):
        i = c_nodes[m]
        j = c_nodes[m+1]
        D[i][j] -= 4
        D[i-1][j] += 1
        D[i+1][j] += 1
        D[i][j-1] += 1
        D[i][j+1] += 1

        m += 2

    return D   

def valid_topplings(A):
    number_ = 0
    for i in range(N):
        for j in range(N):
            if A[i+1][j+1]>3:
                number_ += 1
    return number_

        
N = 6
r_i = 3
r_j = 4
A = np.ones((N+2,N+2), np.int8)
A = 3*A
A[r_i][r_j] += 1

matr_list = [A]

A_ = np.delete(A, N+1,0)
A_ = np.delete(A_, N+1,1)
A_ = np.delete(A_, 0, 0)
A_ = np.delete(A_, 0, 1)
tr_matr_list = [A_]

k_ = 1

while k_>0:
    B = simult_toppling(matr_list[-1])
    matr_list.append(B)
    k_ = valid_topplings(B)

    B_ = np.delete(B, N+1,0)
    B_ = np.delete(B_, N+1,1)
    B_ = np.delete(B_, 0, 0)
    B_ = np.delete(B_, 0, 1)
    tr_matr_list.append(B_)
   
print(tr_matr_list)

# plot the evolution
fig, ax = plt.subplots(int(len(tr_matr_list)/3)+1,3)

#ims = []
k = 0
while k < len(tr_matr_list):
    # im = plt.matshow(tr_matr_list[k], vmin=0, vmax = 7)
    # ims.append([im])
    cax = ax[int(k/3),k-3*int(k/3)].matshow(tr_matr_list[k], vmin=0, vmax = 7, cmap='Set3')
    # plt.colorbar(cax) - #лента с цветове до всяка графика
    k += 1 

for ax_ in ax.flat[len(tr_matr_list):]:
    ax_.remove()

values = [0, 1, 2, 3, 4, 5, 6, 7]
colors = [ cax.cmap(cax.norm(value)) for value in values]
# create a patch (proxy artist) for every color 
patches = [ mpatches.Patch(color=colors[i], label="{l} grains".format(l=values[i]) ) for i in range(len(values)) ]
# put those patched as legend-handles into the legend
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )

#ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=1000)

plt.show()