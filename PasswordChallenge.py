#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:55:50 2019

@author: christophercatzin
"""

# ============================= PASSWORD VALIDATION ==========================

def password_chk(password): 
      
    Sig = ['7']
    SpecialSym =['$', '@', '#', '%','!', '~'] 
    value = True
      
    # SHOULD HAVE THE LENGTH AT LEAST 5
    if len(password) < 5: 
        print('Length should be at least 5') 
        value = False
          
    # SHOULD NOT BE GREATER THAN 9    
    if len(password) > 9: 
        print('length should be not be greater than 9') 
        value = False
          
    # GETS THE CHARACTERS FROM THE PASSWORD
    # AND CHECKS IF IT HAS AT LEASE 1 NUMBER
    if not any(char.isdigit() for char in password): 
        print('Password should have at least one numeral') 
        value = False
    
    # CHECKS IF THE PASSWORD HAS AT LEAST ONE UPPERCASE      
    if not any(char.isupper() for char in password): 
        print('Password should have at least one uppercase letter') 
        value = False
          
    # CHECKS IF THE PASSWORD HAS AT LEAST ONE LOWER CASE
    if not any(char.islower() for char in password): 
        print('Password should have at least one lowercase letter') 
        value = False
    
    # CHECKS IF THE PASSWORD HAS ONE OF THE SPECIAL CHARACTERS      
    if not any(char in SpecialSym for char in password): 
        print('Password should have at least one of the symbols $@#') 
        value = False
        
    if not any(char in Sig for char in password): 
        print('Password does not contain signature!') 
        value = False
        
    if value: 
        return value
    
    
  
# ================================ MAIN METHOD! =============================
        
# THIS GETS THE INPUT PASSWORD, AND VALIDATES IT FROM THE password_chk function
def main(): 
    password = input("Enter your password: ")
      
    if (password_chk(password)): 
        print("================= PASSWORD IS VALID! =====================") 
    else: 
        print("================ PASSWORD IS INVALID! ====================") 
          
# =============================== DRIVE CODE =================================       
if __name__ == '__main__': 
    main()  