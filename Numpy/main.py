'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

 

For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns. 
''' 

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    
    # check every row and compare with previous max value
    # for loop in number of rows and use function "sum"
    
    # check every column and compare with previous max value. 
    # for loop in columns and use function "sum"
    
    # 


    lar_val = -10**9 
    row_index =  0 
    for i in range(nRows):
      arr_sum = 0 
      for j in range(mCols):
        arr_sum = arr_sum + arr[i][j]
      # print(arr_sum)
      if arr_sum > lar_val :
        row_index = i 
      lar_val = max(lar_val , arr_sum)

    #print(row_index)
    arr_sum = 0
    lar_val_c = -10**9 

    for i in range(mCols):
      arr_sum = 0 
      for j in range(nRows):
        arr_sum = arr_sum + arr[j][i]
      #print(arr_sum)
      if arr_sum > lar_val_c :
        col_index = i 
      lar_val_c = max(lar_val_c , arr_sum)

    #print(col_index)


    if lar_val_c > lar_val: 
      print(str("column")+" "+ str(col_index) + " " + str(lar_val_c))

    else: 
      print(str("row")+" "+str(row_index) + " " + str(lar_val))


Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1








    ''' 
For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:

    ''' 


    from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    k = 0
    l = 0
    m = nRows
    n = mCols 
    a = mat
    # help -> Nikita Tiwari Code GeekforGeeks. 
  
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
  
    while (k < m and l < n): 
  
        # Print the first row from 
        # the remaining rows 
        for i in range(l, n): 
            print(a[k][i], end=" ") 
  
        k += 1
  
        # Print the last column from 
        # the remaining columns 
        for i in range(k, m): 
            print(a[i][n - 1], end=" ") 
  
        n -= 1
  
        # Print the last row from 
        # the remaining rows 
        # range will be from right to left 
        if (k < m): 
  
            for i in range(n - 1, (l - 1), -1): 
                print(a[m - 1][i], end=" ") 
  
            m -= 1
  
        # Print the first column from 
        # the remaining columns 
        # range will be from Bottom to Top. 
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                print(a[i][l], end=" ") 
  
            l += 1
  
  





























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1