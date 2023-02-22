import pandas as pd 
import sys 

global df 
df = pd.DataFrame(index = range(1,51),columns = range(1,51))
df = df .fillna("")
global dic 





str = input()
eval(str)
#solution(str)

#def solution(commands):
    #cmd = list(commands)
    
    
    #return cmd
    
    
def UPDATE1 (r,c,value):
    df.loc[r,c] = value
    

def UPDATE2 (value1,value2):
    df_list = df.values.tolist()
    
    for i in range(0,49):
        
        matching = [ind for ind, value in enumerate(df_list[i]) if value == value1]
        if len(matching) >= 1 :
            for j in matching:
                df.loc[i+1,j+1] = value2

                
def MERGE(r1,c1,r2,c2):
    
