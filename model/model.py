from database.dao import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.dao = DAO()
        self.grafo=None

    def load_album_by_durata(self,durata):
        lista=self.dao.read_album_by_durata(durata)
        if len(lista)==0:
            print("Empty list")
            return []
        return lista

    def load_coppie(self):
        lista=self.dao.read_albums()
        if len(lista)==0:
            print("Empty list")
            return []
        return lista

    def build_graph(self,durata):
        self.grafo=nx.Graph()
        self.grafo.clear()
        lista_nodi_grezza=self.load_album_by_durata(durata)
        if len(lista_nodi_grezza)==0:
            print("Empty list")
            return []
        for n in lista_nodi_grezza:
            id=n["id"]
            title=n["title"]
            durata=n["durata"]
            self.grafo.add_node(id,title=title,durata=durata)
        lista_archi_grezza=self.load_coppie()
        if len(lista_archi_grezza)==0:
            print("Empty list")
            return []
        for n in lista_archi_grezza:
            id1=n["id1"]
            id2=n["id2"]
            if id1 in self.grafo and id2 in self.grafo:
                self.grafo.add_edge(id1,id2)
        return self.grafo

    def get_lista(self,id):
        componente=nx.node_connected_component(self.grafo,id)
        dimensione=len(componente)
        durata_tot=0
        for n in componente:
            durata=self.grafo.nodes[n]["durata"]
            durata_tot=durata_tot+durata
        return dimensione,durata_tot








