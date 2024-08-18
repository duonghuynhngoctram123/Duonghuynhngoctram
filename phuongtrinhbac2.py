# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:25:26 2024

@author: Student
"""

import math
print("giải phương trình bậc 2: ax^2 + bx + c = 0")
a= float(input("Nhập a="))
b= float(input("Nhập b="))
c= float(input("nhập c="))
delta = b**2 -(4*a*c)
if delta < 0:
      print("Phương trình vô nghiệm")
elif delta > 0:
      print("Phương trình có hai nghiệm phân biệt x1= ",(-b+math.sqrt(delta))/(2*a)) 
      print ("Phương trình có hai nghiệm phân biệt x2=",(-b-math.sqrt(delta))/(2*a))
elif delta ==0:
    print("phương trình có nghiệm kép x1=x2",-b/2*a)      

     
    
             

