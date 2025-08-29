from mission2.policy.week_policy import get_week_id
from mission2.policy.point_policy import get_point
from mission2.policy.grade_policy import get_grade

class player():
    def __init__(self, name):
        self._name = name
        self._point = 0
        self._attn = [0,0,0,0,0,0,0]
        self._grade = 'NORMAL'

    def add_attn(self, wk):
        self._attn[get_week_id(wk)] += 1

    def calc_point(self):
        self._point = get_point(self._attn)

    def calc_grade(self):
        self._grade = get_grade(self._point)
        return self._grade

    def get_name(self):
        return self._name

    def get_point(self):
        return self._point

    def get_grade(self):
        return self._grade

    def isRemoved(self):
        if self._grade != "NORMAL" : return False
        if self._attn[get_week_id("wednesday")] + self._attn[get_week_id("saturday")] + self._attn[get_week_id("sunday")] > 0 : return False
        return True