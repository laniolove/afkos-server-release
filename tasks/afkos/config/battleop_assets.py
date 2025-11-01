from re import T
from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class BattleOpAssets:
    prefix_path = "tasks/afkos/assets/battleop/"
    I_OPEN_SETTING = RecogImage(name="I_OPEN_SETTING", roi_area=(646, 614, 68, 66), threshold=0.75, prefix_path=prefix_path, files=["I_OPEN_SETTING.png"])
    I_CLOSE_SETTING = RecogImage(name="I_CLOSE_SETTING", roi_area=(646, 614, 68, 66), threshold=0.75, prefix_path=prefix_path, files=["I_CLOSE_SETTING.png"])
    I_DEBUS_TROOPS = RecogImage(name="I_DEBUS_TROOPS", roi_area=(636, 444, 78, 234), threshold=0.75, prefix_path=prefix_path, files=["I_DEBUS_TROOPS.png"])
    T_JUMP_BTL_BTN = RecogText(keywords=["跳过战斗"], roi_area=(150, 1144, 250, 94))
    T_NEED_HERO_FLAG = RecogText(keywords=["上阵至少"], roi_area=(456, 1152, 230, 86))
    T_FULL_HERO_FLAG = RecogText(keywords=["本场战斗"], roi_area=(456, 1152, 230, 86))

    T_TODAY_COST = RecogText(keywords=["今日可消"], roi_area=(156, 648, 244, 116))
    T_NEED_HERO_FLAG_0 = RecogText(keywords=["上阵至少"], roi_area=(270, 1146, 430, 90))
    T_FULL_HERO_FLAG_0 = RecogText(keywords=["本场战斗"], roi_area=(270, 1146, 430, 90))

    T_JUMP_BTLING = RecogText(keywords=["跳过"], roi_area=(484, 942, 230, 132))

    T_SUCCESS = RecogText(keywords=["点击空白处", "白处继续"], roi_area=[221.0, 1108.0, 279.0, 143.0])
    AREA_CUR_COST_POWER = (456, 1152, 230, 86)
    AREAS_HEROS = [
        (14, 778, 112, 148),
        (124, 778, 112, 146),
        (238, 776, 112, 148),
        (358, 778, 106, 148),
        (472, 778, 106, 148),
        (580, 774, 108, 154),
        (14, 966, 104, 152),
        (130, 962, 108, 156),
        (238, 964, 114, 152),
    ]
