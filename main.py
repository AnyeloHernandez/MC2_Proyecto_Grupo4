import networkx as nx
import tkinter as tk
from tkinter import * 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


G = nx.Graph()
root = tk.Tk()
root.title("Algoritmo de busqueda de Anchura")
root.configure(bg="lightblue")
vertex_entry = tk.Entry(root)
vertex_entry.pack()
photo = PhotoImage(file = "R.png")
photoimage  = photo.subsample(3,3)
lupa = PhotoImage(file = "lupa.png")
lupaimage = lupa.subsample(3,3)
eye = PhotoImage(file = "eye.png")
eyeimage = eye.subsample(3,3)
lapiz = PhotoImage(file = "lapiz.png")
lapizimage = lapiz.subsample(3,3)
add_vertex_button=tk.Button(root, text="Agregar Vertice", font=("Lucida Console", 10, "bold"), image=photoimage, compound=LEFT, background='Turquoise', activebackground='blue', activeforeground='white', command=lambda:G.add_node(vertex_entry.get()))
add_vertex_button.pack()

edge_entry_1 = tk.Entry(root)
edge_entry_1.pack()
edge_entry_2 = tk.Entry(root)
edge_entry_2.pack()
add_edge_button = tk.Button(root, text="Agregar Arista", font=("Lucida Console", 10, "bold"), image=photoimage, compound=LEFT, background='Turquoise', activebackground='blue', activeforeground='white', command=lambda:G.add_edge(edge_entry_1.get(),edge_entry_2.get()))
add_edge_button.pack()

print_info_button = tk.Button(root, text="Mostrar datos agregados (terminal)", font=("Lucida Console", 10, "bold"), image=eyeimage, compound=LEFT, background='Turquoise', activeforeground='white', activebackground='blue', command=lambda:print("Número de nodos:", G.number_of_nodes(),"\nNumero de bordes:",G.number_of_edges()))
print_info_button.pack()

figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

def draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='r', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
        canvas.draw

draw_button = tk.Button(root, text="Dibujar grafo", font=("Lucida Console", 10, "bold"), image=lapizimage, compound=LEFT, background='Turquoise', activeforeground='white', activebackground='blue', command=draw_graph)
draw_button.pack()

def show_bfs():
    bfs_edges=list(nx.bfs_edges(G, source=vertex_entry.get()))
    draw_graph(bfs_edges)
    canvas.draw()

bfs_button = tk.Button(root, text="Busqueda de ancho", font=("Lucida Console", 10, "bold"), image=lupaimage, compound=LEFT, background='Turquoise', activeforeground='white', activebackground='blue', command=show_bfs)
bfs_button.pack()
root.mainloop()