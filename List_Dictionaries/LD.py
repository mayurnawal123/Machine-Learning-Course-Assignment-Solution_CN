''' 
Leaders in array
Send Feedback
Given an integer array A of size n. Find and print all the leaders present in the input array. An array element A[i] is called Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
Print all the leader elements separated by space and in the same order they are present in the input array.
''' 



A = [1,3,10,7,0]
otp = []
for item,val in enumerate(A):
  if val >= max(A[item:]):
    otp.append(val)

def leaderprint(arr, n):
  for i in range(0, n):
    for j in range(i, n):
      if (arr[i] < arr[j]):
        break
      if (j == n - 1):
        otp.append(arr[i])
  print(arr)
  return(otp)
print(leaderprint(A,len(A)))


''' 
Reverse string Word Wise
Send Feedback
Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is.
''' 


A = "Hello I am Shreyashish Sengupta"
otp = None 
A = A.split()
#print(A)
for iter, word in enumerate(A):
  if iter ==0:
    otp = word 
  else :
    otp = word + " "+ otp 
#print(str(otp))




# Python3 program to reverse a string
 
# Function to reverse each word in the string
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1
 
s = input()
 
# Convert string to list to use it as a char array
s = list(s)
start = 0
while True:
     
    # We use a try catch block because for
    # the last word the list.index() function
    # returns a ValueError as it cannot find 
    # a space in the list
    try:
        # Find the next space
        end = s.index(' ', start)
 
        # Call reverse_word function
        # to reverse each word
        reverse_word(s, start, end - 1)
 
        #Update start variable
        start = end + 1
 
    except ValueError:
 
        # Reverse the last word
        reverse_word(s, start, len(s) - 1)
        break
 
# Reverse the entire list
s.reverse()
 
# Convert the list back to
# string using string.join() function
s = "".join(s)
 
print(s)
 
''' 
Maximise the sum
Send Feedback
Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return the maximum sum.
That is, we can switch from one array to another array only at common elements.
If no intersection element is present, we need to take sum of all elements from the array with greater sum.
''' 
lena = input()   
# take multiple inputs in array 
A = [ int(x) for x in input().split()] 
lenb = input()
B = [ int(x) for x in input().split()]

sum_max = 0

for iter, val in enumerate(A):
  #print(A)
  #print(B)
  if len(A) >0 and len(B) > 0:
    if val in B:
      indx = B.index(val)
      iter = A.index(val)
      #print(indx)
      if sum(B[:indx+1])>= sum(A[:iter+1]):
        sum_max = sum_max + sum(B[:indx+1])
        #print(sum_max)
        #print("from B value is taken")
        
      else :
        sum_max = sum_max + sum(A[:iter+1])
        #print(sum_max)
        #print("value taken from A")

      A = A[iter+1:]
      B = B[indx+1:]
      #print(A)
      #print(B)
  else: 
    break
if len(A) == 0  and len(B) == 0: 
  sum_max  = sum_max
if len(A) == 0 and len(B) != 0:
  sum_max  = sum_max + sum(B)
if len(B) == 0 and len(A) != 0:
  sum_max  = sum_max + sum(A)   
if len(B) > 0 and len(A) > 0:
  sum_max  = sum_max + max(sum(A),sum(B))


print(sum_max)

''' 
Largest Unique Substring
Send Feedback
Given a string S, find the largest substring with no repetition i.e. largest substring which contain all unique characters.
'''

# max sub string. 
A = 'abcdef'
curr_word = []
max_len = 0 
indx = -1 
A = input()
for iter, val in enumerate(A):
  print(val)
  if val in curr_word:
    indx = curr_word.index(val)
    #print(indx+1)
    #print(iter)
    max_len = max(max_len, len(curr_word))

  curr_word = A[indx+1:iter+1]
  #print(curr_word)
  #print(indx+1)
  #print(iter)
if curr_word == A:
  max_len = len(A)
else :
  max_len = max_len 
#print(curr_word)
#print(max_len)



