from mission2.player import player

class player_factory:
    def create(self, name:str, name_player_dic) -> player:
        return self.get_or_create(name, name_player_dic)

    def get_or_create(self, name:str, name_player_dic) -> player:
        if name in name_player_dic:
            return name_player_dic[name]
        else:
            p = player(name, len(name_player_dic) + 1)
            name_player_dic[name] = p
            return p
