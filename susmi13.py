x=int(input())
if x % 4 == 0:
   if x % 100 == 0:
     if x % 400 == 0:
     	print("{0}is an leap year")
     else:
    	print( "not leap year")
   else:
   	print(" leap year")
else:
	print(" not leap year")
  
