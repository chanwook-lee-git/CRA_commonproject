WEDNESDAY_IDX = 2
SATURDAY_IDX = 5
SUNDAY_IDX = 6

name_id_dic = {}
id_cnt = 0
attn_by_dates = [[0] * 8 for _ in range(100)]
points = [0] * 100
grade = [''] * 100
names = [''] * 100


def get_id_by_name(name):
    global id_cnt

    if name not in name_id_dic:
        id_cnt += 1
        name_id_dic[name] = id_cnt
        names[id_cnt] = name

    return name_id_dic[name]

def calc_weekid_and_point(wk):
    week_point_id_dic = {
        "monday": (0, 1),
        "tuesday": (1, 1),
        "wednesday": (2, 3),
        "thursday": (3, 1),
        "friday": (4, 1),
        "saturday": (5, 2),
        "sunday": (6, 2),
    }

    return week_point_id_dic[wk][0], week_point_id_dic[wk][1]

def add_attn_cnt_and_point(name, wk):
    id = get_id_by_name(name)
    week_id, add_point = calc_weekid_and_point(wk)

    attn_by_dates[id][week_id] += 1
    points[id] += add_point

def update_bonus_point(id):
    ATTN_CNT  = 9
    if attn_by_dates[id][WEDNESDAY_IDX] > ATTN_CNT:
        points[id] += 10
    if attn_by_dates[id][SATURDAY_IDX] + attn_by_dates[id][SUNDAY_IDX] > ATTN_CNT:
        points[id] += 10

def update_grade(id):
    if points[id] >= 50:
        grade[id] = "GOLD"
    elif points[id] >= 30:
        grade[id] = "SILVER"
    else:
        grade[id] = "NORMAL"


def input_file():
    try:
        with open("../attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    add_attn_cnt_and_point(parts[0], parts[1])

        for id in range(1, id_cnt + 1):
            update_bonus_point(id)
            update_grade(id)
            print(f"NAME : {names[id]}, POINT : {points[id]}, GRADE : {grade[id]}")

        print("\nRemoved player")
        print("==============")
        for id in range(1, id_cnt + 1):
            if grade[id] != "NORMAL": continue
            if attn_by_dates[id][WEDNESDAY_IDX] + attn_by_dates[id][SATURDAY_IDX] + attn_by_dates[id][SUNDAY_IDX] > 0: continue
            print(names[id])

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    input_file()