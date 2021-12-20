
class dnacon():
  def __init__(self) -> None:
      super(dnacon, self).__init__()
  
  def to_kmer(self,st,k=3):
      edges = []
      kmer=[]
      print("given sequence is",st)
      nodes = set()
      for i in range(len(st)-k+1):
          # print(st[i:i+k-1],end=":")
          # print(st[i+1:i+k])
          edges.append((st[i:i+k-1], st[i+1:i+k]))
          if st[i:i+k-1] not in kmer:
            kmer.append(st[i:i+k-1])
          if st[i+1:i+k] not in kmer:
            kmer.append(st[i+1:i+k])  
      return kmer, edges
  def kmer_to_graph(self,kmer,bool=True):
      m_dict={}
      for j in range(len(kmer)):
        if j==0:
          stored=kmer[j][:2]  
        i=kmer[j]
        if i[:2] in m_dict:
          m_dict[i[:2]].append(i[1:])
        else:
          m_dict[i[:2]]=[]
          m_dict[i[:2]].append(i[1:])  
      if bool:
          for k in kmer:
            stored=k[:2]
            i=kmer[len(kmer)-1][1:]
            m_dict[i].append(stored)
            break
      
      return m_dict
  def graphprint(self,graph):
       for k in graph.keys():
           print(k,end=":")
           for i in graph[k]:
               print(i,end=" ")
           print()            
  
  def balance(self,my_dict):
      indeg=[]
      outdeg=[]
      count=0
      c=0  
      for key in my_dict.keys():
        for values in my_dict[key]:
          c+=1
        outdeg.append(c)
        c=0
        count=count+1
      for key in my_dict.keys():  
        c=0
        for values in my_dict.values():
          for i in values:
            if i==key:
              c+=1 
        indeg.append(c)  
      return indeg ,outdeg
  
  def check(self,indeg,outdeg):
    _in=0
    _out=0
    start=0
    end=0
    count=0
    if len(indeg)!=len(outdeg):
      print("len of indeg and outdeg dont match")
      return None,None
    for (i,o) in zip(indeg,outdeg):
      j=i-o
      k=o-i
      if((o-i)>1 or (i-o)>1):
        print("error no path can be found")
        return -1,-1
      if((i-o)==1):
        _out=_out+1
        end=count
      elif((o-i)==1):
        start=count
        _in=_in+1
      count+=1  
    if((_in ==1 and _out ==1) or( _out==0 and _in==0)):
        return start,end    
        
  def dfs(self,g,start):
    stack=[]
    stack.append(start)
    path=[]
    while(1):
      adjlst=g[start]
      #has adjacent nodes#
      if len(adjlst)!=0: 
        i=adjlst[0]#get first edge 
        stack.append(i)
        g[start].remove(i)#reomove edge 
        start=i#take up new node as start node 
        z=0
      
      elif len(adjlst)==0:#no next nodes #end nodes
        path.append(start)
        stack.pop()
        if len(stack)!=0:
          start=stack[-1]
        else:
          return path
  
  def pathprint(self,str,bool):
    order=[]
    count=len(str)
    while(count!=0):
      count-=1
      if(count==0):
        if bool:
          print(str[count])
        order.append(str[count])
        return order
      if bool:
        print(str[count],end="->")
      order.append(str[count]) 
  
  def to_sequence(self,path):
    path.pop()
    s=""
    for i in range(len(path)):
      if i>len(path)-2:
        print(path[i],end=" ")
        s+=path[i]
        return s
      else: 
        print(path[i][:-1],end="")
        s+=path[i][:-1]

  def findeularianpath(self,graph):
    indeg,outdeg=self.balance(graph)
    start,end=self.check(indeg,outdeg)
    if start==None:
      print("no path avalable for graph")
      return []
    else:
      path=self.dfs(graph,kmer[0][:2])
      print("eulier path is given below")
      path=self.pathprint(path,True)#flip to false if u want no print statement
      return self.to_sequence(path)
      



d=dnacon()
sequence = "CTTGTATCACGT"
#returns sequence of kmers for a given sequence 
kmer,edge=d.to_kmer(sequence,k=4)#makes 3 mer 
#smaple kmer to test 

#uses adjacency representation to plot graph 
g=d.kmer_to_graph(kmer)
graph=d.kmer_to_graph(kmer)
# d.graphprint(g)
s=d.findeularianpath(g)

#d.graphprint(graph)

