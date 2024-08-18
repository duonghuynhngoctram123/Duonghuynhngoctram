# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:05:20 2024

@author: Student
"""

s= float(input("Nhập quãng đường"))
if s <=1:
    a=20000
    print("Số tiền đi được trong km đầu tiên là ",)
elif s<=3:
    a=13000*s
    print("Số tiền taxi trong 3km đầu tiên là ",a)
if s<=8:
    a=3*13000+(s-3)*12000
    print("Số tiền của bạn là",a)
elif s>8:
    a=3*13000+4*12000+(s-7)*10000
    if a>10000:
        a=a-a*0.08
        print("tiền của bạn được giảm 8% là",a)
    else:
        print("so tien cua ban la",a)
 
    
        
        
    
    

    
    
    
    
        
