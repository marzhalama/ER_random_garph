import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib

g1= nx.erdos_renyi_graph(10,0.5)
#nx.draw(g1, with_labels=True)
#plt.show()
# g2 =nx.erdos_renyi_graph(10,0.3)
# nx.draw(g2, with_labels=True)
# plt.show()
# g3 =nx.erdos_renyi_graph(10,0.1)
# nx.draw(g3, with_labels=True)
# plt.show()
# g4 =nx.erdos_renyi_graph(10,0.075)
# nx.draw(g4, with_labels=True)
# plt.show()
print(g1.edges)


# edge_list = []
# temp_list = []

# for key in list(g1):
#     s = list(g1[key])
#     for el in s:
#         temp_list.append((key, el))   
# edge_list.append(temp_list)
# print(edge_list)   

# lista_w = s
# print(lista_w)


def color_map_color(value, cmap_name='tab20', vmin=0, vmax=7):
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    cmap = cm.get_cmap(cmap_name) 
    rgb = cmap(norm(abs(value)))[:3] 
    color = matplotlib.colors.rgb2hex(rgb)
    return color
# function counting how many colors have been used to color vertices

def get_color(color_list):
    color_set = set(color_list)
    count_of_colors = 0 
    while True:
        if count_of_colors  not in color_set:
            return count_of_colors 
        count_of_colors += 1
# greedy coloring
def greedy_color (g1, order):
    color = {}
    for edge in order:
        used_neighbour_colors = [color[nbr] for nbr in g1[edge]
                                 if nbr in color]
        color[edge] = get_color(used_neighbour_colors)
    return color

first = greedy_color(g1, list(g1.nodes))
nx.draw_networkx(g1)
plt.show()
print(first)

colors_list = []
color_map = []
for node in g1:
    color_map.append(color_map_color(first[node]))
       
nx.draw(g1, node_color=color_map, with_labels=True)
plt.show()