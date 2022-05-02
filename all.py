2010030385 kamani Nandini, [02-05-2022 12:06]
import math
key=input("Enter keyword text (Unique letters) : ").lower().replace(" ", "")
plain_text = input("Enter plain text (Letters only) : ").lower().replace(" ", "")

len_key = len(key)
len_plain = len(plain_text)
row = int(math.ceil(len_plain / len_key))
matrix = [ ['X']*len_key for i in range(row) ]

# =====Encryption=====
t = 0
for r in range(row):
    for c, ch in enumerate(plain_text[t: t + len_key]):
        matrix[r][c] = ch
    t += len_key
sort_order = sorted([(ch, i) for i, ch in enumerate(key)])
cipher_text = ''
for ch, c in sort_order:
    for r in range(row):
        cipher_text += matrix[r][c]

print("\nEncryption")
print("Plain text is :", plain_text)
print("Cipher text is:", cipher_text)

#=====Decryption=====
matrix_new = [ ['X']*len_key for i in range(row) ]
key_order = [ key.index(ch) for ch in sorted(list(key))]
t = 0
for c in key_order:
  for r,ch in enumerate(cipher_text[t : t+ row]):
    matrix_new[r][c] = ch
  t += row
p_text = ''
for r in range(row):
  for c in range(len_key):
    p_text += matrix_new[r][c] if matrix_new[r][c] != 'X' else ''

print("\nDecryption")
print("Cipher text is:",cipher_text)
print("Plain text is :",p_text)

2010030385 kamani Nandini, [02-05-2022 12:07]
transposition technique

2010030385 kamani Nandini, [02-05-2022 12:07]
from time import time


class TokenBucket(object):
    def init(self, tokens, fill_rate):
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = float(fill_rate)
        self.timestamp = time()

    def consume(self, tokens):
        if tokens <= self.tokens:
            self._tokens -= tokens
        else:
            return False
        return True

    def get_tokens(self):
        if self._tokens < self.capacity:
            now = time()
            delta = self.fill_rate * (now - self.timestamp)
            self._tokens = min(self.capacity, self._tokens + delta)
            self.timestamp = now
        return self._tokens

    tokens = property(get_tokens)


if name == 'main':
    from time import sleep

    bucket = TokenBucket(60, 1)
    print("tokens =", bucket.tokens)
    print("consume(10) =", bucket.consume(10))
    sleep(1)
    print("tokens =", bucket.tokens)
    sleep(1)
    print("tokens =", bucket.tokens)
    print("consume(40) =", bucket.consume(40))
    print("tokens =", bucket.tokens)

2010030385 kamani Nandini, [02-05-2022 12:07]
token bucket

2010030385 kamani Nandini, [02-05-2022 12:08]
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text = input("enter text:")
s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))

2010030385 kamani Nandini, [02-05-2022 12:08]
substitution

2010030385 kamani Nandini, [02-05-2022 12:08]
graph = {

'a':{'b':3,'c':4, 'd':7},
'b':{'c':1,'f':5},
'c':{'f':6,'d':2},
'd':{'e':3, 'g':6},
'e':{'g':3, 'h':4},
'f':{'e':1, 'h':8},
'g':{'h':2},
'h':{'g':2}
}


def dijkstra(graph,start,goal):

    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 5000
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0


    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()


        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:

                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]

                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)


    currentNode = goal

    while currentNode != start:

        try:
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    track_path.insert(0,start)


    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(track_path))


dijkstra(graph, 'a', 'h')

2010030385 kamani Nandini, [02-05-2022 12:08]
shortest path

2010030385 kamani Nandini, [02-05-2022 12:09]
def check(s):
    a=list(s)
    c=0
    for i in range(len(a)):
        if (s[i] == '1'):
            c = c + 1
    if(c%2==0):
        return 1
    return 0
s='101010'
x=check(s)
if(x==1):
    print("even parity")
else:
    print("odd parity")

2010030385 kamani Nandini, [02-05-2022 12:09]
parity cheacker

2010030385 kamani Nandini, [02-05-2022 12:09]
import java.io.*;
import java.util.*;
public class LeakyBucket {
  public static void main (String[] args) {
        int N,S,O;
        int I,B,L;
        S=0;
        N=4;
        B=10;
        I=4;
        O=1;

        for(int i=0;i<N;i++)
        {
           L=B-S;

            if(I<=(L))
            {
                S+=I;
                System.out.println("Buffer size= "+S+" \nout of bucket size= "+B);
            }
            else
            {
                System.out.println("Packet loss = "+(I-(L)));
                S=B;
                System.out.println("Buffer size= "+S+" \nout of bucket size= "+B);

            }
            S-=O;
        }
    }
}

