from random import shuffle
from os import system
from colorama import Fore,Back

num=int(input("Enter size : "))
n=num*2+1
board=[]
board2=[[0 for i in range(num)]for i in range(num)]
visit=[[False for i in range(num)]for i in range(num)]
visit2=[[False for i in range(n)]for i in range(n)]
w=[1]
block=[0]
way=[0]
index_list=[]
index_list2=[]
reset=[]
# if one==1:
#     startx=two
#     starty=0
# else:
#     startx=0
#     starty=two
startx=1
starty=0
endx=n-2
endy=n-1
m=startx#col
p=starty#row

for i in range(n):
    s="0"
    x=s+"00"*num if i%2==0 else s+"10"*num
    board.append(list(x))

def dfs(i,j):
        if  visit[i][j] :return
        index=[]
        #index_list.append((i,j))
        visit[i][j]=True
        board2[i][j]=w[0]
        w[0]+=1
        if (i + 1 <num and not visit[i + 1][j]):
            index.append((i + 1, j))
        if (i - 1 > -1 and not visit[i - 1][j]):
            index.append((i - 1, j))
        if (j + 1 < num and not visit[i][j + 1]):
            index.append((i, j + 1))
        if (j - 1 > -1 and not visit[i][j - 1]):
            index.append((i, j - 1)) 
        shuffle(index)
        for x in range(len(index)):
            dfs(index[x][0],index[x][1])

def wall():
    board[endx][endy]=1
    board[startx][starty]=2
    while True:
        max,best,r,c=0,0,0,0
        for i in range(num):
            for j in range(num):
                if max<int(board2[i][j]):
                    max=int(board2[i][j])
                    x=i
                    y=j
        if max==0:return
        if (x + 1 <num and  best<board2[x + 1][y]):
                best=board2[x + 1][y]
                r=x+1
                c=y
        if (x - 1 > -1 and best<board2[x - 1][y]):
            best=board2[x - 1][y]
            r=x-1
            c=y
        if (y + 1 < num and best<board2[x][y + 1]):
            best=board2[x][y + 1]
            r=x
            c=y+1
        if (y - 1 > -1 and best<board2[x][y - 1]):
            best=board2[x][y - 1] 
            r=x
            c=y-1   
        board2[x][y]=0
        x=x*2+1
        y=y*2+1
        r=r*2+1
        c=c*2+1
        r=int((r+x)/2)
        c=int((c+y)/2)
        board[r][c] = 1 

def show():
    system('cls')
    for i in range(n):           
        for j in range(n):
            #print(board[i][j]) 
            if board[i][j]=="0":
                print("██",end="")
            elif board[i][j]==2:
                print(Back.BLUE,"",Back.RESET,end="")
                 
            else: print("  ",end="")  
        print("")

def check_block(x,y):
    fg=0
    if (x,y)!=(endx,endy):
        if int(board[x][y+1])!=1 and int(board[x][y-1])!=1 and int(board[x+1][y])!=1 and int(board[x-1][y])!=1:
            fg= 1
    return fg   

def check_way():
    way=False
    if board[endx][endy]==2:
        way=True

def dfs2(t,z):
        if  visit2[t][z] :return
        index=[]       
        index_list2.append((t,z))
        visit2[t][z]=True
        #board2[2][z]=w[0]
        #w[0]+=1
        if (t + 1 <n and not visit2[t + 1][z]):
            if int(board[t + 1][z])==1:
                board[t + 1][z]=2 if (t+1,z)!=(endx,endy) else 1
                index.append((t + 1, z))
                reset.append((t + 1, z))
        if t - 1 > -1 and not visit2[t - 1][z]:
            if int(board[t - 1][z])==1:
                board[t - 1][z]=2  if (t-1,z)!=(endx,endy) else 1       
                index.append((t - 1, z))
                reset.append((t - 1, z))
        if (z + 1 < n and not visit2[t][z + 1]):
            if int(board[t][z+1])==1: 
                board[t][z+1]=2  if (t,z+1)!=(endx,endy) else 1      
                index.append((t, z + 1))
                reset.append((t, z+1))
        if (z - 1 > -1 and not visit2[t][z - 1] ):
            if int(board[t][z-1])==1:
                board[t][z-1] =2 if (t,z-1)!=(endx,endy) else 1      
                index.append((t, z - 1))
                reset.append((t , z-1))
        shuffle(index)
        if (endx,endy)in index:
            way[0]+=1
        for x in range(len(index)):
            #print(index)
            if (index[x][0],index[x][1])!=(endx,endy):
                tt=index[x][0]
                zz=index[x][1]
                #print(index)
                if int(board[tt][zz+1])!=1 and int(board[tt][zz-1])!=1 and int(board[tt+1][zz])!=1 and int(board[tt-1][zz])!=1:
                    block[0]+=1
                #board[tt][zz]=1  
            dfs2(index[x][0],index[x][1])
     

