week_id_point_dic = {
    "monday": (0, 1),
    "tuesday": (1, 1),
    "wednesday": (2, 3),
    "thursday": (3, 1),
    "friday": (4, 1),
    "saturday": (5, 2),
    "sunday": (6, 2),
}

MON_ID = week_id_point_dic["monday"][0]
TUE_ID = week_id_point_dic["tuesday"][0]
WED_ID = week_id_point_dic["wednesday"][0]
THU_ID = week_id_point_dic["thursday"][0]
FRI_ID = week_id_point_dic["friday"][0]
SAT_ID = week_id_point_dic["saturday"][0]
SUN_ID = week_id_point_dic["sunday"][0]

def get_week_id(wk):
    try:
        return week_id_point_dic[wk][0]
    except:
        return 7

def get_week_id_list():
    return week_id_point_dic.values()