2010030385 kamani Nandini, [02-05-2022 12:09]
leaky bucket

2010030385 kamani Nandini, [02-05-2022 12:10]
def calcRedundantBits(m):

  for i in range(m):
    if(2**i >= m + i + 1):
      return i

def posRedundantBits(data, r):

  j = 0
  k = 1
  m = len(data)
  res = ''

  for i in range(1, m + r+1):
    if(i == 2**j):
      res = res + '0'
      j += 1
    else:
      res = res + data[-1 * k]
      k += 1

  return res[::-1]

def calcParityBits(arr, r):
  n = len(arr)

  for i in range(r):
    val = 0
    for j in range(1, n + 1):

      if(j & (2**i) == (2**i)):
        val = val ^ int(arr[-1 * j])
    arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
  return arr

def detectError(arr, nr):
  n = len(arr)
  res = 0

  for i in range(nr):
    val = 0
    for j in range(1, n + 1):
      if(j & (2**i) == (2**i)):
        val = val ^ int(arr[-1 * j])
    res = res + val*(10**i)
  return int(str(res), 2)
data = '1011001'
m = len(data)
r = calcRedundantBits(m)
arr = posRedundantBits(data, r)
arr = calcParityBits(arr, r)
print("Data transferred is " + arr)

arr = '11101001110'
print("Error Data is " + arr)
correction = detectError(arr, r)
print("The position of error is " + str(correction))

2010030385 kamani Nandini, [02-05-2022 12:10]
hamming

2010030385 kamani Nandini, [02-05-2022 12:10]
def testing(reciever, div=5):
    message = str()
    length = len(reciever)
    col = reciever[length - div:]
    reciever = reciever[:length - div]
    row = []
    row_count = 0
    while (reciever):
        chunk = reciever[:div]
        old_parity = int(reciever[div])
        reciever = reciever[div + 1:]
        message += chunk

        sum_chunk = 0
        for i in range(div):
            sum_chunk += int(chunk[i])
        if old_parity != (sum_chunk % 2):
            row.append(row_count)
        row_count += 1

    print("Error in row_parity at", row)
    col_len = len(message) // div
    col_parity = []
    for j in range(div):
        sum_chunk = 0
        for i in range(col_len):
            sum_chunk += int(message[i * div + j])
        if int(col[j]) != (sum_chunk % 2):
            col_parity.append(j)

    print("Error in col_parity at", col_parity)
    print("message received", message)

    if len(row) == 0 and len(col_parity) == 0:
        print("\nNo error.")
    else:
        for i in range(len(row)):
            idx = row[i] * div + col_parity[-(i + 1)]
            print("error found at index", idx)

            if message[idx] == 0:
                message = message[:idx] + '1' + message[idx + 1:]
            else:
                message = message[:idx] + '0' + message[idx + 1:]
            print("\nMessage after correcting at index", idx, "=", message)
    print("\nFinal message ", message)


def addingParity(string, div=5):
    message = str()
    while (string):
        chunk = string[:div]
        string = string[div:]
        message += chunk

        sum_chunk = 0
        if len(chunk) == div:
            for i in range(div):
                sum_chunk += int(chunk[i])
            message += str(sum_chunk % 2)
        else:
            for i in range(div - len(chunk)):
                message += '0'
            for i in range(len(chunk)):
                sum_chunk += int(chunk[i])
            message += str(sum_chunk % 2)
    column_len = len(message) // (div + 1)
    for i in range(div):
        sum_column = 0
        for j in range(column_len):
            sum_column += int(message[i + (div + 1) * j])
        message += str(sum_column % 2)
    return message

if name=='main':

    input_message=input("\nEnter binary code for sending a message ")

    sender_message=addingParity(input_message)
    print("sender message ",sender_message)
    input_test=input("\nEnter binary code for testing of message ")
    print("\nTesting result")
    testing(input_test)

#sending = 01011100010100111010
#testing = 01011110001001001001011010101001

2010030385 kamani Nandini, [02-05-2022 12:11]
error detection 2d and multi dim parity

2010030385 kamani Nandini, [02-05-2022 12:11]
from queue import PriorityQueue
class Graph:
    def init(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
def dvr(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)
D = dvr(g, 0)

print(D)
for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

2010030385 kamani Nandini, [02-05-2022 12:11]
distance vector