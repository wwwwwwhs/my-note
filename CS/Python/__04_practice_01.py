'''
_______________#########_______________________ 
______________############_____________________ 
______________#############____________________ 
_____________##__###########___________________ 
____________###__######_#####__________________ 
____________###_#######___####_________________ 
___________###__##########_####________________ 
__________####__###########_####_______________ 
________#####___###########__#####_____________ 
_______######___###_########___#####___________ 
_______#####___###___########___######_________ 
______######___###__###########___######_______ 
_____######___####_##############__######______ 
____#######__#####################_#######_____ 
____#######__##############################____ 
___#######__######_#################_#######___ 
___#######__######_######_#########___######___ 
___#######____##__######___######_____######___ 
___#######________######____#####_____#####____ 
____######________#####_____#####_____####_____ 
_____#####________####______#####_____###______ 
______#####______;###________###______#________ 
________##_______####________####______________ 

Descripttion: 实现1~100之间的偶数求和 
version: 0.1
Author: 崩布猪
Date: 2024-02-16 21:08:42
LastEditors: 崩布猪
LastEditTime: 2024-02-16 21:11:59
'''

sum = 0
for x in range(101):
    sum += x
print(sum)
num = 0
for x in range(2,101,2):
    num += x
print(num)