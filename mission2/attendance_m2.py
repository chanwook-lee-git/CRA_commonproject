from mission2.player_factory import player_factory

name_player_dic = {}

def input_file():
    fc = player_factory()
    try:
        with open("../attendance_weekday_500.txt", encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    name, week = parts[0], parts[1]
                    p = fc.create(name, name_player_dic)
                    p.add_attn(week)

        for player in name_player_dic.values():
            player.calc_point()
            player.calc_grade()
            print(f"NAME : {player.get_name()}, POINT : {player.get_point()}, GRADE : {player.get_grade()}")

        print("\nRemoved player")
        print("==============")
        for player in name_player_dic.values():
            if player.isRemoved():
                print(player.get_name())

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

if __name__ == "__main__":
    input_file()