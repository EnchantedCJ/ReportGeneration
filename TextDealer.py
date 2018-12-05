# -*- coding:utf-8 -*-
import json
from pprint import pprint


def read_text():
    with open('./input/text/text.json', 'r', encoding='utf-8') as f:
        textData = f.read()
    text = json.loads(textData)

    ds = []
    with open('./input/text/thu.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            list = line.strip('\n').split()
            ds.append(list)
    text['thu']['state'] = ds

    # pprint(text['thu'])
    return text


def write_text(template, text, figures):
    pprint(text)
    pprint(figures)
    report = template.format(
        eq_depth=text['eq']['depth'],
        eq_lat=text['eq']['lat'],
        eq_lng=text['eq']['lng'],
        eq_loc=text['eq']['loc'],
        eq_mag=text['eq']['mag'],
        eq_name=text['eq']['name'],
        eq_num=text['eq']['num'],
        eq_time=text['eq']['time'],

        region_name=text['region']['name'],

        bridge1_state=text['single']['bridge1']['state'],
        bridge2_state=text['single']['bridge2']['state'],
        mason1_state=text['single']['mason1']['state'],
        mason2_state=text['single']['mason2']['state'],

        station_lat=text['station']['lat'],
        station_lng=text['station']['lng'],
        station_name=text['station']['name'],
        station_pgah=text['station']['pgah'],
        station_pgav=text['station']['pgav'],

        thu00=text['thu']['state'][0][0],
        thu01=text['thu']['state'][0][1],
        thu02=text['thu']['state'][0][2],
        thu10=text['thu']['state'][1][0],
        thu11=text['thu']['state'][1][1],
        thu12=text['thu']['state'][1][2],
        thu20=text['thu']['state'][2][0],
        thu21=text['thu']['state'][2][1],
        thu22=text['thu']['state'][2][2],
        thu30=text['thu']['state'][3][0],
        thu31=text['thu']['state'][3][1],
        thu32=text['thu']['state'][3][2],
        thu40=text['thu']['state'][4][0],
        thu41=text['thu']['state'][4][1],
        thu42=text['thu']['state'][4][2],
        thu50=text['thu']['state'][5][0],
        thu51=text['thu']['state'][5][1],
        thu52=text['thu']['state'][5][2],
        thu60=text['thu']['state'][6][0],
        thu61=text['thu']['state'][6][1],
        thu62=text['thu']['state'][6][2],

        f_1=figures['1'],
        f_2=figures['2'],
        f_3=figures['3'],
        f_4=figures['4'],
        f_5=figures['5'],
        f_6=figures['6'],
        f_7=figures['7'],
        f_8=figures['8'],
        f_9=figures['9'],
        f_10=figures['10'],
        f_11=figures['11'],
        f_12=figures['12'],
        f_13=figures['13'],

        f_station_loc=figures['station_loc'],
        f_EW=figures['EW'],
        f_NS=figures['NS'],
        f_UD=figures['UD'],
        f_spectrum=figures['spectrum'],
        f_single_frame=figures['single_frame'],
        f_single_3frame=figures['single_3frame'],
        f_single_shanghai=figures['single_shanghai'],
        f_single_z15=figures['single_z15'],
        f_single_4frm=figures['single_4frm'],
        f_city=figures['city'],
        f_town=figures['town'],
        f_country=figures['country'],
        f_thu=figures['thu'],
        f_distribution=figures['distribution'],
    )

    # print(report)
    return report

# debug
# if __name__ == '__main__':
#     with open('template.md', 'r', encoding='utf-8') as f:
#         template = f.read()
#     deal_text(template)
