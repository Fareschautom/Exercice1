class Voiture :
    def __init__(self,couleur,marque,statut):
        self.couleur=couleur
        self.marque=marque
        self.statut=statut
    
    def statutVoiture(self):
        print("la voiture {} {} {}".format(self.couleur,self.marque,self.statut))
    
    @property
    def statut(self):
        return self._statut
    
    @statut.setter
    def statut(self, nvxstatut):
        self._statut=nvxstatut

    
    @property
    def getmarque(self):
        return self._marque

    @getmarque.setter
    def marque(self, nvxmarque):
        self._marque=nvxmarque

      
    
 
Voiture1 = Voiture("rouge", "clio", "avance")
Voiture1.statutVoiture()
Voiture1.statut="en arret"
Voiture1.statutVoiture()
Voiture1.marque="clio2"
Voiture1.statutVoiture()