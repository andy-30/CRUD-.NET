class Procurar():


    def verifica(self,list):
        self.list = list
        dic = {}
        dic = {'par':[], 'impar':[], 'positivo':[], 'negativo':[],'zero':0}
        
        for i in range(0,len(self.list)):

            if self.list[i] %2 == 0:
                dic['par'].append(self.list[i])

                if self.list[i] > 0:
                    dic['positivo'].append(self.list[i])
                elif self.list[i] < 0:
                    dic['negativo'].append(self.list[i])

                else:
                    dic['zero'] +=1

            else:
                dic['impar'].append(self.list[i])

                if self.list[i] > 0:
                    dic['positivo'].append(self.list[i])
                elif self.list[i] < 0:
                    dic['negativo'].append(self.list[i])
                else:
                    dic['zero'] +=1

        return dic.items()
        
        

lista = [-1,-2,-3,-4,0,0,1,2,3,4]
procura = Procurar()
print (procura.verifica(lista))
