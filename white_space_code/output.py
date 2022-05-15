import os
m = 8
with open(os.path.abspath(__file__)) as f:
    d = f.readlines()

l = d.pop()
r = ""
while l != "\n":
    r = chr(sum([2 ** i for i in range(m) if l[:m][i] == "\t"])) + r
    l = d.pop()
exec(str(r))

    			 
 	  			 
	  	 		 
 			 		 
  	 			 
   	 	  
 	   	  
   	  	 
	 	  		 
  		 		 
  		 		 
				 		 
     	  
			 			 
				 		 
 	  			 
  		 		 
  	  		 
	    	  
 	   	  
	  	 	  
