import hashlib
import datetime


print('''\n \n \n \t \t \t \t"Welcome to Patient Life Report" ''')
Name=input(" \n \n \n  \t Enter patient Name:  ")

class block():
    def __init__(self,data,id,x):
        self.data=data
        self.id=id
        self.x=x
        self.hash=self.gethash()
        
    def gethash(self):
        i=0
        while(1):
            es=(data+str(i)).encode()
            hs=(hashlib.sha256(es)).hexdigest()
            if(hs[:5]=="".zfill(5)):
                break
            
            i=i+1
            
        return hs 
    
    def printblock(self):
        if(id==0):
            bid="GENESIS BLOCK"
            prevhash="none"
        else:
            bid=self.id
            lastblock=self.x[-1]
            prevhash=lastblock["hash"]
        b={"id":bid,"hash":self.hash,"data":self.data,"prevhash":prevhash,"tstamp":datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S")}
        self.x.append(b)
        print("\n \n \t \t \t " +Name +" was suffering from " + data+ "!")
        print("\n \n ---------------------------------------------------------------------------------------------")
        return (self.x)
    
    

    
x=[] 
id=0
while(1): 
     
    data=input("\n \n Enter the patient's RESULT:  ")
    if (data=="Stop"):
        print("\n \t \t \t" + Name + " last suffered Disease Ended!")
            
        break
    else:
     Block=block(data,id,x)
     completeblockchain=Block.printblock()
     print(completeblockchain)
    id=id+1
    
    print(" --------------------------------------------------------------------------------------------")
    
print("\n***********************************************************************************************")
print("\n \n "+Name +" had suffered from following Disease !")     
print("the final blockchain is ",completeblockchain)
print("*************************************************************************************************")
print("\n \n \t \t \t Thank you !" + Name )
    