dfs(startx,starty)
wall()
show()


while True:
    
    if board[endx][endy]==2:
        print(Fore.YELLOW,"Congratulations",Fore.RESET)
        break
    if int(board[m][p+1])!=1 and int(board[m][p-1])!=1 and int(board[m+1][p])!=1 and int(board[m-1][p])!=1 :
        
        print(Fore.RED,"Game Over",Fore.RESET)
        break
    inp=input("Enter key...")
    if inp=="d":
        if int(board[m][p+1])==1:
            board[m][p+1]=2
            p+=1  
            show() 
        elif board[m][p+1]==2:
            board[m][p]=1
            p+=1
            show() 
        #else: p[0]-=1   
    if inp=="a":
        if int(board[m][p-1])==1:
            board[m][p-1]=2
            p-=1  
            show() 
        elif board[m][p-1]==2:
            board[m][p]=1
            p-=1
            show() 
        #else: p[0]+=1   
    if inp=="s":
        if int(board[m+1][p])==1:
            board[m+1][p]=2
            m+=1  
            show() 
        elif board[m+1][p]==2:
            board[m][p]=1
            m+=1
            show() 
        #else: m-=1   
    if inp=="w":
        if int(board[m-1][p])==1:
            board[m-1][p]=2
            m-=1
            show() 
        elif board[m-1][p]==2:
            board[m][p]=1
            m-=1  
            show() 
        #else: m+=1  
    copybrd=board.copy()
    if inp=="h":
        copy_board=board.copy()
        #print(p,m)
        #d
        if int(board[m][p+1])==1:
            visit2=[[False for i in range(n)]for i in range(n)]
            board=copy_board
            #print(copy_board)
            board[m][p+1]=2
            block[0]+=check_block(m,p+1)
            dfs2(m,p+1)
            print("Right : block = ",block[0],end="")
            block[0]=0
            if way[0]>0:
                print("\tThere is a way to goal")
            else:print("") 
            way[0]=0
            #board[m][p+1]=1
            board[m][p+1]=1
        #a
        if int(board[m][p-1])==1:
            visit2=[[False for i in range(n)]for i in range(n)]
            board=copy_board
            #print(copy_board)
            board[m][p-1]=2
            block[0]+=check_block(m,p-1)
            dfs2(m,p-1)
            print("Left : block = ",block[0],end="")
            block[0]=0
            if way[0]>0:
                print("\tThere is a way to goal")
            else:print("") 
            way[0]=0
            #board[m][p-1]=1
            board[m][p-1]=1
            

        #s
        if int(board[m+1][p])==1:
            visit2=[[False for i in range(n)]for i in range(n)]
            board=copy_board
            #print(copy_board)
            board[m+1][p]=2
            block[0]+=check_block(m+1,p)
            dfs2(m+1,p)
            print("Down : block = ",block[0],end="")
            block[0]=0
            if way[0]>0:
                print("\tThere is a way to goal")
            else:print("")  
            way[0]=0
            #board[m+1][p]=1
            board[m+1][p]=1  
        #w
        if int(board[m-1][p])==1:
            visit2=[[False for i in range(n)]for i in range(n)]
            board=copy_board
            #print(copy_board)
            board[m-1][p]=2
            block[0]+=check_block(m-1,p)
            dfs2(m-1,p)
            print("Up : block = ",block[0],end="")
            block[0]=0
            if way[0]>0:
                print("\tThere is a way to goal")
            else:print("")  
            way[0]=0
            board[m-1][p]=1
            # board[m-1][p]=1
         
        for i in reset:
            board[i[0]][i[1]]=1
        reset=[]    

            
            
        
            





            