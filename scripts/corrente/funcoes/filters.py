
"""
Funcoes para limpeza de dados
oceanograficos. By gustavo viana
"""
import numpy
def remove_outliers(vector: numpy.ndarray, window: int) -> numpy.ndarray:
    

    length = len(vector)
    filteredVector = numpy.zeros_like(vector)
    filteredVector.fill(-99999) # preenchendo com valores invalidos
    
    for line in range(0,length,1):
        
        if ((line < window)|
            (line > length-window)):
            
            continue
        
        else:
            mean = numpy.nanmean(vector[line - window:
                                 line + window])
            
            std = numpy.nanstd(vector[line - window:
                               line + window])
            
            lowerLim = mean - 2*std
            upperLim = mean + 2*std
            
            # checa se o valor da linha esta no intervalo
            # de confiaca 
            
            if ((vector[line] > lowerLim) and
                (vector[line] < upperLim)):
                
                filteredVector[line] = vector[line]
                
    return filteredVector


# --------


def moving_avg(vector: numpy.ndarray, window: numpy.ndarray) -> numpy.ndarray:


    length = len(vector)
    filteredVector = numpy.copy(vector)
    filteredVector.fill(NaN)

    for line in range(0, length, 1):

        if ((line < window) or (line > (length-window))):

            continue


        else:
            
            mean = numpy.nanmean(vector[line - window: line + window])

            filteredVector[line] = mean

    return filteredVector





def main():
    
    print("Teste da Função moving_avg")
    
    myList = numpy.arange(1, 15, 1)
    
    filteredList = moving_avg(myList, 3)
    
    print(filteredList[:])
    print()

    
    # ---------------------------------------


    print("Teste Da Função remove_outliers")
    
    myList = numpy.arange(0, 2000, 1)
    
    # inserindo outliers na lista
    
    myList[51] = 350 # valor outlier
    
    print(f"Não filtrado: {myList[40:60]}")
    print()
    
    myListFiltered = remove_outliers(myList, 4)
    print(f"Filtrado: {myListFiltered[40:60]}")
    
    

if __name__ == "__main__":
    main()

