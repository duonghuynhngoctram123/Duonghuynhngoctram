# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:19:23 2024

@author: Student
"""


a= float(input("Nhập a"))
b= float(input("Nhập b"))
c= float(input("Nhập c"))
if a+b>c and b+c>a and a+c>b:
    print("Đây là một tam giác")
    if a==b==c:
        print("Đây là tam giác đều")
    elif a==b or a==c or b==c:
        print("Đây là tam giác cân")  
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
        print("Đây là tam giác vuông")
    
    
     
    
    
    
    