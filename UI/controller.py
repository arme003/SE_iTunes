import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model

    def handle_crea_grafo(self, e):
        durata=int(self.view.txt_durata.value)
        grafo=self.model.build_graph(durata)
        numero_nodi=self.model.grafo.number_of_nodes()
        numero_archi=self.model.grafo.number_of_edges()
        self.view.lista_visualizzazione_1.controls.clear()
        self.view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato: {numero_nodi} album,{numero_archi} archi\n"))
        self.view.update()


    def populate_dd_album(self,e):
        durata=int(self.view.txt_durata.value)
        lista=self.model.load_album_by_durata(durata)
        if len(lista)==0:
            print(f"Empty list")
            return []
        self.view.dd_album.options.clear()
        for n in lista:
            id=n["id"]
            title=n["title"]
            self.view.dd_album.options.append(ft.dropdown.Option(key=id,text=title))
        self.view.update()

    def get_selected_album(self, e):
        pass

    def handle_analisi_comp(self, e):
        id=int(self.view.dd_album.value)
        dimensione,durata=self.model.get_lista(id)
        self.view.lista_visualizzazione_2.controls.clear()
        self.view.lista_visualizzazione_2.controls.append(ft.Text(f"Dimensione componente: {dimensione}\n"
                                                                  f"Durata totale: {durata} minuti"))
        self.view.update()


    def handle_get_set_album(self, e):
        pass