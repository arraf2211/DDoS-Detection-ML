import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

data = pd.read_csv("DrDos_DNS_New_With_all.csv")
#print(data) ##testing if the data has been loaded properly

##print(data.corr())

#print(data.head(10))

graph = nx.Graph()

testData = data.head(10)
# columnData = testData['Flow ID']
# print(columnData.head(1))

graph.add_node(testData['Flow ID'].values[0])
graph.add_node(testData[' Destination IP'].values[0])
graph.add_node(testData[' Source IP'].values[0])
graph.add_node('Packets') #unsure
graph.add_node('Size') ##if segment size greater than x
graph.add_node('Segment Size') ##if segment size greater than x
graph.add_node("FWD Packets") #connect using Total FWD length
graph.add_node(testData["Fwd PSH Flags"].values[0])
graph.add_node(testData["Fwd Header Length"].values[0])
graph.add_node(testData["Avg Fwd Segment Size"].values[0])
graph.add_node(testData["Fwd Packets/s"].values[0])
graph.add_node("BWD Packets")#connect using Total BWD length
graph.add_node(testData[" Bwd Header Length"].values[0])
graph.add_node(testData["Avg Bwd Segment Size"].values[0])
graph.add_node(testData[" Bwd Packets/s"].values[0])
graph.add_node(testData[" Flow Duration"].values[0]) #if flow duration greater than x
graph.add_node(testData["Down/Up Ratio"].values[0])
graph.add_node(testData["URG Flag Count"].values[0])
graph.add_node(testData["RST Flag Count"].values[0])
graph.add_node(testData["Active Mean"].values[0]) #if greater than 0
graph.add_node(testData["Idle Mean"].values[0])
graph.add_node(testData["Init_Win_bytes_backward"].values[0])
graph.add_node(testData["Init_Win_bytes_forward"].values[0])
graph.add_node(testData["Flow Packets/s"].values[0]) #Packet flow
graph.add_node(testData["Inbound"].values[0]) #if not 0
graph.add_node(testData["Bwd IAT Total"].values[0])
graph.add_node(testData["Fwd IAT Total"].values[0])



# for index, row in testData.iterrows():
pos = nx.spring_layout(graph)
nx.draw_networkx(graph,pos, with_labels=True, node_size=200, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')
plt.show()

