import sqlite3
import uuid
from operator import itemgetter
import math
import os


def create_table():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()
    c.execute('''CREATE TABLE Training(
        ID TEXT PRIMARY KEY,
        Relevance TEXT,
        QueryID TEXT,
        DocID TEXT,
        Feature1 TEXT,
        Feature2 TEXT,
        Feature3 TEXT,
        Feature4 TEXT,
        Feature5 TEXT,
        Feature6 TEXT,
        Feature7 TEXT,
        Feature8 TEXT,
        Feature9 TEXT,
        Feature10 TEXT,
        Feature11 TEXT,
        Feature12 TEXT,
        Feature13 TEXT,
        Feature14 TEXT,
        Feature15 TEXT,
        Feature16 TEXT,
        Feature17 TEXT,
        Feature18 TEXT,
        Feature19 TEXT,
        Feature20 TEXT,
        Feature21 TEXT,
        Feature22 TEXT,
        Feature23 TEXT,
        Feature24 TEXT,
        Feature25 TEXT,
        Feature26 TEXT,
        Feature27 TEXT,
        Feature28 TEXT,
        Feature29 TEXT,
        Feature30 TEXT,
        Feature31 TEXT,
        Feature32 TEXT,
        Feature33 TEXT,
        Feature34 TEXT,
        Feature35 TEXT,
        Feature36 TEXT,
        Feature37 TEXT,
        Feature38 TEXT,
        Feature39 TEXT,
        Feature40 TEXT,
        Feature41 TEXT,
        Feature42 TEXT,
        Feature43 TEXT,
        Feature44 TEXT,
        Feature45 TEXT,
        Feature46 TEXT,
        Feature47 TEXT,
        Feature48 TEXT,
        Feature49 TEXT,
        Feature50 TEXT,
        Feature51 TEXT,
        Feature52 TEXT,
        Feature53 TEXT,
        Feature54 TEXT,
        Feature55 TEXT,
        Feature56 TEXT,
        Feature57 TEXT,
        Feature58 TEXT,
        Feature59 TEXT,
        Feature60 TEXT,
        Feature61 TEXT,
        Feature62 TEXT,
        Feature63 TEXT,
        Feature64 TEXT,
        Feature65 TEXT,
        Feature66 TEXT,
        Feature67 TEXT,
        Feature68 TEXT,
        Feature69 TEXT,
        Feature70 TEXT,
        Feature71 TEXT,
        Feature72 TEXT,
        Feature73 TEXT,
        Feature74 TEXT,
        Feature75 TEXT,
        Feature76 TEXT,
        Feature77 TEXT,
        Feature78 TEXT,
        Feature79 TEXT,
        Feature80 TEXT,
        Feature81 TEXT,
        Feature82 TEXT,
        Feature83 TEXT,
        Feature84 TEXT,
        Feature85 TEXT,
        Feature86 TEXT,
        Feature87 TEXT,
        Feature88 TEXT,
        Feature89 TEXT,
        Feature90 TEXT,
        Feature91 TEXT,
        Feature92 TEXT,
        Feature93 TEXT,
        Feature94 TEXT,
        Feature95 TEXT,
        Feature96 TEXT,
        Feature97 TEXT,
        Feature98 TEXT,
        Feature99 TEXT,
        Feature100 TEXT,
        Feature101 TEXT,
        Feature102 TEXT,
        Feature103 TEXT,
        Feature104 TEXT,
        Feature105 TEXT,
        Feature106 TEXT,
        Feature107 TEXT,
        Feature108 TEXT,
        Feature109 TEXT,
        Feature110 TEXT,
        Feature111 TEXT,
        Feature112 TEXT,
        Feature113 TEXT,
        Feature114 TEXT,
        Feature115 TEXT,
        Feature116 TEXT,
        Feature117 TEXT,
        Feature118 TEXT,
        Feature119 TEXT,
        Feature120 TEXT,
        Feature121 TEXT,
        Feature122 TEXT,
        Feature123 TEXT,
        Feature124 TEXT,
        Feature125 TEXT,
        Feature126 TEXT,
        Feature127 TEXT,
        Feature128 TEXT,
        Feature129 TEXT,
        Feature130 TEXT,
        Feature131 TEXT,
        Feature132 TEXT,
        Feature133 TEXT,
        Feature134 TEXT,
        Feature135 TEXT,
        Feature136 TEXT)''')

    conn.commit()
    conn.close()
    return None


