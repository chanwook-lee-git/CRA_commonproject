from mission2.policy.week_policy import get_week_id_list, get_week_id

def get_point(attn_list):
    point = 0
    point += get_attn_point(attn_list)
    point += get_bonus_point(attn_list)

    return point

def get_attn_point(attn_list):
    attn_point = 0
    for id_point in get_week_id_list():
        week_id = id_point[0]
        point_rate = id_point[1]
        attn_point += attn_list[week_id] * point_rate

    return attn_point

def get_bonus_point(attn_list):
    bonus_point = 0
    if attn_list[get_week_id("wednesday")] > 9:
        bonus_point += 10

    if attn_list[get_week_id("saturday")] + attn_list[get_week_id("sunday")] > 9:
        bonus_point += 10

    return bonus_point