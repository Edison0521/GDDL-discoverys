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
        return "%s %s"%(self.name,self.items )



class Item(object):
    def __init__(self,itemname:str,sigma:float,item:list):
        self.name = itemname
        self.item = item
        self.sigma = sigma

    def __repr__(self):
        return "%s %s %s" % (self.name, self.sigma,self.item)


class Graph(object):
    def __init__(self):
        self.node_list = []  # Initializing node sets
        self.node_number = 0  # Initializing nodenumber sets
        #self.node_types = [] # Initializing node_types
        self.node_attributes = [] # Initializing attributes
        self.edges = [] # Initializing edges
        self.edge_number = 0
        self.pairs = [] # Initializing pairs
        self.titles = []



    @property
    def nodes(self) -> list:
        '''
        return all nodes
        '''
        return self.node_list


    @property
    def attribute(self) -> list:
        '''
        return all types
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
        check node by id
        '''
        return self.nodes[id - 1]
    def find_node_inlist(self, id:int) -> Node:
        '''
        
        '''
        return self.nodes[id]
    def find_edge(self, edge_id:int) -> list:
        '''
        

        edges = []
        if source_id != None or target_id != None:
            for edge in self.edges:
                if (source_id == None or source_id == edge.from_node.id) and (target_id == None or target_id == edge.to_node.id):
                    edges.append(edge)
                    '''
        return self.edges[edge_id - 1]


    def add_edge(self, node_id:int,edge_id:int) -> int:
        '''

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