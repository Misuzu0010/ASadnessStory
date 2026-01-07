label chapter_01:
    scene bg046_000 at t_stand_base_bg
    "大家好啊这里是神秘制作人"
    "怎么说呢，这是我实在是闲的蛋疼做的一个小游戏"
    "希望大家能够看得开心。"
    show chr_nana at t_stand_base_bg_character, pos_left_mid with dissolve
    show chr_daya at t_stand_base_bg_character, pos_right_mid with dissolve

    e "えっと、あけましておめでとうございます！！"
    e "私はこのガルゲームのヒロイン 月沐です~"
    
    e "よろしくお願いいたします"
    "我静静地看着月沐，脑海里浮现出一些不好的东西。"
    menu:
        "回忆第一段恋情":
            call chapter_01_choice_1
        "什么也不做":
            "真的什么也不想做吗"
            menu:
                "侵犯":
                    pass
                "摸摸头":
                    pass
                "杀害":
                    pass
                    
    return