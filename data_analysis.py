"""
读取数据，分析数据，并进行一些可视化操作
"""
# 读取数据，返回所有的paraphrases和非paraphrases
def get_paraphrases(file):
    """
    读取数据，其中file是 quora_duplicate_questions.tsv 的文件路径，
    比如："./dataset/quora_duplicate_questions.tsv"
    """
    paraphrase_pairs = []
    other_pairs = []

    with open(file, "r", errors="ignore") as f:
        next(f) # 跳过文件首行
        for line in f:
            line = line.strip().split("\t")
            try:
                if line[5] == "1":
                    paraphrase_pairs.append([line[5], line[3], line[4], line[0]])
                else:
                    other_pairs.append([line[5], line[3], line[4], line[0]])
            except IndexError: # 原始数据集中有部分数据出现了格式错误，跳过它们或者手动纠正它们
                print("The current pair has wrong format, please skip or correct them manually.")
                print(line)

    return paraphrase_pairs, other_pairs

# 正负样本比例可视化
def data_visualization(y):
    '''
    绘制正负样本比例的饼图,其中y是标签列表，
    比如：[1, 0, 1, 1, 0, 0, 0]
    '''
    from collections import Counter
    import matplotlib.pyplot as plt
    
    target_stats = Counter(y)
    # labels = list(target_stats.keys()) # 直接显示 0，1 而不是"paraphrase"和"others"
    labels = ["paraphrases", "others"] # 这里是自己指定的，可以按需修改
    sizes = list(target_stats.values())
    explode = tuple([0.1] * len(target_stats))
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, shadow=True, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Data ratio') # 图片的标题
    plt.savefig("./dataset/pos_neg_ratio.png") # 图片的保存路径
    plt.show()

