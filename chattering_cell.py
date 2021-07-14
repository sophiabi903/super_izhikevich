#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:39:32 2021

@author: sophiabi
"""

import izhikevich_cells as izh

class ccCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = 'Chattering'
        self.C = 50
        self.k= 1.5
        self.b= 1
        self.c=-40
        self.d=150
        self.vpeak=25
        
        
myCell = ccCell(4000)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)