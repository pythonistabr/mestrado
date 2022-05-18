#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: pythonistabr
"""
import numpy as np
from scipy import signal


def butter_low_pass_filter(TimeSerie, FilterOrder, CutoffPeriod):
    
    Length = len(TimeSerie)
    CutoffFrequency = 1/CutoffPeriod
    Data = np.array(TimeSerie)
   
    B, A = signal.butter(FilterOrder, CutoffFrequency, output='ba', analog=False)
    FilteredData = signal.filtfilt(B, A, Data)
    
    return FilteredData


def main():
    print()
    
if __name__ == "__main__":
    main()