import argparse
from operator import itemgetter


def write_result_file(opt_output, score_dic):
    with open(opt_output, "w") as text_file:
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-task")
    parser.add_argument("-input")
    parser.add_argument("-output")
    args = parser.parse_args()
    opt_task = args.task
    opt_input = args.input
    opt_output = args.output

    print('task: ', opt_task)
    print('input: ', opt_input)
    print('output: ', opt_output)

    weight_list1 = ['0.007656028546428231', '0.012658664405761258', '-0.00895574494736577', '0.007374850747916399',
                    '0.006084378812192495', '-0.005763366011169026', '0.006662164858283657', '0.004620308167815215',
                    '0.007875159462617739', '0.014527758106921806', '0.007754135352833183', '0.010657935599995746',
                    '0.010364677389850922', '0.021409250973690303', '0.032500297032784016', '0.007288616374992879',
                    '0.006983511425779877', '0.007711002341439317', '0.008732856281784806', '0.01930101876072387',
                    '0.007363147666722772', '0.009139355262100048', '0.0073521501818713045', '-0.008468981712518045',
                    '0.007943217290842334', '0.007610306393413046', '0.013605389047648403', '0.022298921092512792',
                    '0.028937509284346626', '0.009816555015760887', '0.11523786785744564', '0.012584527657115412',
                    '0.023551436777316203', '0.006721894622316664', '0.12814567433912197', '0.02215134315653046',
                    '0.007856582442258328', '0.0071917071472321695', '0.0065220832668473165', '0.010113754273619732',
                    '0.01956780354224913', '0.007886230955352952', '0.021720224591243006', '0.007328470710593481',
                    '0.14495396353062381', '0.02462955071372152', '0.01496543331321073', '0.05835901743038865',
                    '0.013061640433376176', '0.0032520377808725348', '0.0075701961008364385', '0.0073510701834528635',
                    '0.007775833585428438', '0.01514312145910292', '0.04502689727567979', '0.039466926622576955',
                    '0.0072374088248271864', '0.044848974986682215', '0.05051309509163598', '0.007428813041617973',
                    '0.020779645050037994', '0.007424907068112095', '0.007022005248114264', '0.009229929940011405',
                    '0.007347299865947434', '0.0073868109426613515', '0.04286581049774908', '0.003902768494636303',
                    '0.0025374371505255734', '0.00810904703491767', '0.011008897986705483', '0.050207794314602955',
                    '0.014401849757938718', '-0.018483605011345373', '0.014852617356067065', '0.007329010879449991',
                    '0.009350247790994127', '0.02119461315798481', '-0.00832011095215198', '-0.006356125193775636',
                    '0.007957943734494044', '0.007617876958549011', '0.007818392147481375', '0.006377196132143984',
                    '0.007911703179999813', '0.02482404679143367', '0.007489585292005202', '0.007374717189536057',
                    '0.008810009998036007', '0.0075935300424773075', '0.10461537009488832', '0.0076707068473272425',
                    '0.00734900450713814', '0.0073488121145322185', '0.0075700107643288045', '0.007352944509492554',
                    '0.006142549977969408', '0.11501622658306826', '0.007548899164451341', '0.006330077596546044',
                    '0.02452285262214027', '0.01993947540554772', '0.04368828742820476', '-0.010910534478009477',
                    '0.02289802092396971', '-0.006328425677345324', '0.006295154162706066', '0.007702939592024485',
                    '0.011922312649215878', '0.1460682943154904', '-0.011024539442777249', '0.00392617834286857',
                    '-0.008066806643453274', '0.02068030105254785', '0.019729863612228483', '0.007981485460324768',
                    '0.08543634582106475', '0.018305168550514717', '-0.017363290667661995', '0.019791086328829942',
                    '0.007440442918033757', '0.013045330364170061', '0.012305097158080166', '0.03129406560981271',
                    '0.007349715963059742', '0.024152505121901854', '0.029712083205416115', '0.028612003955288026',
                    '0.02449340263350139', '0.0073272944918864585', '0.007085457553088937', '0.009955362251839016',
                    '0.007045148804396943', '0.007352373309259918', '0.007964413430777964', '0.007721950308433776']

    weight_list2 = ['0.3296080849059385', '3.8133142768399644', '3.926740389616215', '0.23972239168256268',
                    '1.147587919525394', '3.9692580714958074', '1.3874146358439883', '4.1053229027145095',
                    '0.2995645008088502', '5.684090414441585', '0.35064986428432915', '4.801592962130576',
                    '2.0204852331117618', '5.2519981071351864', '2.601431525197437', '0.11553381128386972',
                    '3.232235209245516', '0.49493476269291364', '2.107238942238899', '5.69617470474362',
                    '0.10548279389887047', '0.8071038175704439', '0.007617406757289715', '3.339673984586884',
                    '3.4828304113878934', '2.4201213145822327', '5.43784061576635', '0.7727222533993482',
                    '0.7410621594466309', '1.70415247952986', '1.0871456072985004', '3.0924960735559988',
                    '5.193646440521253', '3.2481762331540405', '0.9654846051468949', '0.7370708645494662',
                    '0.48415957696657463', '0.210746457551891', '1.2360321391412128', '1.1462459631059467',
                    '4.485969379690464', '0.051640556860574185', '0.7350955585003557', '0.011824169776534771',
                    '0.9674678073080671', '0.743278713735948', '2.6993096095938562', '0.948875273846945',
                    '0.7638623605494433', '1.680013142929823', '2.385946605012087', '0.007584649235326111',
                    '1.106310181663199', '2.451078687713331', '3.609667152030678', '3.3407000009197345',
                    '3.2369530720135735', '4.250773239844871', '0.7694567871406767', '0.2585816019920655',
                    '0.7605047608967108', '0.3100013448888791', '0.5428548835247232', '3.5032192957914847',
                    '3.1816926926347806', '0.8381551406671595', '3.1130693149894615', '4.532344662707476',
                    '3.435847722645004', '2.7204049346214476', '3.7177654288501047', '0.8127717172036606',
                    '2.40544777257304', '0.7565664677474262', '3.566220955225492', '0.24251413051138093',
                    '2.2946034347543582', '1.0888456714254182', '3.522493088674033', '1.8402871915464287',
                    '3.2862979903039005', '0.49628245275830335', '0.6917171915162982', '0.9816920336284072',
                    '0.4051617103406679', '0.7489472122748222', '0.39699621276242225', '0.7675091383033735',
                    '2.6285190756532573', '0.050869324197308795', '1.0066844548679568', '0.34397077300749185',
                    '0.009135361971542051', '0.00933585411412366', '0.9505708800760754', '0.010082323545744327',
                    '1.2876550456164695', '0.984412301700708', '0.8496910818501539', '0.8882974229369206',
                    '0.7524031519069201', '0.7386803111556209', '3.367821017383854', '3.9084328889333504',
                    '0.7716314524687867', '1.8398780764449196', '2.064849558612314', '0.6153388783046968',
                    '4.23599721416153', '1.1501086680364214', '3.9072351412831408', '1.2735098912035367',
                    '3.3419150930037254', '0.7614535369481752', '0.7620971340761897', '0.3235889181841097',
                    '0.9283944910713497', '5.814915762859504', '1.5595593844364553', '0.7364557765691013',
                    '0.40930167809415985', '1.2224212311159637', '5.214685870420125', '3.290657308532004',
                    '0.01902596581601121', '0.7753699519869443', '4.078243736685718', '0.7481848677813506',
                    '0.744953594492284', '0.012179574466341162', '0.607015485904837', '3.7562375824312935',
                    '3.1770738217741985', '0.01743898327599129', '0.5272336622698388', '2.3475413385024395']

    weight_list3 = ['0.7643927064039671', '8.147990340565954', '5.242630483151101', '0.5555836139088985',
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

    rel_list = readfile_to_list(opt_input, '\n')
    max_and_min_feature_list = [max_feature_list, min_feature_list]

    score_dic = {}
    if opt_task == '1':
        score_dic = doc_score(weight_list1, max_and_min_feature_list, rel_list)
    elif opt_task == '2':
        score_dic = doc_score(weight_list2, max_and_min_feature_list, rel_list)
    elif opt_task == '3':
        score_dic = doc_score(weight_list3, max_and_min_feature_list, rel_list)

    write_result_file(opt_output, score_dic)
    return None


main()