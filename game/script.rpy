# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("月沐")

label start:

    call chapter_01
    e "真是一场酣畅淋漓的对话啊"
    return
