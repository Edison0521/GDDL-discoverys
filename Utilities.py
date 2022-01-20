import copy

class Node(object):
    def __init__(self,node_id:int,node_attribute:list):
        self.id = node_id
        self.attribute = node_attribute

    def __repr__(self):
        return "%s %s"%(self.id,self.attribute)

class Edge(object):
    def __init__(self, node_id:int,edge_id:int) -> None:
        self.edge_id = edge_id
        self.node_id = node_id
    def __repr__(self):
        return "%s" % (self.edge_id)



class Pair(object):
    def __init__(self,node1_id:int,node2_id:int):

        self.node1_id = node1_id
        self.node2_id = node2_id
        #self.edge_id = edge_id
        self.pairlist = [self.node1_id,self.node2_id]
    def __repr__(self):
        #return "%s %s"%(self.node1_id,self.node2_id)
        return "%s"%(self.pairlist)




class LCP(object):
    def __init__(self,level_name:str,items:list):
        self.name = level_name
        self.items = items
    def __repr__(self):
        return "%s %s"%(self.name,self.items)
class LCPs(object):
    def __init__(self,level_name:str,items:list):
        self.name = level_name
        self.items = items
    def __repr__(self):
        return "%s %s"%(self.name,self.items)

class Item(object):
    def __init__(self,itemname:str,sigma:float,item:list):
        self.name = itemname
        self.item = item
        self.sigma = sigma

    def __repr__(self):
        return "%s %s %s" % (self.name, self.sigma,self.item)


class Graph(object):
    def __init__(self):
        self.node_list = []  # 初始化点集
        self.node_number = 0  # 顶点个数初始化
        #self.node_types = [] # 初始化类型
        self.node_attributes = [] # 初始化属性
        self.edges = [] # 初始化边
        self.edge_number = 0
        self.pairs = [] #初始化配对
        self.titles = []



    @property
    def nodes(self) -> list:
        '''
        返回图中所有节点
        '''
        return self.node_list


    @property
    def attribute(self) -> list:
        '''
        返回图中所有的type
        '''
        return self.node_attributes
    @property
    def title(self):

        return self.titles

    def addtitle(self,title:str):
        tiltes = title
        self.titles.append(tiltes)
        return title

    def addNode(self,node_id:int,node_attribute:list):
        self.node_number = node_id + 1
        node = Node(node_id,node_attribute)
        self.node_attributes.append(node_attribute)
        self.node_list.append(node)
        return node_id
    def find_node(self, id:int) -> Node:
        '''
        根据id查询节点
        '''
        return self.nodes[id - 1]
    def find_node_inlist(self, id:int) -> Node:
        '''
        根据id查询节点
        '''
        return self.nodes[id]
    def find_edge(self, edge_id:int) -> list:
        '''
        根据起始点id查询边

        edges = []
        if source_id != None or target_id != None:
            for edge in self.edges:
                if (source_id == None or source_id == edge.from_node.id) and (target_id == None or target_id == edge.to_node.id):
                    edges.append(edge)
                    '''
        return self.edges[edge_id - 1]


    def add_edge(self, node_id:int,edge_id:int) -> int:
        '''
        新增一条边

        参数
        ----
        自定，但至少有relation

        返回值
        ------
        id : int
            新增边的id

        if from_node_id > len(self.node_list):
            return -1
        if to_node_id > len(self.node_list):
            return -1

        edges = self.find_edge_by_endpoints(from_node_id, to_node_id)
        for edge in edges:
            if edge.relation == relation:
                return -1

        self.edge_number = self.edge_number + 1
        edge_id = self.edge_number

        from_node = self.find_node(from_node_id)
        to_node = self.find_node(to_node_id)
        edge = Edge(edge_id, from_node, to_node, relation)
        self.edges.append(edge)
        '''
        self.edge_number = edge_id
        edge = Edge(node_id,edge_id)
        self.edges.append(edge)
        return edge_id


    def add_pair(self):
        deleter = []
        for i in range(len(self.edges)):
            for j in range(len(self.edges)):
                if i != j:
                    if str(self.edges[i]) == str(self.edges[j]):
                        deleter.append(self.edges[i])
                        if self.edges[j] not in deleter:
                            #print(deleter)
                            pair = Pair(self.edges[i].node_id,self.edges[j].node_id)

                            if pair not in self.pairs:
                                self.pairs.append(pair)

class gddl(object):
    def __init__(self):
        self.itemlists = []
        self.gddls = []

    def additems(self,itemname:str,sigma:float,item:list):
        self.item = item
        self.sigma = sigma
        self.name = itemname
        gitem = Item(self.name,self.sigma,self.item)
        self.itemlists.append(gitem)

    def gddl(self,item:list):
        self.item = item
        self.gddls.append(self.item)
