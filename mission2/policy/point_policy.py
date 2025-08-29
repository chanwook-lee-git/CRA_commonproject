from mission2.policy.week_policy import get_week_id_list, get_week_id, WED_ID, SAT_ID, SUN_ID

def get_point(attn_list) -> int:
    return get_attn_point(attn_list) + get_bonus_point(attn_list)

def get_attn_point(attn_list) -> int:
    attn_point = 0
    for week_id_point in get_week_id_list():
        week_id = week_id_point[0]
        point_rate = week_id_point[1]
        attn_point += attn_list[week_id] * point_rate

    return attn_point

def get_bonus_point(attn_list) -> int:
    bonus_point = 0
    if attn_list[WED_ID] >= 10:
        bonus_point += 10

    if attn_list[SAT_ID] + attn_list[SUN_ID] >= 10:
        bonus_point += 10

    return bonus_point