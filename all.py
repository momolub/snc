JOBSCHEDULING
def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
print("Following is maximum profit sequence of jobs")
printJobScheduling(arr, 3)
-----------------
MINIMUMSPANNINGTREE
INF = 9999999
V = 4
G = [[0, 2, 3, 4],
     [1, 0, 3, 4],
     [1, 2, 0, 4],
     [1, 2, 3, 0]]
selected = [0, 0, 0, 0]
edge = 0
selected[0] = True
print("Edge : Weight\n")
while (edge < V - 1):
    min = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if min > G[i][j]:
                        min = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    edge += 1
    -----------------
    OBST
    def optCost(freq, i, j):
    if j < i:
        return 0
    if j == i:
        return freq[i]
    fsum = Sum(freq, i, j)
    Min = 999999999999

    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1) +
                optCost(freq, r + 1, j))
        if cost < Min:
            Min = cost
    return Min + fsum

def optimalSearchTree(keys, freq, n):
    return optCost(freq, 0, n - 1)

def Sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s

if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print("Cost of Optimal BST is",
          optimalSearchTree(keys, freq, n))
   ---------------------
  GREEDYKNAPSACK
  class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:

    @staticmethod
    def getMaxValue(wt, val, capacity):
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
        iVal.sort(reverse=True)

        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue


if __name__ == "__main__":
    wt = []
    n = int(input("Enter weights:"))
    for i in range(0,n):
        ele = int(input())
        wt.append(ele)
    num = int(input("Enter values:"))
    val = []
    for i in range(0, num):
        el = int(input())
        val.append(el)

    capacity = int(input("Enter capacity"))
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
    -------------------
    quicksort
    def partition(arr, low, high):
  i = (low-1)     # index of smaller element
  pivot = arr[high]   # pivot
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)
def quickSort(arr, low, high):
  if len(arr) == 1:
    return arr
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
  ele = int(input())
  arr.append(ele)
print(arr)
l = len(arr)
quickSort(arr, 0, l-1)
print("Sorted array is:")
for i in range(l):
  print("%d" % arr[i])
  ------------------------
  mergesort
  def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
def printList(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()
if __name__ == '__main__':
  arr= []
  n = int(input("NO of integers:"))
  for i in range (0,n):
      ele = int(input())
      arr.append(ele)
  print(arr)
  print("Given array is", end="\n")
  printList(arr)
  mergeSort(arr)
  print("Sorted array is: ", end="\n")
  printList(arr)
  -----------------------
  stringmatchingrabin
  d = 256
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(N - M + 1):

        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
            if j == M:
                print("Pattern found at index " + str(i))

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            if t < 0:
                t = t + q
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101
search(pat, txt, q)
---------------
KNAPSACKBACKTRACKING
import sys
import math

sys.setrecursionlimit(10 ** 8)

c = 0


def knapSack(mW, w, v, n):
    global c
    c += 1

    if (mW == 0 or n == 0):
        return [0, []]

    if (w[n - 1] > mW):
        return knapSack(mW, w, v, n - 1)

    set1 = knapSack(mW - w[n - 1], w, v, n - 1)
    set2 = knapSack(mW, w, v, n - 1)

    if (set1[0] + v[n - 1] > set2[0]):
        set1[1].append(n - 1)
        set1[0] += v[n - 1]
        return set1
    else:
        return set2


val = [160, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print("Knapsack Max & list:", knapSack(W, wt, val, n))
print("Total Recursive Steps: ", c)
--------------
N-QUEENS
global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j],end=' ')
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def solveNQ():
    board = [ [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
    printSolution(board)
    return True

solveNQ()
----------------
GRAPHCOLORING
class Graph():
    def init(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] \
                      for row in range(vertices)]

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False

        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=' ')
        return True

g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.graphColouring(m)
