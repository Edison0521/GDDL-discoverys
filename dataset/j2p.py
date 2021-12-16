import pandas as pd
import json
import numpy as np
import csv
import os
'''
path=("1011Edges.csv")

# 这里是原始的分隔符
reader = list(csv.reader(open(path, "rU",encoding='utf-8'), delimiter=';'))
with open(path, 'w',encoding='utf-8') as csvfile:
	# 这里是修改后的分隔符
    writer = csv.writer(csvfile, delimiter=';;')
    writer.writerows(row for row in reader)
'''
# 使用 Python JSON 模块载入数据
with open('IMDBless.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())

# 展平边数据
df_Edges_list = pd.json_normalize(data,  record_path=['Edges'])
# 展平节点数据
df_Vertices_list = pd.json_normalize(data,
                                     record_path = ['Vertices'],
                                     )
#print(type(df_Vertices_list))
#保存信息
#np.savetxt('333.csv',df_Vertices_list,delimiter=";;")
s = str(',')
df_Edges_list.to_csv('lessEdges.csv',encoding='utf-8',sep= s)
#保存节点信息
df_Vertices_list.to_csv('lessNodes.csv',encoding='utf-8',sep = s)
