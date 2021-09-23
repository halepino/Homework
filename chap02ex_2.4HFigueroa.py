# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:10:35 2021

@author: holly
"""

# DSC530
# Author: Figueroa, Holly
# Objective: USing variable totalwgt_lb, investigate whether first babies
# are lighter or heavier than others. Computre Cohen's d to quantify the 
# the difference between the groups. How does it compare to the difference
# in pregnancy length?


from __future__ import print_function

import sys
from operator import itemgetter

import nsfg
import first
import thinkstats2
import thinkplot


def compare_weights(live, firsts, non_first):
    
    mean1 = live.totalwgt_lb.mean()
  
    
    mean2 = firsts.totalwgt_lb.mean()
    var2 = firsts.totalwgt_lb.var()
    std2 = firsts.totalwgt_lb.std()
    
    mean3 = non_first.totalwgt_lb.mean()
    var3 = non_first.totalwgt_lb.var()
    std3 = non_first.totalwgt_lb.std()
          
    print("first births mean weight: ", mean2)
    print("non-first births mean weight: ", mean3)

    print("first births variance: ", var2)
    print("non-first births variance: ", var3)
    
    print("first births standard deviation: ", std2)
    print("first births standard deviation: ", std3)
    
    print("Difference relative to mean (% weight",
          (mean2 - mean3) / mean1 * 100)
    
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, non_first.totalwgt_lb)
    print("Cohen's d: ", d)
    
def main(script):
    
    # Read data file and specifcy fullterm births
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    
    # Divide data by first births vs others
    first_births = live[live.birthord == 1]
    non_first_births = live[live.birthord != 1]
    
    # Create histograms for weights compared for first born vs others
    firstwgt_hist = thinkstats2.Hist(first_births.totalwgt_lb, 
                                     label = 'First Born Weights')
    otherwgt_hist = thinkstats2.Hist(non_first_births.totalwgt_lb, 
                                     label = 'Non-First Born Weights')
    
    # Create plots for both groups
    thinkplot.Hist(firstwgt_hist)
    thinkplot.Show(xlabel = 'pounds', ylabel = 'frequency')
    thinkplot.Hist(otherwgt_hist)
    thinkplot.Show(xlabel = 'pounds', ylabel = 'frequency')
    
    # Get central measures for each group
    compare_weights(live, first_births, non_first_births)
    
     

if __name__ == '__main__':
    main(*sys.argv)
