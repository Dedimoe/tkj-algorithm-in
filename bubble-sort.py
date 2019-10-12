#program bubble sort
#2019-10-12

print 'mulai'
A=[7,8,1,0]
print A
n=4
i=0
while i<n:
  j=i
  while j<n:
     if A[i]>A[j]:
        print 'Tukar A[',i,'] dg A[',j,']'
        Tmp=A[i]
        A[i]=A[j]
        A[j]=Tmp

     j=j+1

  i=i+1

print A
print 'selesai'
