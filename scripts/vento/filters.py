
"""
## -- Data Cleaning Functions --

Oceanographic data cleaning. By gustavo viana
jan/2022
"""

def remove_outliers(vector, window):
    
    from numpy import nanmean, nanstd
    from numpy import zeros_like, NaN
    from copy import copy
    # -------------------------------
    
    length = len(vector)
    filteredVector = zeros_like(vector)
    filteredVector.fill(-99999)
    
    for line in range(0, length, 1):
        
        if ((line < window)|
            (line > length-window)):
            
            continue
        
        else:
            meanValue = nanmean(vector[line - window:
                                 line + window])
            
            stdValue = nanstd(vector[line - window:
                               line + window])
            
            lowerLim = meanValue - 2*stdValue
            upperLim = meanValue + 2*stdValue
            
            if ((vector[line] > lowerLim) and
                (vector[line] < upperLim)):
                
                filteredVector[line] = vector[line]
        
    filteredVector[filteredVector == -99999] = NaN
                
    return filteredVector

# --


def moving_average(vector, window):

    from numpy import nanmean, NaN, copy

    length = len(vector)
    filteredVector = copy(vector)
    filteredVector.fill(NaN)

    for line in range(0, length, 1):

        if ((line < window) or (line > (length-window))):

            continue

        else:
            
            meanValue = nanmean(vector[line - window: line + window])

            filteredVector[line] = meanValue

    return filteredVector



def main():
    
    print(" -- function testing --")
    print("Moving Average")
    
    #import numpy as np
    
    #myList = np.arange(start=1,stop=16, step=1)
    
    #filteredList = moving_average(myList, 3)
    
    #print(filteredList[:])
    #print()

    
    # ---------------------------------------


    print("Remove outliers")
    
    #myList = np.arange(start=0, stop=2000, step=1);
    
    # inserindo outlier na lista
    #myList[22] = 180
    #myList[51] = 350
    
    #myListFiltered = remove_outliers(myList, 4)
    
    #print(f"Filtered Data: {myListFiltered[22]}\
    #    , Data:{myList[22]}")
    
    print()
    
    #print(f"Filtered Data: {myListFiltered[51]}\
    #    , Data:{myList[51]}")
    

if __name__ == "__main__":
    main()

