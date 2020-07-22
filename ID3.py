# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a ID3 script file.
"""

from math import log
import operator
import tree_plotter

def create_data_set():
    '''
    创建样本数据
    :return:
    '''
    data_set = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing','flippers']
    return data_set, labels
    
def calc_shannon_ent(data_set):
     '''
     计算信息熵
     :param data_set: 如上
     :return:
     '''
     # 返回数据集行数
     num = len(data_set) #n rows
     # 保存每个标签（label）出现次数的字典
     label_counts={}
     # 对每组特征向量进行统计
     for feat_vec in data_set:
         current_label=feat_vec[-1] #取得最后一列数据（标签信息）
         if current_label not in label_counts.keys(): # 如果标签没有放入统计次数的
             label_counts[current_label]=0
             label_counts[current_label]+=1 #label计数
             
     # 计算熵
     shannon_ent=0.0
     for key in label_counts:
         prob=float(label_counts[key])/num  #选择该标签的概率
         shannon_ent=shannon_ent-prob*log(prob,2) # 利用公式计算
     return shannon_ent #返回经验熵
 
def split_data_set(data_set,axis,value):
    '''
    返回特征值等于value的子数据集，且该数据集不包含列（特征）axis
    :param data_set: 待划分的数据集
    :param axis:特征索引（划分数据集的特征）
    :param value：分类值（需要返回的特征值）
    :return:
    '''
    # 创建返回的数据集列表
    ret_data_set=[]
    # 遍历数据集
    for feat_vec in data_set:
        if feat_vec[axis]==value:
            # 去掉axis特征
            reduce_feat_vec=feat_vec[:axis]
            # 将符合条件的添加到返回的数据集
            reduce_feat_vec.extend(feat_vec[axis+1:])
            ret_data_set.append(reduce_feat_vec)
    # 返回划分后俄数据集
    return ret_data_set

def choose_best_feature_to_split(data_set):
    '''
    按照最大信息增益划分数据
    :param data_set:样本数据
    :param shannon_ent:信息增益最大特征的索引值
    :return:
    '''
    
    num_feature=len(data_set[0])-1 #特征个数
    base_entropy=calc_shannon_ent(data_set) #经验熵
    #信息增益
    best_info_gain=0
    #最优特征的索引值
    best_feature_idx=-1
    #遍历所有特征
    for feature_idx in range(num_feature):
        # 获取data_set的第i个所有特征
        feature_val_list=[number[feature_idx] for number in data_set] #得到某个特征下所有值
        #创建set集合{}，元素不可重复
        unique_feature_val_list=set(feature_val_list) #获取无重复的属性特征值
        #经验条件熵
        new_entropy=0
        #计算信息增益
        for feature_val in unique_feature_val_list:
            #sub_data_set划分后的子集
            sub_data_set=split_data_set(data_set,feature_idx,feature_val)
            # 计算子集的概率
            prob=len(sub_data_set)/float(len(data_set)) #即p(t)
            #根据公式计算经验条件熵
            new_entropy+=prob*calc_shannon_ent(sub_data_set) #对各子集的熵求集合
            #信息增益
            info_gain=base_entropy-new_entropy #计算信息增益
            #输出每个特征的信息增益
            print('第%d个特征的增益为%.3f' % (feature_idx,info_gain))
            #计算最大信息增益
            if info_gain > best_info_gain:
                # 更新信息增益，找到最大的信息增益
                best_info_gain=info_gain
                # 记录信息增益最大的特征的索引值
                best_feature_idx=feature_idx
                
        return best_feature_idx
    
    
def majority_cnt(class_list):
    '''
    统计每个类别出现的次数，并按大到小排序，返回出现次数最大的类别标签
    :param class_list:类标签列表
    :return sorted_class_count[0][0]：出现次数最多的元素（类标签）
    '''
    class_count={}
    # 统计class_list中每个元素出现的次数
    for vote in class_list:
        if vote not in class_count.keys():
            class_count[vote]=0
            class_count[vote]+=1
        #根据字典的值降序排列
        sorted_class_count=sorted(class_count.items(),key=operator.itemgetter(1),reversed=True)
   
    return sorted_class_count[0][0]

def create_tree(data_set,labels):
    """
    构建决策树
    :param data_set: 数据集合，如： [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    :param labels: 标签数组，如：['no surfacing', 'flippers']
    :param feat_labels:存储选择的最优特征标签
    :return:
    """
    #取分类标签
    class_list=[sample[-1] for sample in data_set] # ['yes', 'yes', 'no', 'no', 'no']
    # 类别相同，停止划分
    if class_list.count(class_list[-1]) == len(class_list):
        return class_list[-1]
    # 长度为1，遍历所有特征时，返回出现次数最多的类别
    if len(class_list[0]) == 1:
        return majority_cnt((class_list))
    # 按照信息增益最高选取分类特征属性
    best_feature_idx = choose_best_feature_to_split(data_set)  # 返回分类的特征的数组索引
    best_feat_label = labels[best_feature_idx]  # 该特征的label
    my_tree = {best_feat_label: {}}  # 构建树的字典
    
    # 从labels的list中删除该label，相当于待划分的子标签集
    del (labels[best_feature_idx]) 
    #得到训练集中所有最优特征的属性值
    feature_values = [example[best_feature_idx] for example in data_set]
    #去掉重复的属性值
    unique_feature_values = set(feature_values)
    #遍历特征，创建决策树
    for feature_value in unique_feature_values:
        sub_labels = labels[:]  # 子集合
        # 构建数据的子集合，并进行递归
        sub_data_set = split_data_set(data_set, best_feature_idx, feature_value) # 待划分的子数据集
        my_tree[best_feat_label][feature_value] = create_tree(sub_data_set, sub_labels)
    return my_tree


def classify(input_tree, feat_labels, test_vec):
    """
    决策树分类
    :param input_tree: 已经生成的决策树
    :param feat_labels: 存储选择的最优特征标签
    :param test_vec: 测试的数据，顺序对应最优特征标签
    :return: 分类结果
    """
    first_str = list(input_tree.keys())[0]  # 获取树的第一特征属性
    second_dict = input_tree[first_str]  # 树的分子，子集合Dict（下一个字典）
    feat_index = feat_labels.index(first_str)  # 获取决策树第一层在feat_labels中的位置
    for key in second_dict.keys():
        if test_vec[feat_index] == key:
            if type(second_dict[key]).__name__ == 'dict':
                class_label = classify(second_dict[key], feat_labels, test_vec)
            else:
                class_label = second_dict[key]
            return class_label
        
data_set, labels = create_data_set()
decision_tree = create_tree(data_set, labels)
print ("决策树：", decision_tree)
data_set,labels = create_data_set()
print ("（1）不浮出水面可以生存，无脚蹼：", classify(decision_tree, labels, [1, 0]))
print ("（2）不浮出水面可以生存，有脚蹼：", classify(decision_tree, labels, [1, 1]))
print ("（3）不浮出水面可以不能生存，无脚蹼：", classify(decision_tree, labels, [0, 0]))
tree_plotter.create_plot(decision_tree)
    
    

    
    
    
    
    
    
    
    
    
    
    
    