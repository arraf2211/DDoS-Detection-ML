import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import grakel as gk
from grakel import Graph
from grakel.utils import graph_from_networkx , cross_validate_Kfold_SVM
from grakel.kernels import WeisfeilerLehman, VertexHistogram, ShortestPath, ShortestPathAttr
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = pd.read_csv("DrDos_DNS_New_With_all.csv")
#print(data) ##testing if the data has been loaded properly

##print(data.corr())

#print(data.head(10))

graph_list = []

testData = data.head(60)
# columnData = 
# print(columnData.head(1))
#TODO Using for loops, iterate through each value making a graph and storing it somewhere
#TODO Have some edges be dependent on some factors e.g if this value is equal to 0 then dont include it

for i in range(len(testData)):
    #Grakel Graph Formatting
    edges = {"Flow ID":["Source IP","Destination IP","Protocol","Flow Duration","Down/Up Ratio",
                         "URG Flag Count","RST Flag Count","Idle Mean","Active Mean","Initial Window Bytes Backward",
                         "Initial Window Bytes Forward","Flow Packets per Sec","Inbound"],
            "Flow Packets per Sec":["Flow ID","Backward IAT Total","Forward IAT Total",
                                    "Minimum Segment Size Forward","Average Packet Size"],
            "Source IP":["Flow ID","Total Forward Packets"],
            "Destination IP":["Flow ID","Total Backward Packets"],
            "Minimum Segment Size Forward":["Flow ID"],
            "Average Packet Size":["Flow ID"],
            "Total Forward Packets":["Source IP","Forward PSH Flags","Forward Header Length","Average Forward Segment Size","Forward Packets per Sec",
                                     "Total Length Forward Packets"],
            "Total Backward Packets":[ "Destination IP","Total Length Backward Packets","Backward Header Length",
                                      "Average Backward Segment Size","Backward Packets per Sec"],
            "Total Length Forward Packets":["Total Forward Packets"],
            "Total Length Backward Packets":["Total Backward Packets"],
            "Forward Header Length":["Total Forward Packets"],
            "Average Forward Segment Size":["Total Forward Packets"],
            "Forward Packets per Sec":["Total Forward Packets"],
            "Backward Header Length":["Total Backward Packets"],
            "Average Backward Segment Size":["Total Backward Packets"],
            "Backward Packets per Sec":["Total Backward Packets"],
            "Flow Duration":["Flow ID"],
            "Down/Up Ratio":["Flow ID"],
            "Active Mean":["Flow ID"],
            "Idle Mean":["Flow ID"],
            "Protocol":["Flow ID"],
            "Initial Window Bytes Backward":["Flow ID"],
            "Initial Window Bytes Forward":["Flow ID"],
            "Backward IAT Total":["Flow Packets per Sec"],
            "Forward IAT Total":["Flow Packets per Sec"],
            "Forward PSH Flags":["Total Forward Packets"],
            "URG Flag Count":["Flow ID"],
            "RST Flag Count":["Flow ID"],
            "Inbound":["Flow ID"]}

    node_attributes = {
        "Flow ID":testData["Flow ID"].values[i],
        "Destination IP":testData[' Destination IP'].values[i],
        "Source IP":testData[' Source IP'].values[i],
        "Minimum Segment Size Forward":testData[' min_seg_size_forward'].values[i],
        "Average Packet Size":testData[' Average Packet Size'].values[i],
        "Total Forward Packets":testData[" Total Fwd Packets"].values[i],
        "Total Backward Packets":testData[" Total Backward Packets"].values[i],
        "Total Length Forward Packets":testData["Total Length of Fwd Packets"].values[i],
        "Total Length Backward Packets":testData[" Total Length of Bwd Packets"].values[i],
        "Forward Header Length":testData["Fwd Header Length"].values[i],
        "Average Forward Segment Size":testData["Avg Fwd Segment Size"].values[i],
        "Forward Packets per Sec":testData["Fwd Packets/s"].values[i],
        "Backward Header Length":testData[" Bwd Header Length"].values[i],
        "Average Backward Segment Size":testData["Avg Bwd Segment Size"].values[i],
        "Backward Packets per Sec":testData[" Bwd Packets/s"].values[i],
        "Flow Duration":testData[" Flow Duration"].values[i],
        "Down/Up Ratio":testData["Down/Up Ratio"].values[i],
        "Active Mean":testData["Active Mean"].values[i],
        "Idle Mean":testData["Idle Mean"].values[i],
        "Initial Window Bytes Backward":testData["Init_Win_bytes_backward"].values[i],
        "Initial Window Bytes Forward":testData["Init_Win_bytes_forward"].values[i],
        "Flow Packets per Sec":testData["Flow Packets/s"].values[i],
        "Backward IAT Total":testData["Bwd IAT Total"].values[i],
        "Forward IAT Total":testData["Fwd IAT Total"].values[i],
        "Protocol":testData[" Protocol"].values[i],
        "Forward PSH Flags":testData["Fwd PSH Flags"].values[i],
        "URG Flag Count":testData["URG Flag Count"].values[i],
        "RST Flag Count":testData["RST Flag Count"].values[i],
        "Inbound":testData["Inbound"].values[i]
    }
    
    g = Graph(edges, node_labels = node_attributes)
    graph_list.append(g)





    # graph = nx.Graph()
    # #graph.add_node(testing)
    # graph.add_node("Flow ID", Flow_ID = testData["Flow ID"].values[i])
    # graph.add_node("Destination IP", Destination_IP = testData[' Destination IP'].values[i])
    # graph.add_node("Source IP", Source_IP=testData[' Source IP'].values[i])
    # graph.add_node("Minimum Segment Size Forward", Min_Seg_Size_Forward=testData[' min_seg_size_forward'].values[i])
    # graph.add_node("Average Packet Size", Average_Packet_Size=testData[' Average Packet Size'].values[i])
    # graph.add_node("Total Forward Packets", Total_Fwd_Packets=testData[" Total Fwd Packets"].values[i])
    # graph.add_node("Total Backward Packets", Total_Backward_Packets=testData[" Total Backward Packets"].values[i])
    # graph.add_node("Total Length Forward Packets", Total_Length_Fwd_Packets=testData["Total Length of Fwd Packets"].values[i])
    # graph.add_node("Total Length Backward Packets", Total_Length_Bwd_Packets=testData[" Total Length of Bwd Packets"].values[i])
    # graph.add_node("Fwd Header Length", Fwd_Header_Length=testData["Fwd Header Length"].values[i])
    # graph.add_node("Average Forward Segment Size", Avg_Fwd_Segment_Size=testData["Avg Fwd Segment Size"].values[i])
    # graph.add_node("Forward Packets per Sec", Fwd_Packets_Per_S=testData["Fwd Packets/s"].values[i])
    # graph.add_node("Backward Header Length", Bwd_Header_Length=testData[" Bwd Header Length"].values[i])
    # graph.add_node("Average Backward Segment Size", Avg_Bwd_Segment_Size=testData["Avg Bwd Segment Size"].values[i])
    # graph.add_node("Backward Packets per Sec", Bwd_Packets_Per_S=testData[" Bwd Packets/s"].values[i])
    # graph.add_node("Flow Duration", Flow_Duration=testData[" Flow Duration"].values[i])
    # graph.add_node("Down/Up Ratio", Down_Up_Ratio=testData["Down/Up Ratio"].values[i])
    # graph.add_node("Active Mean", Active_Mean=testData["Active Mean"].values[i])
    # graph.add_node("Idle Mean", Idle_Mean=testData["Idle Mean"].values[i])
    # graph.add_node("Initial Window Bytes Backward", Init_Win_Bytes_Backward=testData["Init_Win_bytes_backward"].values[i])
    # graph.add_node("Initial Window Bytes Forward", Init_Win_Bytes_Forward=testData["Init_Win_bytes_forward"].values[i])
    # graph.add_node("Flow Packets per Sec", Flow_Packets_Per_S=testData["Flow Packets/s"].values[i])
    # graph.add_node("Backward IAT Total", Bwd_IAT_Total=testData["Bwd IAT Total"].values[i])
    # graph.add_node("Forward IAT Total", Fwd_IAT_Total=testData["Fwd IAT Total"].values[i])
    # graph.add_node("Protocol", Protocol=testData[" Protocol"].values[i])
    # graph.add_node("Forward PSH Flags",FWD_PSH = testData["Fwd PSH Flags"].values[i])
    # graph.add_node("URG Flag Count" , Urg_Flag = testData["URG Flag Count"].values[i])
    # graph.add_node("RST Flag Count", RST_Flag = testData["RST Flag Count"].values[i])
    # graph.add_node("Inbound", Inbound = testData["Inbound"].values[i]) 

    # # if(testData["Fwd PSH Flags"].values[i] != 0):
    # #     graph.add_node(testData["Fwd PSH Flags"].values[i]) #if 1 or 0
    # # if(testData["URG Flag Count"].values[i] != 0):
    # #     graph.add_node(testData["URG Flag Count"].values[i]) #if 0 or 1
    # # if(testData["RST Flag Count"].values[i] != 0):
    # #     graph.add_node(testData["RST Flag Count"].values[i]) #if 0 or 1
    # # if(testData["Inbound"].values[i] != 0):
    # #     graph.add_node(testData["Inbound"].values[i]) #if not 0

    # #graph.add_edge(testing, testing1)
    # graph.add_edge("Flow ID", "Source IP")
    # graph.add_edge("Flow ID", "Destination IP")
    # graph.add_edge("Flow ID", "Protocol")
    # graph.add_edge("Flow ID", "Flow Duration")
    # graph.add_edge("Flow ID", "Down/Up Ratio")
    # graph.add_edge("Flow ID", "URG Flag Count")
    # graph.add_edge("Flow ID", "RST Flag Count")
    # graph.add_edge("Flow ID", "Idle Mean")
    # graph.add_edge("Flow ID", "Active Mean")
    # graph.add_edge("Flow ID", "Initial Window Bytes Backward")
    # graph.add_edge("Flow ID", "Initial Window Bytes Forward")
    # graph.add_edge("Flow ID", "Flow Packets per Sec")
    # graph.add_edge("Flow ID", "Inbound")
    # graph.add_edge("Flow Packets per Sec", "Backward IAT Total")
    # graph.add_edge("Flow Packets per Sec", "Forward IAT Total")
    # graph.add_edge("Flow Packets per Sec", "Minimum Segment Size Forward")
    # graph.add_edge("Flow Packets per Sec", "Average Packet Size")
    # graph.add_edge("Source IP","Total Forward Packets")
    # graph.add_edge("Destination IP","Total Backward Packets")
    # graph.add_edge("Total Forward Packets","Forward PSH Flags")
    # graph.add_edge("Total Forward Packets","Forward Header Length")
    # graph.add_edge("Total Forward Packets","Average Forward Segment Size")
    # graph.add_edge("Total Forward Packets","Forward Packets per Sec")
    # graph.add_edge("Total Forward Packets","Total Length Forward Packets")
    # graph.add_edge("Total Backward Packets","Total Length Backward Packets")
    # graph.add_edge("Total Backward Packets","Backward Header Length")
    # graph.add_edge("Total Backward Packets","Average Backward Segment Size")
    # graph.add_edge("Total Backward Packets","Backward Packets per Sec")

    # graph_list.append(graph)

