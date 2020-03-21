#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:16:00 2019

@author: bsibanda
#"""
##
#annual_salary=float(input("Enter your annual salary here"))
#monthly_salary= annual_salary /12
#portion_saved=float(input ("Enter the  portion of your monthly savings you want to save"))
#total_cost=float(input( "Enter the cost of your dream house here"))
#portion_downpayment= 0.25*total_cost
#monthly_saved=monthly_salary*portion_saved
#current_saving = 0.0
#number_of_months=0 
#while current_saving <= portion_downpayment:
#    number_of_months+=1 #because money is ended at the end of the month
#    
#    current_saving *= (1+(0.04/12)) #1  QSTN WHY IS IT THAT WHEN I CHANGE WHICH COMES FIRST I GET DIFFERENT ANSWERS
#    current_saving += monthly_saved #2
#
#print("Number of months to save =", number_of_months)
#
#
#With NEw changes with inspiration from kaizerflow github
annual_salary=int(input("Enter your annual salary:"))
percent_saved= int(input("Enter the percent of salary to save"))
total_cost= int(input("Enter the cost of your dreamhouse"))

#static data
portion_down_payment= 0.25(total_cost)
monthly_return = 0.04/12

#data that will change
current_savings = 0.0
monthly_salary= annual_salary/12
#semi_annual_raise = float(0.07)
#annual_return= float(0.04)
#cost_of_house=(1000000)
#downpayment= 0.25*cost_of_house
#annual_salary=float(input("Enter your initial annual salary here"))
#monthly_salary=annual_salary/12
#epsilon=100
#current_saving = 0.0
#number_of_months=1 
#low = 0 
#high = 10000
#guess= (high +low)/2
#
#while current_saving <= downpayment and abs(downpayment-current_saving)>=epsilon:
#    monthly_saved_percent=monthly_salary*guess
#    # print(monthly_saved_percent)
#    monthly_saved= monthly_saved_percent/10000
#    print(monthly_saved)
#    current_saving = current_saving + monthly_saved + (4/12)*(current_saving
#                                                       + monthly_saved)
#    number_of_months+=1 
#    print(current_saving)
#    print(number_of_months)
#        
#    if number_of_months%6==0:
#        monthly_salary=(1 + semi_annual_raise)*monthly_salary
#        print(monthly_saved)
#          
#    if number_of_months>36:
#       low=guess   
#    elif number_of_months<36 :
#        high= guess 
#    else: 
#        print(number_of_months)
#    
#print("The number of months" ,number_of_months)
#
#
