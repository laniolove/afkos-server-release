from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class TypeTowerAssets:
    prefix_path = "tasks/afkos/assets/typetower/"
    I_MOVE_L = RecogImage(name="切换左边作业", roi_area=[0, 598, 131, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_left_0.png"])
    I_MOVE_R = RecogImage(name="切换右边作业", roi_area=[574, 598, 146, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    T_FIRST_FLAG = RecogText(keywords=["选择目的地"], roi_area=(237.0, 255.0, 239.0, 142.0))
    T_TOWER_1 = RecogText(keywords=["出发"], roi_area=(512.0, 418.0, 186.0, 151.0), exact_name="耀光塔")
    T_TOWER_1_MAX = RecogText(keywords=["最高层"], roi_area=(12.0, 374.0, 307.0, 133.0), exact_name="耀光塔最高层")
    T_TOWER_2 = RecogText(keywords=["出发"], roi_area=(500.0, 603.0, 186.0, 154.0), exact_name="绿意塔")
    T_TOWER_2_MAX = RecogText(keywords=["最高层"], roi_area=(0, 559.0, 307.0, 136.0), exact_name="绿意塔最高层")
    T_TOWER_3 = RecogText(keywords=["出发"], roi_area=(512.0, 969.0, 185.0, 149.0), exact_name="蛮血塔")
    T_TOWER_3_MAX = RecogText(keywords=["最高层"], roi_area=(12.0, 925.0, 306.0, 131.0), exact_name="蛮血塔最高层")
    T_TOWER_4 = RecogText(keywords=["出发"], roi_area=(512.0, 786.0, 185.0, 149.0), exact_name="亡灵塔")
    T_TOWER_4_MAX = RecogText(keywords=["最高层"], roi_area=(12.0, 742.0, 306.0, 131.0), exact_name="亡灵塔最高层")
    T_TOWER_BTL = RecogText(keywords=["挑战！"], roi_type="A")
    T_JOB_ENTER = RecogText(keywords=["通关"], roi_area=[123.0, 1169.0, 151.0, 100.0])
    T_BTL_START = RecogText(keywords=["战斗", "战牛"], roi_area=[500.0, 1111.0, 195.0, 167.0])
    T_USE_JOB = RecogText(keywords=["一键采用"], roi_area=[302.0, 986.0, 250.0, 159.0])
    T_NOT_HAVE = RecogText(keywords=["未拥有"], roi_type="D")
    T_CANCEL_HAVE = RecogText(keywords=["取消"], roi_area=(143.0, 760.0, 184.0, 154.0))
    # T_UNLOCK_WORD = RecogText(keywords=["新词条解锁"], roi_area=[181.0, 984.0, 332.0, 138.0])
    T_CLOSE_WORD = RecogText(keywords=["关闭"], roi_area=[275.0, 1124.0, 171.0, 147.0])
    T_EXT_NOT_HAVE = RecogText(keywords=["未拥有"], roi_area=(264.0, 549.0, 182.0, 143.0))
    T_OP_FLAG_BTL = RecogText(keywords=["手动战斗"], roi_area=(36.0, 927.0, 211.0, 140.0))
    T_SUCCESS = RecogText(keywords=["天赋挑战", "挑战", "下一关"], black_list=["再次挑战", "自动挑战", "动挑战"], roi_area=[0, 640, 720, 640])
    T_FAIL = RecogText(keywords=["再次挑战"], black_list=["天赋挑战", "挑战", "自动挑战", "动挑战"], roi_area=[391.0, 1155.0, 216.0, 118.0])
    T_TOWER_TITLE = RecogText(keywords=["塔"], roi_area=[203.0, 0, 328.0, 114.0])
    T_MAX_TOWER = RecogText(keywords=["最高层数"], roi_area=(345.0, 1119.0, 312.0, 153.0))
    T_OVER_TOWER = RecogText(keywords=["已通关"], roi_area=(0, 0, 720, 1280))