# pos = nx.spring_layout(graph_list[50])
# nx.draw_networkx(graph_list[50],pos, with_labels=True, node_size=100, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
# plt.show()
    
# print(nx.weisfeiler_lehman_graph_hash(graph))
# print(nx.weisfeiler_lehman_graph_hash(graph2))
    
edges = {"Flow ID":["Source IP","Destination IP","Protocol","Flow Duration","Down/Up Ratio",
                         "URG Flag Count","RST Flag Count","Idle Mean","Active Mean","Initial Window Bytes Backward",
                         "Initial Window Bytes Forward","Flow Packets per Sec","Inbound"],
            "Flow Packets per Sec":["Flow ID","Backward IAT Total","Forward IAT Total",
                                    "Minimum Segment Size Forward","Average Packet Size"],
            "Source IP":["Flow ID","Total Forward Packets"],
            "Destination IP":["Flow ID","Total Backward Packets"],
            "Minimum Segment Size Forward":["Flow ID"],
            "Average Packet Size":["Flow ID"],
            "Total Forward Packets":["Source IP","Forward PSH Flags","Forward Header Length","Average Forward Segment Size","Forward Packets per Sec",
                                     "Total Length Forward Packets"],
            "Total Backward Packets":[ "Destination IP","Total Length Backward Packets","Backward Header Length",
                                      "Average Backward Segment Size","Backward Packets per Sec"],
            "Total Length Forward Packets":["Total Forward Packets"],
            "Total Length Backward Packets":["Total Backward Packets"],
            "Forward Header Length":["Total Forward Packets"],
            "Average Forward Segment Size":["Total Forward Packets"],
            "Forward Packets per Sec":["Total Forward Packets"],
            "Backward Header Length":["Total Backward Packets"],
            "Average Backward Segment Size":["Total Backward Packets"],
            "Backward Packets per Sec":["Total Backward Packets"],
            "Flow Duration":["Flow ID"],
            "Down/Up Ratio":["Flow ID"],
            "Active Mean":["Flow ID"],
            "Idle Mean":["Flow ID"],
            "Protocol":["Flow ID"],
            "Initial Window Bytes Backward":["Flow ID"],
            "Initial Window Bytes Forward":["Flow ID"],
            "Backward IAT Total":["Flow Packets per Sec"],
            "Forward IAT Total":["Flow Packets per Sec"],
            "Forward PSH Flags":["Total Forward Packets"],
            "URG Flag Count":["Flow ID"],
            "RST Flag Count":["Flow ID"],
            "Inbound":["Flow ID"]}

