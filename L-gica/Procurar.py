class Procurar():
    
    def verifica(self,list):
        self.list = list
        par = []
        impar = []
        positivo = []
        negativo = []
        zero = 0
        verifica = {}
        for i in range(0,len(self.list)):
            
            if self.list[i] %2 == 0:
                par.append(self.list[i])
                
                if self.list[i] > 0:
                    positivo.append(self.list[i])
                elif self.list[i] < 0:
                    negativo.append(self.list[i])
                else:
                    zero +=1
            else:
                impar.append(self.list[i])
                
                if self.list[i] > 0:                
                    positivo.append(self.list[i])
                elif self.list[i] < 0:
                    negativo.append(self.list[i])
                else:
                    zero +=1

        verifica['par'] = (par)
        verifica['impar'] =(impar)
        verifica['positivo'] =(positivo)
        verifica['negativo'] = (negativo)
        verifica['zero'] = (zero)
        return verifica    
    
lista = [-1,-2,-3,-4,0,1,2,3,4]
a = Procurar()
print (a.verifica(lista))
