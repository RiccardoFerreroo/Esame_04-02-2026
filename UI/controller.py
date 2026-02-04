from logging import exception

import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        try :
            valore =str(self._view.dd_ruolo.value)
            if valore == "None":
                raise Exception
        except Exception :
            self._view.show_alert("selezionare ruolo artista")
            return
        #print(valore)
        self._model.get_nodes(valore)
        self._model.build_graph()



    def handle_classifica(self, e):
        pass
    def get_ruoli(self):
        return self._model.get_ruoli()