i = 0
#get rid of [] around data
node_attributes = {
    "Flow ID":0,
    "Destination IP":0,
    "Source IP":0,
    "Minimum Segment Size Forward":testData[' min_seg_size_forward'].values[i],
    "Average Packet Size":testData[' Average Packet Size'].values[i],
    "Total Forward Packets":testData[" Total Fwd Packets"].values[i],
    "Total Backward Packets":testData[" Total Backward Packets"].values[i],
    "Total Length Forward Packets":testData["Total Length of Fwd Packets"].values[i],
    "Total Length Backward Packets":testData[" Total Length of Bwd Packets"].values[i],
    "Forward Header Length":testData["Fwd Header Length"].values[i],
    "Average Forward Segment Size":testData["Avg Fwd Segment Size"].values[i],
    "Forward Packets per Sec":testData["Fwd Packets/s"].values[i],
    "Backward Header Length":testData[" Bwd Header Length"].values[i],
    "Average Backward Segment Size":testData["Avg Bwd Segment Size"].values[i],
    "Backward Packets per Sec":testData[" Bwd Packets/s"].values[i],
    "Flow Duration":testData[" Flow Duration"].values[i],
    "Down/Up Ratio":testData["Down/Up Ratio"].values[i],
    "Active Mean":testData["Active Mean"].values[i],
    "Idle Mean":testData["Idle Mean"].values[i],
    "Initial Window Bytes Backward":testData["Init_Win_bytes_backward"].values[i],
    "Initial Window Bytes Forward":testData["Init_Win_bytes_forward"].values[i],
    "Flow Packets per Sec":testData["Flow Packets/s"].values[i],
    "Backward IAT Total":testData["Bwd IAT Total"].values[i],
    "Forward IAT Total":testData["Fwd IAT Total"].values[i],
    "Protocol":testData[" Protocol"].values[i],
    "Forward PSH Flags":testData["Fwd PSH Flags"].values[i],
    "URG Flag Count":testData["URG Flag Count"].values[i],
    "RST Flag Count":testData["RST Flag Count"].values[i],
    "Inbound":testData["Inbound"].values[i]
}

#maybe convert the labels into numbers?

G = Graph(edges, node_labels = node_attributes)

# print(testData["URG Flag Count"].values[i])
# H2O_adjacency = [[2, 0, 0], [2, 2, 1], [1, 0, 0]]
# H2O_node_labels = {0: testData["Inbound"].values[i], 1: testData["RST Flag Count"].values[i], 2: testData["URG Flag Count"].values[i]}
# H2O = Graph(initialization_object=H2O_adjacency, node_labels=H2O_node_labels)

sp_kernel = ShortestPath()
spA_Kernel = ShortestPathAttr() #gives different values based on graph attributes [[5.39816065e+19]] [[1.90274166e+19]]
gk = WeisfeilerLehman(n_iter=3,base_graph_kernel=VertexHistogram, normalize=True)



gk_graph = graph_list[0]

print(mLaplacian.fit_transform([G]))


# print(gk_graph.get_edge_dictionary())

#TODO: Build the graph Kernel to return feature Vectors to be used on SVM

# Ks =list()
# for i in range(1,7): #cross validation
#     gk = WeisfeilerLehman(n_iter=i,base_graph_kernel=VertexHistogram, normalize=True)
#     K = gk.fit_transform(gk_graph)
#     Ks.append(K)



