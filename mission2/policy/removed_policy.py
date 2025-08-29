from mission2.policy.week_policy import WED_ID, SAT_ID, SUN_ID

def is_removed(grade, attn):
    if grade != "NORMAL": return False
    if attn[WED_ID] + attn[SAT_ID] + attn[SUN_ID] > 0: return False
    return True
