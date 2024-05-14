import sys
from tkinter import *
from dijkstra import *


class App:
    def __init__(self, root):
        self.entries = None
        self.root = root
        self.root.title("Algoritmo de Dijkstra")
        self.root.geometry('435x600')
        self.graph = Graph()
        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Vértice fuente").grid(row=0, column=0, padx=10, pady=10)
        Label(self.root, text="Vértice destino").grid(row=0, column=1, padx=10, pady=10)
        Label(self.root, text="Peso de la arista").grid(row=0, column=2, padx=10, pady=10)

        self.entries = []
        self.add_edge_fields()

        button_frame = Frame(self.root)
        button_frame.grid(row=100, column=0, columnspan=3)

        Button(button_frame, text="Agregar arista", command=self.add_edge_fields).pack(side=LEFT, expand=True, padx=50)
        Button(button_frame, text="Calcular rutas", command=self.calculate_routes).pack(side=LEFT, expand=True, padx=50)

    def add_edge_fields(self):
        row = len(self.entries) + 1
        src_entry = Entry(self.root)
        src_entry.grid(row=row, column=0, padx=5, pady=5, ipadx=5, ipady=1)

        dest_entry = Entry(self.root)
        dest_entry.grid(row=row, column=1, padx=5, pady=5, ipadx=5, ipady=1)

        weight_entry = Entry(self.root)
        weight_entry.grid(row=row, column=2, padx=5, pady=5, ipadx=5, ipady=1)

        self.entries.append((src_entry, dest_entry, weight_entry))

    def calculate_routes(self):

        num_vertices = 5
        for v in range(num_vertices):
            self.graph.add_vertex(v)

        for src_entry, dest_entry, weight_entry in self.entries:
            src_key = int(src_entry.get())
            dest_key = int(dest_entry.get())
            weight = int(weight_entry.get())

            # self.graph.add_vertex(dest_key)
            self.graph.add_edge(src_key, dest_key, weight)

        source = self.graph.find_vertex(0)
        dijkstra(self.graph, source)

        self.show_results()

    def show_results(self):
        result_window = Toplevel(self.root)
        result_window.title("Resultados de Dijkstra")
        result_window.geometry('400x400')

        Label(result_window, text="Vértice").grid(row=0, column=0)
        Label(result_window, text="Distancia").grid(row=0, column=1)
        Label(result_window, text="Predecesor").grid(row=0, column=2)

        for i, v in enumerate(self.graph.vertices):
            Label(result_window, text=f"{v.key}").grid(row=i+1, column=0)
            Label(result_window, text=f"{v.d}").grid(row=i+1, column=1)
            Label(result_window, text=f"{v.pi.key if v.pi else 'None'}").grid(row=i+1, column=2)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
