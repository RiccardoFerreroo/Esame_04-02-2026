import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.dao = DAO()
    def get_nodes(self, role):
        print("model chiamato")
        self.artists = self.dao.get_artists(role)
        print("artists: ", len(self.artists))
        return self.artists
    def build_graph(self, role: str):
        self.G = nx.DiGraph()
        self.G.add_nodes_from(self.artists)
        #print(self.G.number_of_nodes())


    def classifica(self):
        pass
    def get_ruoli(self):
        #print('model chiamato')
        return self.dao.get_ruoli()
