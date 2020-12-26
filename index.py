from flask import Flask, render_template, request, redirect
import cx_Oracle
import random
import sys
app = Flask(__name__)


@app.route('/')
def home_page():
     return render_template('/home.html')



def wordBreak(dict, str):
 
    if not str:
        return True
 
    for i in range(1, len(str) + 1):
 
        prefix = str[:i]
        if prefix in dict and wordBreak(dict, str[i:]):
            return True
 
    return False



@app.route('/LCS',methods = ['GET','POST'])
def LCS_page():

     length = None
     if request.method == "POST":
         filename = "abc/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
     
         if f.mode == 'r':
              contents=f.readlines()
              X = contents[0]
              Y = contents[1]
              #print ("Length of LCS is: ", length)
              a = len(X) 
              b = len(Y) 
              c = [[None]*(b+1) for i in range(a+1)] 
  
              for i in range(a+1): 
                 for j in range(b+1): 
                      if i == 0 or j == 0 : 
                         c[i][j] = 0
                      elif X[i-1] == Y[j-1]: 
                          c[i][j] = c[i-1][j-1]+1
                      else: 
                          c[i][j] = max(c[i-1][j] , c[i][j-1]) #checks to see which value is maximum

              length = c[a][b]          
              
     return render_template('/LCS.html',length=length)

@app.route('/SCS',methods = ['GET','POST'])

def SCS_page():

     length = None
     if request.method == "POST":
         filename = "abc/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
     
         if f.mode == 'r':
              contents =f.readlines()
              X = contents[0]
              Y = contents[1]
              a = len(X)
              b = len(Y)
              dp = [[0] * (b + 2) for i in range(a + 2)]
              for i in range(a + 1):
                 for j in range(b + 1):
                     if (not i):
                         dp[i][j] = j
                     elif (not j):
                         dp[i][j] = i
                     elif (X[i - 1] == Y[j - 1]):
                         dp[i][j] = 1 + dp[i - 1][j - 1]
                     else:
                         dp[i][j] = 1 + min(dp[i - 1][j],dp[i][j - 1])
               
              length = dp[a][b]
         #print("Length of the shortest supersequence is:",length )
     return render_template('/SCS.html',length=length)

@app.route('/Levinshtein',methods = ['GET','POST'])
def levinshtein_page():

     length = None
     if request.method == "POST":
         filename = "abc/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
     
         if f.mode == 'r':
             contents =f.readlines()
             X = contents[0]
             Y = contents[1]
             a = len(X)
             b = len(Y)
             dp = [[0 for x in range(b + 1)] for x in range(a + 1)]
             for i in range(a + 1):
                 for j in range(b+ 1):
                     if i == 0:
                         dp[i][j] = j 
                     elif j == 0:
                         dp[i][j] = i
                     elif X[i-1] == Y[j-1]:
                         dp[i][j] = dp[i-1][j-1]
                     else:
                         dp[i][j] = 1 + min(dp[i][j-1],	dp[i-1][j],dp[i-1][j-1])
               
             length = dp[a][b]
                #print("Length of the shortest supersequence is:",length )
     return render_template('/Levenshtein.html',length=length)

@app.route('/LIS',methods = ['GET','POST'])
def LIS_page():

     length = None
     if request.method == "POST":
         filename = "deg/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             lis = [1]*count 
             for i in range (1, count): 
                 for j in range(0, i): 
                     if int(contents[i]) > int(contents[j]) and lis[i]< lis[j] + 1 : 
                         lis[i] = lis[j]+1
                         
             length = 0
             for i in range(count): 
                  length = max(length, lis[i]) 

     return render_template('/LIS.html',length=length)


