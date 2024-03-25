# -*- coding: utf-8 -*-
# Todas as extensões devem implementar esta interface.
# As implementações devem ser chamadas de BurpExtender, no pacote Burp, devem ser declaradas públicas e devem fornecer um construtor padrão (público, sem argumentos).
from burp import IBurpExtender


class BurpExtender(IBurpExtender):

    # Implementando a classe IBurpExtender

    def registerExtenderCallbacks(self, callbacks):
        # Este método é usado quando a extensão é carregada
        callbacks.setExtensionName("Hello World2")
        # Nome da extensão
        for x in xrange(1, 100):
            # Criei um loop que vai printar 'hi' de 0 a 100
            string = "hi " + str(x)
            callbacks.printOutput(string)
        return
