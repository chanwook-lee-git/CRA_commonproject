# python -m pytest -q tests/test_attendance_m2.py --cov=mission2 --cov-report=html

import os, sys, io, builtins
from mission2.policy.week_policy import get_week_id, get_week_id_list, MON_ID, TUE_ID, WED_ID, THU_ID, FRI_ID, SAT_ID, SUN_ID
from mission2.policy.point_policy import get_point, get_attn_point, get_bonus_point
from mission2.policy.grade_policy import get_grade
from mission2.policy.removed_policy import is_removed
from mission2.player import player
from mission2.player_factory import player_factory
import mission2.attendance_m2 as app

# 프로젝트 루트를 sys.path에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# grade_policy 검증
def test_grade_policy_get_grade():
    # 입력한 point에 따라, 알맞은 grade를 반환하는지 검증
    assert get_grade(0) == "NORMAL"
    assert get_grade(29) == "NORMAL"
    assert get_grade(30) == "SILVER"
    assert get_grade(49) == "SILVER"
    assert get_grade(50) == "GOLD"
    assert get_grade(4315532) == "GOLD"


# point_policy 검증
def _blank_attn():
    return [0]*7

def test_point_policy_attn_point():
    # 각 요일별로 출석 횟수를 증가시키며, point rate에 따라 결과가 일치하는지 검증
    attn = _blank_attn()
    attn[MON_ID] = 3
    assert get_attn_point(attn) == 3
    attn[TUE_ID] = 1
    assert get_attn_point(attn) == 4
    attn[WED_ID] = 2
    assert get_attn_point(attn) == 10
    attn[THU_ID] = 0
    assert get_attn_point(attn) == 10
    attn[FRI_ID] = 5
    assert get_attn_point(attn) == 15
    attn[SAT_ID] = 9
    assert get_attn_point(attn) == 33
    attn[SUN_ID] = 3
    assert get_attn_point(attn) == 39

def test_point_policy_wed_bonus_point():
    # 수요일과 주말 출석일수에 따라서 bonus point가 합산 되는지 검증
    attn = _blank_attn()
    attn[WED_ID] = 10
    assert get_bonus_point(attn) == 10
    assert get_point(attn) == 40
    attn[SAT_ID] = 5
    assert get_bonus_point(attn) == 10
    assert get_point(attn) == 50
    attn[SUN_ID] = 5
    assert get_bonus_point(attn) == 20
    assert get_point(attn) == 70


# remove_policy 검증
def test_removed_policy_true_and_false():
    # 등급과 수요일 및 주말 출석에 따라 탈락 후보에 선정 되는지 검증
    attn = _blank_attn()
    assert is_removed('NORMAL', attn) == True
    attn[MON_ID] = 1
    assert is_removed('NORMAL', attn) == True
    assert is_removed('SILVER', attn) == False
    assert is_removed('GOLD', attn) == False
    attn[WED_ID] = 1
    assert is_removed('NORMAL', attn) == False
    attn = _blank_attn()
    attn[SAT_ID] = 1
    assert is_removed('NORMAL', attn) == False
    attn = _blank_attn()
    attn[SUN_ID] = 1
    assert is_removed('NORMAL', attn) == False


# week_policy 검증
def test_week_policy_get_week_id():
    # 요일에 따라 알맞은 index를 반환하는지 검증
    assert get_week_id("monday") == 0
    assert get_week_id("tuesday") == 1
    assert get_week_id("wednesday") == 2
    assert get_week_id("thursday") == 3
    assert get_week_id("friday") == 4
    assert get_week_id("saturday") == 5
    assert get_week_id("sunday") == 6

def test_week_policy_get_week_id_list():
    # get_week_id_list 함수 실행 시, 예상된 결과를 반환하는지 검증
    vals = list(get_week_id_list())
    assert len(vals) == 7
    assert vals == [(0, 1), (1, 1), (2, 3), (3, 1), (4, 1), (5, 2), (6, 2)]

def test_week_policy_invalid_raises_7():
    # week 값에, invalid data가 입력 할 경우, 7을 반환하는지 검증
    assert get_week_id("NoDay") == 7


# player 검증
def test_player_point_grade_and_removed():
    # player class 생성 후 attn 값을 입력 했을 때, 각 속성별로 예상된 결과를 반환하는지 검증
    p = player("P", 1)
    for _ in range(10): p.add_attn("wednesday")
    for _ in range(6):  p.add_attn("saturday")
    for _ in range(4):  p.add_attn("sunday")
    for _ in range(3):  p.add_attn("monday")

    p.calc_point()
    p.calc_grade()
    assert p.get_name() == "P"
    assert p.get_id() == 1
    assert p.get_point() == 73
    assert p.get_grade() == "GOLD"
    assert p.isRemoved() is False


# player_factory 검증
def test_player_factory_create_and_reuse():
    # factory 및 dic을 활용하여 player 생성 시, 이름에 따른 player class가 정상적으로 생성되는지 검증
    fac = player_factory()
    registry = {}
    a1 = fac.create("Alice", registry)
    a2 = fac.create("Alice", registry)
    b  = fac.create("Bob", registry)
    assert a1 is a2
    assert a1 is not b
    assert set(registry.keys()) == {"Alice", "Bob"}



# attendance_m2 검증
def test_attendance_m2_file_not_found(monkeypatch, capsys):
    # 파일 오픈 실패 시, '파일을 찾을 수 없습니다.' 호출 여부 검증
    app.input_file()
    out = capsys.readouterr().out
    assert "파일을 찾을 수 없습니다." in out

def test_attendance_m2_integration_happy_path(monkeypatch, capsys):
    # sample data로, 정상적인 결과를 printing 하는지 검증
    sample = "\n".join([
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P wednesday",
        "P saturday",
        "P sunday",
        "Jack monday"
    ])
    fake_path = "../attendance_weekday_500.txt"

    real_open = builtins.open
    def fake_open(path, *args, **kwargs):
        if path == fake_path:
            return io.StringIO(sample)
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", fake_open)
    app.name_player_dic.clear()

    app.input_file()
    out = capsys.readouterr().out

    assert "NAME : P, POINT : 44, GRADE : SILVER" in out
    assert "NAME : Jack, POINT : 1, GRADE : NORMAL" in out
    assert "\nRemoved player\n==============\n" in out
    assert "Jack" in out


