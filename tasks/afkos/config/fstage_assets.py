from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class FStageAssets:
    prefix_path = "tasks/afkos/assets/fstage/"
    I_FRIEND_ENTER = RecogImage(name="进入好友", roi_type="L", threshold=0.75, prefix_path=prefix_path, files=["friend_enter.png"])
    I_MOVE_L = RecogImage(name="切换左边作业", roi_area=[0, 598, 131, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_left_0.png"])
    I_MOVE_R = RecogImage(name="切换右边作业", roi_area=[574, 598, 146, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    T_HELP_IT = RecogText(keywords=["前往帮助"], roi_area=[114.0, 892.0, 220.0, 144.0])
    T_TALENT_STAGE = RecogText(keywords=["天赋挑战", "幻灵挑战"], roi_area=[54.0, 943.0, 255.0, 159.0])
    T_NORMAL_STAGE = RecogText(keywords=["挑战"], roi_area=[431.0, 945.0, 195.0, 162.0])
    T_ONE_STAGE = RecogText(keywords=["挑战"], roi_area=(262.0, 978.0, 195.0, 161.0))
    T_JOB_ENTER = RecogText(keywords=["通关"], roi_area=[123.0, 1169.0, 151.0, 100.0])
    T_BTL_START = RecogText(keywords=["战斗", "战牛"], roi_area=[387.0, 1110.0, 195.0, 168.0])
    T_USE_JOB = RecogText(keywords=["一键采用"], roi_area=[302.0, 986.0, 250.0, 159.0])
    T_TALENT_TITLE = RecogText(keywords=["赛季天赋关卡"], roi_area=[204.0, 0, 328.0, 114.0])
    T_NORMAL_TITLE = RecogText(keywords=["赛季挂机关卡"], roi_area=[203.0, 0, 328.0, 114.0])
    T_NOT_HAVE = RecogText(keywords=["未拥有"], roi_area=[0, 640, 720, 640])
    T_SUCCESS = RecogText(keywords=["下一关", "继续挑战"], roi_area=[390.0, 1115.0, 222.0, 162.0])
    T_FAIL = RecogText(keywords=["再次挑战"], roi_area=[371.0, 1135.0, 256.0, 145.0])
    T_STAGE_SYMBOL = RecogText(keywords=["敌方阵容"], roi_area=[0, 733.0, 179.0, 141.0])
    T_FRIEND_VIEW = RecogText(keywords=["收礼进度"], roi_area=(45.0, 68.0, 283.0, 144.0))
    T_OP_FLAG_BTL = RecogText(keywords=["手动战斗"], roi_area=(36.0, 927.0, 211.0, 140.0))
    T_XiGua = RecogText(keywords=["工匠"], roi_area=[0, 0, 720, 1280])
