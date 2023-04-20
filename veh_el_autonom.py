#programa aparte que calcule, para cada estado, el número de vehículos eléctricos registrados, junto con la autonomía máxima y su marca:
#El programa funcionará necesariamente con la técnica map-reduce, que podemos poner en juego con la librería mrjob.

import sys
from mrjob.job import MRJob 

def calc_max(values):
        """
        example [1,'TSLA',5], [1,'RIVIAN',4],[1,'TSLA',3] ---> [3,'TSLA',5]
        """
        vmax   = 0
        vcount = 0
        make   = "" 
        for i,j,k in values:   
            if (float(k) >= float(vmax)):
                vmax  = k
                make = j
            vcount += 1 
        return [vcount, make, vmax ]
    
    
class MRVehiculosCount(MRJob):
    def mapper(self, _, line):
        elementos = (line.strip()).split(';')
        val = elementos[10]
        
        if (val.isnumeric()):
            val = elementos[10] 
        else: 
            val = int(0) 
        llave = str(elementos[3])
        make  =  str(elementos[6])
        yield llave, (1, make, val)
        
    def reducer(self, key, value):    
        yield  key, calc_max(value)
         

if __name__ == '__main__': 
    try: 
        MRVehiculosCount.run() 
    except:
        print('El código no se ha ejecutado correctamente.')