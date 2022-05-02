2010030385 kamani Nandini, [02-05-2022 12:12]
def xor(a, b):

  result = []

  for i in range(1, len(b)):
    if a[i] == b[i]:
      result.append('0')
    else:
      result.append('1')

  return ''.join(result)

def mod2div(dividend, divisor):
  pick = len(divisor)
  tmp = dividend[0 : pick]
  while pick < len(dividend):
    if tmp[0] == '1':
      tmp = xor(divisor, tmp) + dividend[pick]
    else:
      tmp = xor('0'*pick, tmp) + dividend[pick]
    pick += 1

  if tmp[0] == '1':
    tmp = xor(divisor, tmp)
  else:
    tmp = xor('0'*pick, tmp)
  checkword = tmp
  return checkword

def encodeData(data, key):

  l_key = len(key)

  appended_data = data + '0'*(l_key-1)
  remainder = mod2div(appended_data, key)

  codeword = data + remainder
  print("Remainder : ", remainder)
  print("Encoded Data (Data + Remainder) : ",
    codeword)
data = "100100"
key = "1101"
encodeData(data, key)

2010030385 kamani Nandini, [02-05-2022 12:12]
crc

2010030385 kamani Nandini, [02-05-2022 12:12]
n=int(input("Enter the no.of frames:"))
list1=[]
list2=[]
for i in range(0,n):
    x=input()
    list1.append(x)
    list2.append(len(x)+1)

sender=''
for i in range(0,n):
    print("frame",(i+1),"sent")
    print(str(list2[i])+list1[i]+'\n')

2010030385 kamani Nandini, [02-05-2022 12:12]
character count

2010030385 kamani Nandini, [02-05-2022 12:12]
list1=[]
flag='@'
esc='/'
a=input('Enter your message=')
list1.append(flag)
len1=len(a)
for i in a:
 if i=='@':
  list1.append(esc)
  list1.append(i)
 else:
  list1.append(i)
list1.append(flag)
print ('At senders side=',list1)
len1=len(a)
list2=[]
del list1[0],list1[len(list1)-1]
for i in range(0,len1,1):
 if a[i]=='#':
  list1.remove('#')
 else:
  list2.append(a[i])
print ('At recievers side=',list2)

# message = shreya@ch

2010030385 kamani Nandini, [02-05-2022 12:13]
byte stuffing

2010030385 kamani Nandini, [02-05-2022 12:13]
bits=[1,1,1,1,1,1]
stuffed=[]
count=0
for i in range(len(bits)):
    if bits[i]==1:
        count=count+1
        stuffed.append(bits[i])
    elif bits[i]!=1:
        count=0
        stuffed.append(bits[i])
    if count== 5:
            stuffed.insert(i,0)
print(stuffed)

2010030385 kamani Nandini, [02-05-2022 12:13]
bit stuffing

2010030385 kamani Nandini, [02-05-2022 12:13]
import math
message = int(input("Enter the message to be encrypted: "))

p = 11
q = 7
e = 3

n = p * q

def encrypt(msg):
    en = math.pow(msg, e)
    c = en % n
    print("Encrypted Message = ", c)
    #return c

print("Original Message = ", message)
encrypt(message)
#c = encrypt(message)

2010030385 kamani Nandini, [02-05-2022 12:14]
assymetric encryption-RSA