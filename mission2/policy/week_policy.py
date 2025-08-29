week_id_point_dic = {
    "monday": (0, 1),
    "tuesday": (1, 1),
    "wednesday": (2, 3),
    "thursday": (3, 1),
    "friday": (4, 1),
    "saturday": (5, 2),
    "sunday": (6, 2),
}

def get_week_id(wk):
    return week_id_point_dic[wk][0]

def get_week_id_list():
    return week_id_point_dic.values()