def insert_db(data):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    conn.text_factory = str
    c = conn.cursor()
    c.executemany(
        '''INSERT INTO Training VALUES (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)

    conn.commit()
    conn.close()
    return None


def create_max_min_table():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()

    c.execute('''CREATE TABLE Max_min_feature(
        ID TEXT PRIMARY KEY,
        Type TEXT,
        Feature1 TEXT,
        Feature2 TEXT,
        Feature3 TEXT,
        Feature4 TEXT,
        Feature5 TEXT,
        Feature6 TEXT,
        Feature7 TEXT,
        Feature8 TEXT,
        Feature9 TEXT,
        Feature10 TEXT,
        Feature11 TEXT,
        Feature12 TEXT,
        Feature13 TEXT,
        Feature14 TEXT,
        Feature15 TEXT,
        Feature16 TEXT,
        Feature17 TEXT,
        Feature18 TEXT,
        Feature19 TEXT,
        Feature20 TEXT,
        Feature21 TEXT,
        Feature22 TEXT,
        Feature23 TEXT,
        Feature24 TEXT,
        Feature25 TEXT,
        Feature26 TEXT,
        Feature27 TEXT,
        Feature28 TEXT,
        Feature29 TEXT,
        Feature30 TEXT,
        Feature31 TEXT,
        Feature32 TEXT,
        Feature33 TEXT,
        Feature34 TEXT,
        Feature35 TEXT,
        Feature36 TEXT,
        Feature37 TEXT,
        Feature38 TEXT,
        Feature39 TEXT,
        Feature40 TEXT,
        Feature41 TEXT,
        Feature42 TEXT,
        Feature43 TEXT,
        Feature44 TEXT,
        Feature45 TEXT,
        Feature46 TEXT,
        Feature47 TEXT,
        Feature48 TEXT,
        Feature49 TEXT,
        Feature50 TEXT,
        Feature51 TEXT,
        Feature52 TEXT,
        Feature53 TEXT,
        Feature54 TEXT,
        Feature55 TEXT,
        Feature56 TEXT,
        Feature57 TEXT,
        Feature58 TEXT,
        Feature59 TEXT,
        Feature60 TEXT,
        Feature61 TEXT,
        Feature62 TEXT,
        Feature63 TEXT,
        Feature64 TEXT,
        Feature65 TEXT,
        Feature66 TEXT,
        Feature67 TEXT,
        Feature68 TEXT,
        Feature69 TEXT,
        Feature70 TEXT,
        Feature71 TEXT,
        Feature72 TEXT,
        Feature73 TEXT,
        Feature74 TEXT,
        Feature75 TEXT,
        Feature76 TEXT,
        Feature77 TEXT,
        Feature78 TEXT,
        Feature79 TEXT,
        Feature80 TEXT,
        Feature81 TEXT,
        Feature82 TEXT,
        Feature83 TEXT,
        Feature84 TEXT,
        Feature85 TEXT,
        Feature86 TEXT,
        Feature87 TEXT,
        Feature88 TEXT,
        Feature89 TEXT,
        Feature90 TEXT,
        Feature91 TEXT,
        Feature92 TEXT,
        Feature93 TEXT,
        Feature94 TEXT,
        Feature95 TEXT,
        Feature96 TEXT,
        Feature97 TEXT,
        Feature98 TEXT,
        Feature99 TEXT,
        Feature100 TEXT,
        Feature101 TEXT,
        Feature102 TEXT,
        Feature103 TEXT,
        Feature104 TEXT,
        Feature105 TEXT,
        Feature106 TEXT,
        Feature107 TEXT,
        Feature108 TEXT,
        Feature109 TEXT,
        Feature110 TEXT,
        Feature111 TEXT,
        Feature112 TEXT,
        Feature113 TEXT,
        Feature114 TEXT,
        Feature115 TEXT,
        Feature116 TEXT,
        Feature117 TEXT,
        Feature118 TEXT,
        Feature119 TEXT,
        Feature120 TEXT,
        Feature121 TEXT,
        Feature122 TEXT,
        Feature123 TEXT,
        Feature124 TEXT,
        Feature125 TEXT,
        Feature126 TEXT,
        Feature127 TEXT,
        Feature128 TEXT,
        Feature129 TEXT,
        Feature130 TEXT,
        Feature131 TEXT,
        Feature132 TEXT,
        Feature133 TEXT,
        Feature134 TEXT,
        Feature135 TEXT,
        Feature136 TEXT)''')

    conn.commit()
    conn.close()

    return None


def insert_feature_to_db(feature_list):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    conn.text_factory = str
    c = conn.cursor()

    c.executemany(
        '''INSERT INTO Max_min_feature VALUES (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', feature_list)

    conn.commit()
    conn.close()
    return


def query_db():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()
    print('iterate select query:')
    for row in c.execute('''SELECT * FROM Training LIMIT 10'''):
        print(row)
        # for item in row:
        # print(item)
        # print(str(item), end='', flush=True)
    return None


def readfile(filepath, delim):
    data = []
    with open(filepath, 'r') as f:
        lines = f.read().split(delim)
        for line in lines:
            cols = line.split(' ')
            row = []
            row.insert(0, str(uuid.uuid4()))
            row.append(cols.pop(0))
            for col in cols:
                row.append(col.split(':')[1])
            data.append(tuple(row))
    print(len(data))
    return data


def get_rel_train():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()

    high_rel_list = []
    low_rel_list = []

    # TODO: 調整 pair 的個數: LIMIT relevance=4 的個數
    for row in c.execute('''SELECT * FROM Training WHERE Relevance=? ORDER BY random()''', ['4']):
        high_rel_list.append(row[3:140])

    high_rel_num = len(high_rel_list)
    for row in c.execute(
            '''SELECT * FROM Training WHERE Relevance=? ORDER BY random() LIMIT ?''', ['0', high_rel_num]):
        low_rel_list.append(row[3:140])

    conn.commit()
    conn.close()
    rel_list = [high_rel_list, low_rel_list]
    return rel_list


# def get_max_and_min_feature():
#     script_dir = os.path.dirname(os.path.realpath(__file__))
#     rel_path = "learningToRank.db"
#     abs_file_path = os.path.join(script_dir, rel_path)
#     conn = sqlite3.connect(str(abs_file_path))
#     c = conn.cursor()
#
#     max_and_min_feature_list = []
#     for row in c.execute('''SELECT * FROM Max_min_feature'''):
#         max_and_min_feature_list.append(row)
#
#     conn.commit()
#     conn.close()
#     return max_and_min_feature_list

def get_max_and_min_feature():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()

    feature_dic = {}
    for row in c.execute('''SELECT * FROM Training'''):
        for item_index in range(4, len(row)):
            item_list = []
            item = float(row[item_index])
            if item_index - 3 in feature_dic:
                feature_dic[item_index - 3].append(item)
            else:
                item_list.append(item)
                feature_dic[item_index - 3] = item_list

    max_feature_list = []
    min_feature_list = []
    for feature_num in feature_dic.keys():
        doc_by_feature = sorted(feature_dic[feature_num])
        # print(doc_by_feature)
        max_feature = doc_by_feature[len(doc_by_feature) - 1]
        max_feature_list.append(max_feature)
        min_feature = doc_by_feature[0]
        min_feature_list.append(min_feature)
    max_and_min_feature_list = [max_feature_list, min_feature_list]

    conn.commit()
    conn.close()
    return max_and_min_feature_list


def get_rel_test():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "learningToRank.db"
    abs_file_path = os.path.join(script_dir, rel_path)
    conn = sqlite3.connect(str(abs_file_path))
    c = conn.cursor()

    rel_list = []
    for row in c.execute('''SELECT * FROM Testing'''):
        rel_list.append(row[2:140])

    conn.commit()
    conn.close()

    return rel_list


def read_testfile_to_list(filepath, delim):
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


def pair_format(high_rel_list, low_rel_list):
    pair_list = []
    for iter_num in range(0, len(high_rel_list)):  # TODO: pair 個數
        x_high_rel = high_rel_list[iter_num]
        x_low_rel = low_rel_list[iter_num]
        pair = [x_high_rel, x_low_rel]
        pair_list.append(pair)
    return pair_list


def differential(weight_list, pair_list, max_and_min_feature_list):
    differential_result = []
    for iter_num in range(0, len(pair_list)):  # TODO: 拿出 pair 的個數
        pair = pair_list[iter_num]
        x_high_rel = pair[0]
        x_low_rel = pair[1]

        new_differ_result = []
        for index in range(0, len(weight_list)):  # TODO: 讀 136 個 features
            # print("[feature" + str(index + 1) + "]")
            feature_of_x_high = float(x_high_rel[index + 1])
            feature_of_x_low = float(x_low_rel[index + 1])
            feature_of_x_high = normalize(feature_of_x_high, max_and_min_feature_list, index)
            feature_of_x_low = normalize(feature_of_x_low, max_and_min_feature_list, index)
            weight = float(weight_list[index])

            w_multiple_feature_high = weight * feature_of_x_high
            w_multiple_feature_low = weight * feature_of_x_low

            try:
                a = math.exp(w_multiple_feature_low - w_multiple_feature_high)
            except OverflowError:
                a = float('inf')

            b = feature_of_x_low - feature_of_x_high

            try:
                ex = math.exp(weight * b / (1 + a))
            except OverflowError:
                ex = float('inf')

            pow1 = pow(b, 2) * weight * a

            try:
                pow2 = pow((1 + a), 2)
            except OverflowError:
                pow2 = float('inf')

            differential_every_feature = ((b / (1 + a)) - (pow1 / pow2)) * ex / (1 + ex)

            if math.isnan(differential_every_feature):
                # print("weight: " + str(weight))
                # print("x1: " + str(feature_of_x_high) + ", x2: " + str(feature_of_x_low))
                # print("wx1: " + str(w_multiple_feature_high) + ", wx2: " + str(w_multiple_feature_low))
                # print("exp(wx2-wx1):    " + str(a))
                # print("x2-x1:           " + str(b))
                # print("e^(wb/(1+a)):    " + str(ex))
                # print("pow1:    " + str(pow1))
                # print("pow2:    " + str(pow2))
                # print("differential_every_feature: " + str(differential_every_feature))
                differential_every_feature = 0

            if iter_num == 0:
                differential_result.append(differential_every_feature)
            else:
                diff = differential_result[index]
                diff = diff + differential_every_feature
                new_differ_result.append(diff)

        if iter_num != 0:
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


def renew_weight(weight_list, differential_result, pair_list_length):
    new_weight_list = []
    for index in range(0, len(weight_list)):
        weight_by_feature = weight_list[index]
        differential_by_feature = differential_result[index]
        # print("old weight_by_feature: " + str(weight_by_feature))

        if math.isnan(differential_by_feature):
            print("weight_by_feature: " + str(differential_by_feature))

        learning_rate = 0.02  # TODO: 調整 learning rate
        weight_by_feature = weight_by_feature - learning_rate * differential_by_feature / pair_list_length
        # TODO: ＾＾＾pair 數＾＾＾
        # print("new weight_by_feature: " + str(weight_by_feature))
        new_weight_list.append(weight_by_feature)
    return new_weight_list


def renew_weight_by_iteration(weight_list, pair_list, max_and_min_feature_list):
    for iter_num in range(0, 100):  # TODO: iteration 的次數
        print("[[[iter " + str(iter_num + 1) + "]]]")
        differential_result = differential(weight_list, pair_list, max_and_min_feature_list)
        pair_list_length = len(pair_list)
        weight_list = renew_weight(weight_list, differential_result, pair_list_length)

        if iter_num == 99:
            print("final weight: ")
            for w in weight_list:
                print("'" + str(w) + "',", end='', flush=True)
    return weight_list


def get_loss_function_value(weight_list, max_and_min_feature_list, pair_list):
    loss_value = 0.0
    for iter_num in range(0, len(pair_list)):  # TODO: 拿出 pair 的個數
        pair = pair_list[iter_num]
        x_high_rel = pair[0]
        x_low_rel = pair[1]
        high_score = 0.0
        low_score = 0.0
        for index in range(0, len(weight_list)):  # TODO: 讀 136 個 features
            feature_of_x_high = float(x_high_rel[index + 1])
            feature_of_x_low = float(x_low_rel[index + 1])
            feature_of_x_high = normalize(feature_of_x_high, max_and_min_feature_list, index)
            feature_of_x_low = normalize(feature_of_x_low, max_and_min_feature_list, index)
            weight = float(weight_list[index])
            high_wx = weight * feature_of_x_high
            low_wx = weight * feature_of_x_low
            high_score = high_score + high_wx
            low_score = low_score + low_wx
        loss_value = loss_value + math.log(1 + math.exp(low_score - high_score))
    return loss_value


def doc_score(weight_list, max_and_min_feature_list, rel_list):
    score_dic = {}
    for doc in rel_list:
        score = 0.0
        query_id = doc[0]
        doc_id = doc[1]
        # print("doc: " + str(doc_id))
        # print("doc: " + str(doc_id))
        feature_list = doc[2:138]
        for index in range(0, len(weight_list)):
            weight = float(weight_list[index])
            feature = float(feature_list[index])
            feature = normalize(feature, max_and_min_feature_list, index)  # TODO: normalize
            wx = weight * feature
            try:
                sigmoid = 1 / (1 + math.exp(-feature))
            except OverflowError:
                sigmoid = 1
            score = score + sigmoid * wx
            # score = score + wx
        score_per_doc = (doc_id, score)
        if query_id in score_dic:
            score_dic[query_id].append(score_per_doc)
        else:
            score_list = [score_per_doc]
            score_dic[query_id] = score_list
    # print("score_dic_before_sort: \n" + str(score_dic))

    score_dic_new = {}
    for query_id in score_dic.keys():
        score_list_sort = sorted(score_dic[query_id], key=itemgetter(1), reverse=True)
        score_dic_new[query_id] = score_list_sort[0:10]
    # print("score_dic_after_sort: \n" + str(score_dic_new))
    return score_dic_new


def write_result_file(score_dic):
    with open("out1.txt", "w") as text_file:
        print("QueryId,DocumentId", file=text_file)
        for qid in score_dic.keys():
            for doc_score_tuple in score_dic[qid]:
                print("{}".format(str(qid) + "," + str(doc_score_tuple[0])), file=text_file)
    return None


def main():
    """ DB relation """
    # create_table()
    #
    # script_dir = os.path.dirname(os.path.realpath(__file__))
    # rel_path = "../data/train.txt"
    # abs_file_path = os.path.join(script_dir, rel_path)
    # insert_db(readfile(abs_file_path, '\n'))
    #
    # create_max_min_table()
    # get_max_and_min_feature()
    # print("max:\n" + str(max_and_min_feature_list[0]))
    # print("min:\n" + str(max_and_min_feature_list[1]))
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
    # insert_feature_to_db(tuple(max_feature_list))
    # insert_feature_to_db(tuple(min_feature_list))

    # query_db()

    # TODO: Training
    weight_list = [1.0 / 136.0] * 136
    rel_list = get_rel_train()
    max_and_min_feature_list = [max_feature_list, min_feature_list]
    # print("max:\n" + str(max_and_min_feature_list[0]))
    # print("min:\n" + str(max_and_min_feature_list[1]))
    high_rel_list = rel_list[0]
    low_rel_list = rel_list[1]
    pair_list = pair_format(high_rel_list, low_rel_list)
    weight_list = renew_weight_by_iteration(weight_list, pair_list, max_and_min_feature_list)

    # TODO: Loss function
    loss_value = get_loss_function_value(weight_list, max_and_min_feature_list, pair_list)
    print("loss value: " + str(loss_value) + "\n")

    # TODO: Testing
    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "../data/test.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    rel_list = read_testfile_to_list(abs_file_path, '\n')
    score_dic = doc_score(weight_list, max_and_min_feature_list, rel_list)
    write_result_file(score_dic)

    return None


main()
