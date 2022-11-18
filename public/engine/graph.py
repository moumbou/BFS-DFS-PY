from dataclasses import dataclass

# ICI ON VA UTILISEZ LA METHODE DATACLASS QUI EST BCP PLUS 
# SIMPLE A UTILISER POUR CREER UNE CLASS
@dataclass
class Graph:
    # LES ENTRES GRAPH ET INDEX SONT DES LISTES VIDE POUR LES UTILISER TEMPORAIREMENT
    graph: list
    index: list
    # NEWLIST EST UN DICTIONNAIRE AVEC LE QUEL ON VA STOCKER LE RESULTAT FINAL
    newList: dict

    # ON DEFINI UNE FONCTION CONVERTTOGRAPH QUI VA PRENDRE COMME PARAMETRE SELF
    # AFIN DACCEDER LES VARIABLE GRAPH,INDEX,NEWLIST ET MEME LA FONCTION EN ELLE MEME
    def convertToGraph(self) -> dict:
        # DANS CETTE LOOP ON VA RETIRER TOUT LES INDEX DE LA LISTE
        # DU DICTIONNAIRE DONNE SANS REPITION
        # EN DAUTRE TERME ON AURA PAS DEUX INDEX OU CLE DU MEME TYPE
        # EXP : [0,0,1,2,2] MAIS PLUS TOT [0,1,2] SEULEMENT
        for n in self.graph:
            for i in n:
                if i not in self.index:
                    self.index.append(i)

        # APRES AVOIR OBTENU TOUT LES INDEX QUI EXISTE DANS LA LISTE
        # ON VA POUVOIR TRIER LES NOEUDS
        for i in self.index:
            # CECI EST UNE LISTE TEMPORAIRE QUI SE REINITIALISE A 
            # CHAQUE DEBUT DE LA LOOP
            tempList=[]
            for node in self.graph:
                # LE IF ICI EST TRES IMPORTANT POUR EVITER 
                # QUE NOTRE LOOP NE CASSE
                if i in node:
                    tempList.append(node[i])
            # APRES AVOIR TRIER LES NOEUDS DE LA MEME CLE 
            # OU INDEX ON VA POUVOIR INSERER LE TOUT DANS NOTRE DICTIONNAIRE
            self.newList[i]=tempList
        
        # ON RETOURNE LE RESULTAT SOUS FORME DE DICTIONNAIRE ET VOILA !
        return self.newList