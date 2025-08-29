from mission2.player import player

class player_factory:
    def create(self, name, name_player_dic) -> player:
        p = self.get_or_create(name, name_player_dic)
        return p

    def get_or_create(self, name, name_player_dic):
        if name in name_player_dic:
            return name_player_dic[name]
        else:
            p = player(name)
            name_player_dic[name] = p
            return p