@app.route('/MCM',methods = ['GET','POST'])
def MCM_page():

     length = None
     if request.method == "POST":
         filename = "deg/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             mcm = [[0 for x in range(count)] for x in range(count)] 
             for i in range(1, count): 
                  mcm[i][i] = 0
             
             for L in range(2, count): 
                 for i in range(1, count-L + 1): 
                     j = i + L-1
                     mcm[i][j] = sys.maxsize
                     for k in range(i, j): 
                         q = mcm[i][k] + mcm[k + 1][j] + int(contents[i-1])*int(contents[k])*int(contents[j]) 
                         if q < mcm[i][j]: 
                             mcm[i][j] = q 
             length = mcm[1][count-1]
     return render_template('/Matrix_Chain_Multiplication.html',length=length)

@app.route('/PP',methods = ['GET','POST'])
def PP_page():

     length = None
     if request.method == "POST":
         filename = "deg/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             sum = 0
             for i in range(0,count):
                 sum += int(contents[i])
 
             partition = [[True for i in range(count + 1)]for j in range(sum // 2 + 1)]
 
             for i in range(0, count + 1):
                 partition[0][i] = True
 
             for i in range(1, sum // 2 + 1):
                 partition[i][0] = False
 
             for i in range(1, sum // 2 + 1):
                 for j in range(1, count + 1):
                     partition[i][j] = partition[i][j - 1]
                     if i >= int(contents[j - 1]):
                         partition[i][j] = (partition[i][j] or partition[i - int(contents[j - 1])][j - 1])

             if partition[sum // 2][count] == True:
                 length = True
             else:
                  length = False 
             print(length)   
     return render_template('/Partition_Problem.html',length=length)


@app.route('/CCP',methods = ['GET','POST'])
def CCP_page():

     length = None
     if request.method == "POST":
         filename = "deg/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             change=123
             coins = [0 for k in range(change+1)] 
             coins[0] = 1
             for i in range(0,count): 
                 for j in range(int(contents[i]),change+1): 
                     coins[j] += coins[j-int(contents[i])]   
             length = coins[count]
     return render_template('/Coin_Change_Problem.html',length=length)

@app.route('/KSP',methods = ['GET','POST'])
def KSP_page():

     length = None
     if request.method == "POST":
         filename = "hf/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             W = 123
             count = count/2
             count = int(count)
             K = [[0 for x in range(W + 1)] for x in range(count + 1)] 
             for i in range(count + 1): 
                 for w in range(W + 1): 
                     if i == 0 or w == 0: 
                         K[i][w] = 0
                     elif int(contents[2*(i-1)]) <= w: 
                         K[i][w] = max(int(contents[(i-1)+1]) + K[i-1][w-int(contents[2*(i-1)])],K[i-1][w]) 
                     else: 
                         K[i][w] = K[i-1][w]
             length= K[count][W] 

     return render_template('/Knap_Sack_Problem.html',length=length)


@app.route('/RCP',methods = ['GET','POST'])
def RCP_page():

     length = None
     if request.method == "POST":
         filename = "hf/"
         filename = filename + request.form.get("input")
         f = open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             val = [0 for x in range(int(count/2)+1)] 
             val[0] = 0
  
             for i in range(1, int(count/2)+1): 
                max_val = 123 
                for j in range(i): 
                     max_val = max(max_val, int(contents[j]) + val[i-j-1]) 
                     val[i] = max_val 
             
             length = val[int(count/2)] 

     return render_template('/Rod_Cutting_Problem.html',length=length)

@app.route('/WBP',methods = ['GET','POST'])
def WBP_page():

     length = None
     if request.method == "POST":
         filename = "j/"
         filename = filename + request.form.get("input")
         #print(filename)
         f=open(filename,"r")
         count = 0

         if f.mode == 'r':
             for i in f:
                  count = count + 1
             f.close()
         
         f=open(filename,"r")
         if f.mode == 'r':
             contents =f.readlines()
             string1="adilasif"
             if wordBreak(contents,string1):
                 length = "Yes"
             else:
                  length = "No"
     return render_template('/Word_Breaking_Problem.html',length=length)



if __name__ == "__main__":
    app.run(debug=True)
