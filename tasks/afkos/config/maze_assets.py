from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class MazeAssets:
    prefix_path = "tasks/afkos/assets/maze/"
    I_SEL_BATTLE = RecogImage(name="战斗选择", roi_type="D", threshold=0.75, prefix_path=prefix_path, files=["battle_img_0.png"])
    I_SEL_SHOP = RecogImage(name="商店选择", roi_type="D", threshold=0.75, prefix_path=prefix_path, files=["shop_jiemian_0.png"])
    I_RETRY_BATTLE = RecogImage(name="战斗重试", roi_area=(572, 1107, 148, 168), threshold=0.75, prefix_path=prefix_path, files=["retry_battle.png"])
    I_DIFF_LEFT = RecogImage(name="I_DIFF_LEFT", roi_area=(214, 452, 150, 154), prefix_path=prefix_path, files=["maze_left.png"])
    I_DIFF_RIGHT = RecogImage(name="I_DIFF_RIGHT", roi_area=(354, 449, 152, 154), prefix_path=prefix_path, files=["maze_right.png"])
    # I_DIFF_11 = RecogImage(name="maze_problem_11", match_mode="sift", roi_area=(275, 437, 170, 170), prefix_path=prefix_path, files=["maze_problem_11.png"])
    T_MAZE_START = RecogText(keywords=["进入"], roi_area=[326.0, 1113.0, 193.0, 165.0])
    T_BTL_START = RecogText(keywords=["战斗", "战牛"], roi_area=[325.0, 1110.0, 194.0, 169.0])
    T_SEL_LUOYIN = RecogText(keywords=["选择烙印"], roi_area=[232.0, 1114.0, 254.0, 159.0])
    T_LUOYIN_0 = RecogText(keywords=["史诗"], roi_type="L")
    T_LUOYIN_1 = RecogText(keywords=["精英"], roi_type="L")
    T_LUOYIN_2 = RecogText(keywords=["稀有"], roi_type="L")
    T_LUOYIN_OK = RecogText(keywords=["确认"], roi_area=[262.0, 1111.0, 192.0, 166.0])
    T_AGAIN_GO = RecogText(keywords=["继续前进"], roi_area=[4.0, 1118.0, 254.0, 156.0])
    T_BTL_PLUS_TIPS = RecogText(keywords=["附加挑战"], roi_type="U")
    T_OVER = RecogText(keywords=["结束探索"], roi_area=[57.0, 1115.0, 253.0, 156.0])
    T_RUN_FLAG = RecogText(keywords=["结束探索"], roi_area=[561.0, 1169.0, 159.0, 111.0])
    T_Failing = RecogText(keywords=["上阵英雄"], roi_area=(222.0, 517.0, 272.0, 145.0))
    T_LONG_OVER = RecogText(keywords=["长按结束"], roi_area=(115.0, 723.0, 241.0, 151.0))
    T_DIFF_RAND = RecogText(keywords=["难度"], roi_area=(272.0, 0, 177.0, 89.0))
    # T_AREA_DIFF_RAND = RecogText(keywords=["难度"], roi_area=(317, 490, 80, 70))
    AREA_T_DIFF = (317, 490, 80, 70)
