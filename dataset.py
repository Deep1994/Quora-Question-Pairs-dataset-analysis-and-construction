"""
从所有的 praraphrases 中随机抽取5000条, 从所有的 非paraphrases 中随机抽取5000条, 以上共10000条作为验证集;
从剩下的所有的 praraphrases 中随机抽取5000条, 从剩下的所有的 非paraphrases 中随机抽取5000条, 以上共10000条作为测试集;
剩余所有的作为训练集。
"""

def get_dataset(data_paraphrases, data_none_paraphrases):
    from data_preprocess import clean_text
    import random

    all_paraphrases = []
    all_none_paraphrases = []

    # 读取 paraphrases
    with open(data_paraphrases, "r") as f:
        for line in f:
            line = line.strip().split("\t")
            all_paraphrases.append(line)
    
    assert(len(all_paraphrases) == 149263)

    # 读取 none paraphrases
    with open(data_none_paraphrases, "r") as f:
        for line in f:
            line = line.strip().split("\t")
            all_none_paraphrases.append(line)

    assert(len(all_none_paraphrases) == 255027)

    # print(len(all_paraphrases))
    # print(all_paraphrases[:10])
    # print(len(all_none_paraphrases))
    # print(all_none_paraphrases[:10])


    # 生成随机索引，构建训练/验证/测试集
    ## random 5000 paraphrases for dev
    dev_paraphrases_index = sorted(random.sample(list(range(len(all_paraphrases))), 5000))
    assert(len(dev_paraphrases_index) == 5000)

    rest_index = list(set(list(range(len(all_paraphrases)))) - set(dev_paraphrases_index))
    assert(len(rest_index) == len(all_paraphrases) - 5000)

    ## random 5000 paraphrases for test
    test_paraphrases_index = sorted(random.sample(rest_index, 5000))
    assert(len(test_paraphrases_index) == 5000)

    ## rest paraphrases for train
    train_paraphrases_index = list(set(rest_index) - set(test_paraphrases_index))
    assert(len(train_paraphrases_index) == len(all_paraphrases) - 10000)

    ## random 5000 none paraphrases for dev
    dev_none_paraphrases_index = sorted(random.sample(list(range(len(all_none_paraphrases))), 5000))
    assert(len(dev_none_paraphrases_index) == 5000)

    rest_index = list(set(list(range(len(all_none_paraphrases)))) - set(dev_none_paraphrases_index))
    assert(len(rest_index) == len(all_none_paraphrases) - 5000)

    ## random 5000 none paraphrases for test
    test_none_paraphrases_index = sorted(random.sample(rest_index, 5000))
    assert(len(test_none_paraphrases_index) == 5000)

    ## rest none paraphrases for train
    train_none_paraphrases_index = list(set(rest_index) - set(test_none_paraphrases_index))
    assert(len(train_none_paraphrases_index) == len(all_none_paraphrases) - 10000)

    # 将训练/验证/测试集写成文件
    ## train set
    print("writing train file...")
    train_index = train_paraphrases_index + train_none_paraphrases_index
    assert(len(train_index) == 404290 - 20000)
    with open("./dataset/train.tsv", "w") as f:
        for p_idx, np_idx in zip(train_paraphrases_index, train_none_paraphrases_index[:len(train_paraphrases_index)]):
            # paraphrase
            paraphrase = all_paraphrases[p_idx]
            f.write(paraphrase[0])
            f.write("\t")
            f.write(paraphrase[1])
            f.write("\t")
            f.write(paraphrase[2])
            f.write("\t")
            f.write(paraphrase[3])
            f.write("\n")

            # none paraphrase
            none_paraphrase = all_none_paraphrases[np_idx]
            f.write(none_paraphrase[0])
            f.write("\t")
            f.write(none_paraphrase[1])
            f.write("\t")
            f.write(none_paraphrase[2])
            f.write("\t")
            f.write(none_paraphrase[3])
            f.write("\n")

    with open("./dataset/train.tsv", "a") as f:
        for np_idx in train_none_paraphrases_index[len(train_paraphrases_index):]:

            # none paraphrase
            none_paraphrase = all_none_paraphrases[np_idx]
            f.write(none_paraphrase[0])
            f.write("\t")
            f.write(none_paraphrase[1])
            f.write("\t")
            f.write(none_paraphrase[2])
            f.write("\t")
            f.write(none_paraphrase[3])
            f.write("\n")
    
    print("train file writing done!")

    ## dev set
    print("writing dev file...")
    dev_index = dev_paraphrases_index + dev_none_paraphrases_index
    assert(len(dev_index) == 10000)
    with open("./dataset/dev.tsv", "w") as f:
        for p_idx, np_idx in zip(dev_paraphrases_index, dev_none_paraphrases_index):
            # paraphrase
            paraphrase = all_paraphrases[p_idx]
            f.write(paraphrase[0])
            f.write("\t")
            f.write(paraphrase[1])
            f.write("\t")
            f.write(paraphrase[2])
            f.write("\t")
            f.write(paraphrase[3])
            f.write("\n")

            # none paraphrase
            none_paraphrase = all_none_paraphrases[np_idx]
            f.write(none_paraphrase[0])
            f.write("\t")
            f.write(none_paraphrase[1])
            f.write("\t")
            f.write(none_paraphrase[2])
            f.write("\t")
            f.write(none_paraphrase[3])
            f.write("\n")

    print("dev file writing done!")

    ## test set
    print("writing test file...")
    test_index = test_paraphrases_index + test_none_paraphrases_index
    assert(len(test_index) == 10000)
    with open("./dataset/test.tsv", "w") as f:
        for p_idx, np_idx in zip(test_paraphrases_index, test_none_paraphrases_index):
            # paraphrase
            paraphrase = all_paraphrases[p_idx]
            f.write(paraphrase[0])
            f.write("\t")
            f.write(paraphrase[1])
            f.write("\t")
            f.write(paraphrase[2])
            f.write("\t")
            f.write(paraphrase[3])
            f.write("\n")

            # none paraphrase
            none_paraphrase = all_none_paraphrases[np_idx]
            f.write(none_paraphrase[0])
            f.write("\t")
            f.write(none_paraphrase[1])
            f.write("\t")
            f.write(none_paraphrase[2])
            f.write("\t")
            f.write(none_paraphrase[3])
            f.write("\n")

    print("test file writing done!")

if __name__ == "__main__":
    paraphrase_file = "./dataset/paraphrases.tsv"
    none_paraphrases_file = "./dataset/none_paraphrases.tsv"

    get_dataset(paraphrase_file, none_paraphrases_file)





