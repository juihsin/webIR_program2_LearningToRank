import sqlite3
import uuid
from operator import itemgetter
from random import randint
import math
import os


def get_all_query_id():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()
    all_query_id = []
    for row in c.execute('''SELECT DISTINCT QueryID FROM Training'''):
        all_query_id.extend(row)
    conn.commit()
    conn.close()
    return all_query_id


def get_rel_train(query_num, all_query_id):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()
    rel_list = {}
    qid_set_index = []
    for num in range(0, query_num):
        print("get query" + str(num))
        rand_qid_index = randint(2, len(all_query_id))
        while rand_qid_index in qid_set_index:
            rand_qid_index = randint(2, len(all_query_id))
        else:
            qid_set_index.append(rand_qid_index)
            rand_qid = all_query_id[rand_qid_index]

        for row in c.execute('''SELECT * FROM Training WHERE QueryID=?''', [rand_qid]):
            doc_tuple = row[4:140]
            doc_tuple = list(doc_tuple)
            doc_tuple.insert(0, row[1])
            doc_tuple = tuple(doc_tuple)

            query_id = row[2]
            if query_id in rel_list:
                rel_list[query_id].append(doc_tuple)
            else:
                doc_tuple_list = [doc_tuple]
                rel_list[query_id] = doc_tuple_list
    conn.commit()
    conn.close()
    return rel_list


def get_max_and_min_feature():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()

    max_and_min_feature_list = []
    for row in c.execute('''SELECT * FROM Max_min_feature'''):
        max_and_min_feature_list.append(row)

    conn.commit()
    conn.close()
    return max_and_min_feature_list


def readfile_to_list(filepath, delim):
    data = []
    with open(filepath, 'r') as f:
        lines = f.read().split(delim)
        for line in lines:
            cols = line.split(' ')
            cols.pop(0)
            row = []
            for col in cols:
                row.append(col.split(':')[1])
            data.append(tuple(row))
    return data


def differential_train(weight_list, rel_list_now, max_and_min_feature_list):
    differential_result = []
    for doc_num in range(0, len(rel_list_now)):  # TODO: doc 的個數
        doc = rel_list_now[doc_num]
        relevance = float(doc[0])
        feature_list = doc[1:len(doc)]

        new_differ_result = []
        for index in range(0, len(weight_list)):  # TODO: 讀 136 個 features
            # print("[feature" + str(index + 1) + "]")
            feature = float(feature_list[index])
            feature = normalize(feature, max_and_min_feature_list, index)  # TODO: normalize
            weight = float(weight_list[index])
            wx = weight * feature
            differential_every_feature = (-2) * feature * (relevance + 1) * (relevance - wx)

            # if weight > 1:
            #     print("feature after nor: " + str(feature))
            #     print("weight: " + str(weight))
            #     print("relevance: " + str(relevance))
            #     print("wx: " + str(wx))
            #     print(
            #         "differential_every_feature((-2) * feature * (relevance - wx)): " + str(differential_every_feature))
            #     print("\n")

            if doc_num == 0:
                new_differ_result.append(differential_every_feature)
            else:
                diff = differential_result[index]
                diff = diff + differential_every_feature
                new_differ_result.append(diff)
        # print("new_differ_result: " + str(new_differ_result))
        differential_result = new_differ_result
        # for d in differential_result:
        #     print(str(d) + ',', end='', flush=True)
    return differential_result


def normalize(feature_of_x, max_and_min_feature_list, index):
    max_feature_list = max_and_min_feature_list[0]
    min_feature_list = max_and_min_feature_list[1]
    max_feature = max_feature_list[index]
    min_feature = min_feature_list[index]
    feature_of_x = (feature_of_x - min_feature) / (max_feature - min_feature)
    return feature_of_x


def renew_weight(weight_list, differential_result, doc_num):
    new_weight_list = []
    for index in range(0, len(weight_list)):
        weight_by_feature = weight_list[index]
        differential_by_feature = differential_result[index]
        # print("old weight_by_feature: " + str(weight_by_feature))
        # print("weight_by_feature: " + str(differential_by_feature))
        learning_rate = 0.02  # TODO: 調整 learning rate
        weight_by_feature = weight_by_feature - learning_rate * differential_by_feature / doc_num

        if math.isnan(weight_by_feature):
            weight_by_feature = 0

        # print("new weight_by_feature: " + str(weight_by_feature))
        new_weight_list.append(weight_by_feature)
    return new_weight_list


def get_loss_function_value(weight_list, max_and_min_feature_list, rel_list):
    loss_value = 0.0
    for qid in rel_list.keys():
        for doc in rel_list[qid]:
            score = 0.0
            rel = float(doc[0])
            feature_list = doc[1:len(doc)]
            for index in range(0, len(weight_list)):
                weight = float(weight_list[index])
                feature = float(feature_list[index])
                feature = normalize(feature, max_and_min_feature_list, index)  # TODO: normalize
                wx = weight * feature
                score = score + wx
            loss_value = loss_value + pow((rel - score), 2)
    return loss_value


def doc_score(weight_list, max_and_min_feature_list, rel_list):
    score_dic = {}
    for doc in rel_list:
        score = 0.0
        query_id = doc[0]
        doc_id = doc[1]
        feature_list = doc[2:138]
        for index in range(0, len(weight_list)):
            weight = float(weight_list[index])
            feature = float(feature_list[index])
            feature = normalize(feature, max_and_min_feature_list, index)  # TODO: normalize
            wx = weight * feature
            score = score + wx
        score_per_doc = (doc_id, score)
        if query_id in score_dic:
            score_dic[query_id].append(score_per_doc)
        else:
            score_list = [score_per_doc]
            score_dic[query_id] = score_list

    score_dic_new = {}
    for query_id in score_dic.keys():
        score_list_sort = sorted(score_dic[query_id], key=itemgetter(1), reverse=True)
        score_dic_new[query_id] = score_list_sort[0:10]
    return score_dic_new


