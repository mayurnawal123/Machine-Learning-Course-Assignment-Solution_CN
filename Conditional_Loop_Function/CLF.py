# Even Fibonacci Numbers
 ''' Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N. Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers. ''' 


 def fib_even(N):
  num = [1,1]
  iter = 2
  otp = []
  max_val = 0 

  while max_val < N:  
      num.append(num[iter-1] + num[iter -2])
      #print(num)
      if num[iter] % 2 ==0 :
        otp.append(num[iter])
      iter +=1  
      max_val = num[iter-1] + num[iter -2]
  return sum(otp) 
N = input()
c = fib_even(N)
print(c)

# Reversing Series Pattern
 '''Print the following pattern for the given number of rows ''' 
# Check if line is even or odd.
# Make variable start, end, inc/dec based on whether line is even or odd 
# Print using for loop 
# increment line variable after the print is OverflowError




''' 
Given a decimal number (integer N), convert it into binary and print.
The binary number should be in the form of an integer. ''' 


# to get binary from decimal 
N = int(input())
otp = None 
if N > 0: 
    while N >0: 
      rem_n = N%2
      new_n = N//2 
      if otp == None: 
        otp = str(rem_n)
      else: 
        otp = str(rem_n) + otp  
      N = new_n
    print(otp)
else: 
    print(0)



''' 
All prime numbers
Send Feedback
Given an integer N, print all the prime numbers that lie in the range 2 to N (both inclusive).
Print the prime numbers in different line ''' 

N = int(input())

prime_val = True 
otp = []
for iter in range(2,N+1): 
  for prev_iter in range(2,iter):
    #print('current value is', prev_iter)
    if iter % prev_iter ==0:
      prime_val = False
  if prime_val == True:
    print(iter)
    otp.append(iter)
    # print(otp)
  prime_val = True
#print(otp)



''' 
Trailing zeroes in n!
Send Feedback
Find and return number of trailing 0s in n factorial without calculating n factorial.
''' 


N = int(input())
#print ( N // 5 + N//25) 

no_zeros = 0
iter = 5 
while (N/iter>=1): 
    no_zeros += int(N/iter) 
    iter *= 5

print(int(no_zeros))









