""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""


class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=[]):
        """ find a path from start_vertex to end_vertex
            in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted
            double, i.e. every occurence of vertex in the list
            of adjacent vertices. """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min

    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def erdoes_gallai(dsequence):
        """ Checks if the condition of the Erdoes-Gallai inequality
            is fullfilled
            dsequence has to be a valid degree sequence
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        for k in range(1, len(dsequence) + 1):
            left = sum(dsequence[:k])
            right = k * (k - 1) + sum([min(x, k) for x in dsequence[k:]])
            if left > right:
                return False
        return True

    def density(self):
        """ method to calculate the density of a graph """
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V * (V - 1))

    def is_connected(self,vertices_encountered=None, start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict
        vertices = list(gdict.keys())  # "list" necessary in Python 3
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def diameter(self):
        """ calculates the diameter of the graph """

        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1])
        return diameter


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    complete_graph = {
        "a": ["b", "c"],
        "b": ["a", "c"],
        "c": ["a", "b"]
    }

    isolated_graph = {
        "a": [],
        "b": [],
        "c": []
    }

    g1 = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    g2 = {"a": ["d", "f"],
          "b": ["c"],
          "c": ["b", "c", "d", "e"],
          "d": ["a", "c"],
          "e": ["c"],
          "f": ["a"]
          }

    g3 = {"a": ["d", "f"],
          "b": ["c", "b"],
          "c": ["b", "c", "d", "e"],
          "d": ["a", "c"],
          "e": ["c"],
          "f": ["a"]
         }

    g4 = {"a": ["c"],
         "b": ["c", "e", "f"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["b", "c", "f"],
         "f": ["b", "e"]
         }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    print("Find a path:")
    print(graph.find_path("a", "e"))
    print("Find all paths:")
    print(graph.find_path("a", "e"))
    print("Vertex degree :")
    print(graph.vertex_degree("d"))
    print("Isolated vertexes:")
    print(graph.find_isolated_vertices())
    print("Minimum degree of vertexes:")
    print(graph.delta())
    print("Maximum degree of vertexes:")
    print(graph.Delta())
    print("Degree sequence:")
    print(graph.degree_sequence())
    print("Erdős-Gallai theorem:")
    mylist = (5,2,1,1,1,0)
    print(graph.erdoes_gallai(graph.degree_sequence()))

    print("Density of g:")
    print(graph.density())

    print("Density of complete_graph:")
    graph = Graph(complete_graph)
    print(graph.density())

    print("Density of isolated_graph:")
    graph = Graph(isolated_graph)
    print(graph.density())

    print("Connected graph1:")
    graph = Graph(g1)
    print(graph.is_connected())

    print("Connected graph2:")
    graph = Graph(g2)
    print(graph.is_connected())

    print("Connected graph3:")
    graph = Graph(g3)
    print(graph.is_connected())

    print("Diameter for g:")
    graph = Graph(g4)
    print(graph.diameter())