# 句子长度统计
def get_sentence_length(pps, ops):
    '''统计一下句子的长度
    :param pps: list, paraphrase_pairs
    :param ops: list, other_pairs
    :return: dict
    '''
    from nltk.tokenize import TweetTokenizer
    import matplotlib.pyplot as plt

    all_pairs = pps + ops
    tt = TweetTokenizer()

    # 用来打印出question 2句长为0的样本(共两条，用"null"补全)
    for pair in ops:
        if len(tt.tokenize(pair[2])) == 0:
            print("The length of question2 of this pair is 0, please use 'null' to replace it.")
            print(pair)

    lenlist_q1 = [len(tt.tokenize(pair[1])) for pair in all_pairs] # 所有question 1的句长列表
    lenlist_pps_q1 = lenlist_q1[:len(pps)] # paraphrase pairs的question 1的句长列表
    lenlist_ops_q1 = lenlist_q1[len(pps):] # other pairs的question 1的句长列表
    maxlen_q1 = max(lenlist_q1) # 所有question 1的最大句子长度
    maxlen_pps_q1 = max(lenlist_pps_q1) # 所有paraphrase pairs中question 1的最大句子长度
    maxlen_ops_q1 = max(lenlist_ops_q1) # 所有other pairs中question 1的最大句子长度
    minlen_q1 = min(lenlist_q1) # 所有question 1的最小句子长度
    minlen_pps_q1 = min(lenlist_pps_q1) # 所有paraphrase pairs中question 1的最小句子长度
    minlen_ops_q1 = min(lenlist_ops_q1) # 所有other pairs中question 1的最小句子长度
    
    lenlist_q2 = [len(tt.tokenize(pair[2])) for pair in all_pairs] # 所有question 2的句长列表
    lenlist_pps_q2 = lenlist_q2[:len(pps)] # paraphrase pairs的question 2的句长列表
    lenlist_ops_q2 = lenlist_q2[len(pps):] # other pairs的question 2的句长列表
    maxlen_q2 = max(lenlist_q2) # 所有question 2的最大句子长度
    maxlen_pps_q2 = max(lenlist_pps_q2) # 所有paraphrase pairs中question 2的最大句子长度
    maxlen_ops_q2 = max(lenlist_ops_q2) # 所有other pairs中question 2的最大句子长度
    minlen_q2 = min(lenlist_q2) # 所有question 2的最小句子长度
    minlen_pps_q2 = min(lenlist_pps_q2) # 所有paraphrase pairs中question 2的最小句子长度
    minlen_ops_q2 = min(lenlist_ops_q2) # 所有other pairs中question 2的最小句子长度

    avg_q1 = sum(lenlist_q1)/len(lenlist_q1) # 所有question 1的平均句子长度
    avg_pps_q1 = sum(lenlist_pps_q1)/len(lenlist_pps_q1) # 所有paraphrase pairs中question 1的平均句子长度
    avg_ops_q1 = sum(lenlist_ops_q1)/len(lenlist_ops_q1) # 所有other pairs中question 1的平均句子长度

    avg_q2 = sum(lenlist_q2)/len(lenlist_q2) # 所有question 2的平均句子长度
    avg_pps_q2 = sum(lenlist_pps_q2)/len(lenlist_pps_q2) # 所有paraphrase pairs中question 2的平均句子长度
    avg_ops_q2 = sum(lenlist_ops_q2)/len(lenlist_ops_q2) # 所有other pairs中question 2的平均句子长度

    # 绘制句子长度直方图
    ## for question 1
    plt.hist(lenlist_q1, bins=40, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel('the length of question 1')
    plt.ylabel('value')
    plt.title('The sentence length distribution of question 1')
    plt.savefig("./dataset/len_q1.png")
    plt.show()
    

    # 清除原有图像
    plt.cla()

    ## for question 2
    plt.hist(lenlist_q2, bins=40, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel('the length of question 2')
    plt.ylabel('value')
    plt.title('The sentence length distribution of question 2')
    plt.savefig("./dataset/len_q2.png")
    plt.show()

    return {"maxlen_q1": maxlen_q1, "maxlen_pps_q1": maxlen_pps_q1, "maxlen_ops_q1": maxlen_ops_q1,
            "minlen_q1": minlen_q1, "minlen_pps_q1": minlen_pps_q1, "minlen_ops_q1": minlen_ops_q1,
            "maxlen_q2": maxlen_q2, "maxlen_pps_q2": maxlen_pps_q2, "maxlen_ops_q2": maxlen_ops_q2,
            "minlen_q2": minlen_q2, "minlen_pps_q2": minlen_pps_q2, "minlen_ops_q2": minlen_ops_q2,
            "avg_q1": avg_q1, "avg_pps_q1": avg_pps_q1, "avg_ops_q1": avg_ops_q1,
            "avg_q2": avg_q2, "avg_pps_q2": avg_pps_q2, "avg_ops_q2": avg_ops_q2}

if __name__ == "__main__":
    data_path = "./dataset/quora_duplicate_questions.tsv"
    # data_path = "G:/datasets/paraphrase datasets/Quora/quora_duplicate_questions.tsv"
    paraphrase_pairs, other_pairs = get_paraphrases(data_path)

    # 正负样本比例统计
    print("="*20)
    print("Total paraphrase pairs number is: %d" % len(paraphrase_pairs)) # 共 149263 对paraphrases
    print("Other pairs number is: %d" % len(other_pairs)) # 共 255027 对非paraphrases
    print("Total number is: %d" % (len(paraphrase_pairs) + len(other_pairs))) # 共 404290 对数据
    print("="*20)

    # 正负样本比例可视化
    y = [1] * len(paraphrase_pairs) + [0] * len(other_pairs)
    data_visualization(y)

    # 句子长度统计
    len_dict =  get_sentence_length(paraphrase_pairs, other_pairs)
    for k, v in len_dict.items():
        print(k, v)
    # print(len_dict)

    # 把所有的paraphrases保存成文件，方便读取
    print("="*20)
    print("save all the paraphrases...")
    with open("./dataset/paraphrases.tsv", "w") as f:
        # f.write("question1" + "\t" + "question2" + "\n")
        for pair in paraphrase_pairs:
            f.write(pair[0])
            f.write("\t")
            f.write(pair[1])
            f.write("\t")
            f.write(pair[2])
            f.write("\t")
            f.write(pair[3])
            f.write("\n")
    print("Done!")

    # 把所有的非paraphrases保存成文件，方便读取
    print("="*20)
    print("save all the none paraphrases...")
    with open("./dataset/none_paraphrases.tsv", "w") as f:
        # f.write("question1" + "\t" + "question2" + "\n")
        for pair in other_pairs:
            f.write(pair[0])
            f.write("\t")
            f.write(pair[1])
            f.write("\t")
            f.write(pair[2])
            f.write("\t")
            f.write(pair[3])
            f.write("\n")
    print("Done!")