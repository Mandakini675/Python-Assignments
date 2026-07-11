u1 = int(input("enter unit1:"))
u2 = int(input("enter unit2:"))
u3 = int(input("enter unit3:"))
u4 = int(input("enter unit4:"))
u5 = int(input("enter unit5:"))
u6 = int(input("enter unit6:"))

if u1>u2:
    if u1>u3:  
          if u1>u4:
                if u1>u5:
                    if u1>u6:
                         hs = u1
                    else:
                        hs = u6
                else: 
                   if u6>u5:
                     hs = u6
                   else:
                      hs = u5
            
          else:
                if u4>u5:
                    if u4>u6:
                       hs = u4
                    else:
                       hs = u6
                else:
                     if u5>u6:
                       hs = u5
                     else:
                       hs = u6
    else:
       if u3>u4:
             if u3>u5:
                  if u3>u6:
                     hs=u3
                  else:
                      hs= u6
             else:
                 if u5>u6:
                     hs=u5
                 else:
                    hs= u6
       else:
           if u4>u5:
                if u4>u6:
                    hs = u4
                else:
                    hs = u6
           else:
                 if u5>u6:
                       hs = u5
                 else:
                      hs = u6       
else:
    if u2>u3:
       if u2>u4:
           if u2>u5:
               if u2>u6:
                   hs= u2
               else:
                   hs = u6
           else:
               if u5>u6:
                     hs=u5
               else:
                    hs= u6
       else:
            if u4>u5:
                if u4>u6:
                    hs = u4
                else:
                    hs = u6
            else:
                 if u5>u6:
                       hs = u5
                 else:
                      hs = u6   
    else:
        if u3>u4:
             if u3>u5:
                  if u3>u6:
                     hs=u3
                  else:
                      hs= u6
             else:
                 if u5>u6:
                     hs=u5
                 else:
                    hs= u6
        else:
           if u4>u5:
                if u4>u6:
                    hs = u4
                else:
                    hs = u6
           else:
                 if u5>u6:
                       hs = u5
                 else:
                      hs = u6 

print("Highest Stock = ",hs)