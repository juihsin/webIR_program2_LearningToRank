from operator import itemgetter

import bigfloat
import os
from bigfloat import BigFloat


def write_result_file(score_dic):
    with open("out3.txt", "w") as text_file:
        print("QueryId,DocumentId", file=text_file)
        for qid in score_dic.keys():
            for doc_score_tuple in score_dic[qid]:
                print("{}".format(str(qid) + "," + str(doc_score_tuple[0])), file=text_file)
    return None


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


def normalize(feature_of_x, max_and_min_feature_list, index):
    max_feature_list = max_and_min_feature_list[0]
    min_feature_list = max_and_min_feature_list[1]
    max_feature = max_feature_list[index]
    min_feature = min_feature_list[index]
    feature_of_x = (feature_of_x - min_feature) / (max_feature - min_feature)
    return feature_of_x


def main():
    weight_list = ['0.7643927064039671', '8.147990340565954', '5.242630483151101', '0.5555836139088985',
                   '2.6071620481902595', '5.31224125934428', '3.125770691279782', '8.214282509751971',
                   '0.7360974222649234', '7.7616543154027235', '0.8436694455670583', '8.712793939152082',
                   '2.8481021810227776', '8.246541026847327', '3.5638983617681967', '0.2585499011783811',
                   '4.463220325926589', '1.160053093649624', '4.498134954887511', '10.409092280013843',
                   '0.2231946756181903', '1.0667073519307768', '0.008556590647385797', '4.502725290794837',
                   '5.288888018687528', '3.2001033707764313', '10.560105604650383', '1.0512148689998273',
                   '0.9907420444144678', '3.9080451934471068', '1.4484681920418487', '6.253536517062158',
                   '7.129261931076374', '5.0149884020178455', '1.3061601067353708', '0.9862007246719605',
                   '1.1093076483075721', '0.47900223591209934', '2.7761230755278303', '2.7040190225639',
                   '8.669362336682584', '0.10605940325452586', '0.9828616115730634', '0.01798332876724914',
                   '1.284621769424317', '1.0057538934925623', '3.629758145912913', '1.284067807381074',
                   '0.9843510563107396', '2.24452935536198', '3.299493111891646', '0.007959451622016238',
                   '1.416931783662072', '5.5751321500403455', '5.326014803610078', '4.50542783878659',
                   '4.471959742673766', '5.962637797639219', '0.9797443790264615', '0.5961520831310334',
                   '1.022063096547892', '0.5624692426912903', '1.1974040528067067', '7.472314415221831',
                   '4.395263797988813', '1.8848011468713053', '4.212902748069407', '8.957995825815619',
                   '6.705692313081286', '3.6550819055821644', '7.881799258708074', '1.0676711187155274',
                   '3.4912839452593656', '0.9899334177468396', '7.7382029333112525', '0.5492824473056397',
                   '5.163061366149822', '1.4159846930743443', '4.723921478781025', '2.458628800800176',
                   '4.638642082965788', '1.1656324439530672', '1.5383080589195497', '2.2210964190890334',
                   '0.9827285476141958', '1.0142292994329722', '0.9237751582292145', '1.0380257841103098',
                   '5.806397289109345', '0.050314281863090234', '1.3128598535213842', '0.7931033288755582',
                   '0.011420462394283978', '0.011950760187601108', '2.1528647685686146', '0.01693254224954875',
                   '2.929667027647434', '1.3330037231510488', '1.9749229242211364', '2.002720714661514',
                   '1.0162994748363934', '0.9885522690372659', '4.649244168084603', '5.866439993276383',
                   '1.0464610013634952', '2.458706235653373', '3.3272230992430365', '1.3662790256711237',
                   '8.23992161947114', '1.6419982956908838', '5.8938998103251325', '1.8735622040711664',
                   '4.465646525038462', '0.9895659552952868', '1.0245464383781617', '0.7950078783094975',
                   '1.2249520817395145', '9.586801523381157', '2.283186882412103', '0.9849392232914328',
                   '0.9608763532080137', '1.5452438190139033', '8.562378518255423', '4.3869510837134404',
                   '0.02845168498534214', '1.0485507184455756', '5.537801667195832', '1.0023726990501856',
                   '1.0046406172158553', '0.01881970007923866', '1.3473477933905704', '6.681923588868126',
                   '4.386652048873895', '0.026342597067692954', '1.2113489247393545', '3.246215596345057']

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

    script_dir = os.path.dirname(os.path.realpath(__file__))
    rel_path = "../data/test.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    rel_list = readfile_to_list(abs_file_path, '\n')
    max_and_min_feature_list = [max_feature_list, min_feature_list]
    score_dic = doc_score(weight_list, max_and_min_feature_list, rel_list)
    write_result_file(score_dic)
    return None


main()