def write_result_file(score_dic):
    with open("out3.txt", "w") as text_file:
        print("QueryId,DocumentId", file=text_file)
        for qid in score_dic.keys():
            for doc_score_tuple in score_dic[qid]:
                print("{}".format(str(qid) + "," + str(doc_score_tuple[0])), file=text_file)
    return None


def main():
    # TODO: Training
    weight_list = [1.0 / 136.0] * 136
    all_query_id = get_all_query_id()
    # query_id_set_list = random_sample_query(2000, all_query_id)  # TODO: 2000 筆 query
    # rel_list = get_rel_train(query_id_set_list)
    # rel_list = format_doc_set(query_id_set_list, rel_list)
    rel_list = get_rel_train(300, all_query_id)  # TODO: 300 筆 query
    print("Get training data finish!")
    max_feature_list = [277.0, 218.033568, 16.0, 856.0, 4040.0, 16.0, 1678.5, 265.0, 86.0, 15.0, 315.0, 1.0, 1.0,
                        1.636364, 1.0, 121.0, 26096.399767, 2580.061807, 0.09, 0.757377, 3233.0, 1.0, 10343023.179426,
                        121.077417, 9.0, 1.0, 1.851064, 0.0, 0.705756, 42.0, 1.0, 1.0, 3.0, 3.0, 1.0, 0.0, 86.0, 6669.0,
                        1672.5, 42.0, 0.757377, 2789632.0, 0.0, 2763906.25, 1.0, 0.705644, 136.783001, 65535.0, 1.0,
                        1.0, 8667.005515, 161696.888889, 1.0, 168.788808, 0.617647, 1.0, 13048.199883, 0.617647, 1.0,
                        6857.293941, 0.0, 0.25, 25963.491963, 3.0, 13075.29137, 1552.0, 1.0, 1549.0, 97.0, 135.169415,
                        301.683641, 1.0, 254.0, 1.0, 168.788808, 4514.730882, 42.0, 1.0, 128.560046, 43.221589,
                        65.075948, 315.0, 771.111504, 3347.0, 2058.949308, 0.0, 6927.854528, 314131554.0, 52.0,
                        13544625.0, 1.0, 2287.866383, 166804769.503892, 167505292.377452, 1579.0, 980000001.0, 4040.0,
                        1.0, 0.0625, 3335.0, 0.0, 0.0, 0.617647, 13540.0, 0.0, 43.215106, 0.25, 94.0, 1.0, 65534.0,
                        13554.0, 0.25, 113.046133, 1.0, 0.0, 695.932703, 1.0, 0.757377, 254.0, 0.0, 862.0, 1.0, 15.0,
                        73.169271, 148653.237799, 0.0, 72.19844, 0.0, 0.0, 2783892.25, 26017.674936, 178.0, 26150.58274,
                        2209.0, 706.513591, 8674.545513]
    min_feature_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -6809.256888,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.725981, 0.0, 0.0, 0.0, -138.203961, -174.793032, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, -160.344508, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -163.438492, 0.0, 0.0, -169.913234,
                        -15.386967, 1.0, 0.0, 0.0, -3404.628444, 0.0, 0.0, 0.0, 0.0, 0.0, -3404.628444, 0.0, 0.0, 0.0,
                        -139.367787, 0.0, 0.0, 0.0, -3483.406367, 0.0, 0.0, 4.0, 1.0, -15.300321, 0.0, 0.0, 1.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 2.001239, -4.387408, 0.0, 0.0, 0.0, 0.0, 0.0, -141.712421, 0.0,
                        -2083777989.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -162.903042,
                        -160.149259, 0.0, 0.0, -161.336069, -4.412168, 0.0, 0.0, 0.0, 100.0, 2.0, 0.0, 1.993372, 0.0,
                        -139.196935, 0.0, 0.0, 0.0, 1.0, -163.220923, 0.0, 0.0, 0.0, 0.0, 0.0, -143.962503, 0.0,
                        -146.691595, -190.997484, 0.0, 0.0, 0.0, -6966.812734, 0.0, 0.0, -3483.406367]
    max_and_min_feature_list = [max_feature_list, min_feature_list]

    differential_result = []
    for iter_num in range(0, 100):  # TODO: iteration 次數
        print("[[[iter " + str(iter_num + 1) + "]]]")
        for query_id in rel_list.keys():
            rel_list_now = rel_list[query_id]
            differential_result = differential_train(weight_list, rel_list_now, max_and_min_feature_list)
            doc_num = len(rel_list_now)
            weight_list = renew_weight(weight_list, differential_result, doc_num)

        if iter_num == 99:
            print("微分結果: " + str(differential_result))
            print("\nfinal weight: ")
            for w in weight_list:
                print("'" + str(w) + "',", end='', flush=True)

    # TODO: Loss function
    loss_value = get_loss_function_value(weight_list, max_and_min_feature_list, rel_list)
    print("loss value: " + str(loss_value) + "\n")

    # TODO: Testing
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "../data/test.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    rel_list = readfile_to_list(abs_file_path, '\n')
    score_dic = doc_score(weight_list, max_and_min_feature_list, rel_list)
    write_result_file(score_dic)

    return None


main()
