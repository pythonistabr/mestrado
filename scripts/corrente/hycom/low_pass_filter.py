#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:03:05 2022

@author: pythonistabr
"""
import numpy as np
from scipy import signal


def butter_low_pass_filter(Time_Serie, Filter_Order, Cutoff_Period):
    
    Length = len(Time_Serie)
    Cutoff_Frequency = 1/Cutoff_Period
    Data = np.array(Time_Serie)
   
    B, A = signal.butter(Filter_Order, Cutoff_Frequency, output='ba', analog=False)
    Filtered_Data = signal.filtfilt(B, A, Data)
    
    return Filtered_Data



def main():
    print()
    
if __name__ == "__main__":
    main()
    
    
