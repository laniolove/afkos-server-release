from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class MStageAssets:
    prefix_path = "tasks/afkos/assets/mstage/"
    I_MOVE_L = RecogImage(name="切换左边作业", roi_area=[0, 598, 131, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_left_0.png"])
    I_MOVE_R = RecogImage(name="切换右边作业", roi_area=[574, 598, 146, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    I_NEW_WORD_R = RecogImage(name="新词条切换右边", roi_type="R", threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    # I_JOB_ROLE_LIST = RecogImage(
    #     name="I_JOB_ROLE_LIST", roi_area=[0, 0, 720, 1280], match_mode="sift", threshold=0.75, prefix_path=prefix_path, files=["I_JOB_ROLE_LIST.png"]
    # )
    T_JOB_ENTER = RecogText(keywords=["通关"], roi_area=[123.0, 1169.0, 151.0, 100.0])
    T_SUCCESS = RecogText(
        keywords=["天赋挑战", "挑战", "下一关", "多队挑战", "幻灵挑战", "下一"], black_list=["再次挑战", "自动挑战", "动挑战"], roi_area=[0, 640, 720, 640]
    )
    T_OBTAIN_REWARD = RecogText(keywords=["收获奖励"], roi_area=[243.0, 650.0, 233.0, 132.0])
    T_FAIL = RecogText(keywords=["再次挑战"], black_list=["天赋挑战", "挑战", "自动挑战", "动挑战"], roi_area=[391.0, 1155.0, 216.0, 118.0])
    T_TALENT_STAGE = RecogText(
        keywords=["幻灵挑战", "天赋挑战", "多队挑战"], black_list=["再次挑战", "自动挑战", "动挑战"], roi_area=[96.0, 1008.0, 215.0, 116.0]
    )
    T_NORMAL_STAGE = RecogText(keywords=["挑战"], black_list=["再次挑战", "自动挑战", "动挑战", "多队挑战"], roi_area=[453.0, 1009.0, 155.0, 122.0])
    T_BTL_START = RecogText(keywords=["战斗", "战牛"], roi_area=[500.0, 1111.0, 195.0, 167.0])
    T_USE_JOB = RecogText(keywords=["一键采用"], roi_area=[302.0, 986.0, 250.0, 159.0])
    T_TALENT_TITLE = RecogText(keywords=["赛季天赋关卡"], roi_area=[204.0, 0, 328.0, 114.0])
    T_NORMAL_TITLE = RecogText(keywords=["赛季挂机关卡"], roi_area=[203.0, 0, 328.0, 114.0])
    T_NOT_HAVE = RecogText(keywords=["未拥有"], roi_type="D")
    T_LIMIT_PROGRESS = RecogText(keywords=["本日极限进度"], roi_type="D")
    T_CANCEL_HAVE = RecogText(keywords=["取消"], roi_area=(143.0, 760.0, 184.0, 154.0))
    T_UNLOCK_WORD = RecogText(keywords=["新词条解锁"], roi_area=[181.0, 984.0, 332.0, 138.0])
    T_CLOSE_WORD = RecogText(keywords=["关闭"], roi_area=[275.0, 1124.0, 171.0, 147.0])
    T_EXT_NOT_HAVE = RecogText(keywords=["未拥有"], roi_area=(264.0, 549.0, 182.0, 143.0))
    T_OP_FLAG_BTL = RecogText(keywords=["手动战斗"], roi_area=(36.0, 927.0, 211.0, 140.0))
    T_ONE_STAGE = RecogText(keywords=["挑战"], roi_area=(262.0, 978.0, 195.0, 161.0))
    AREA_RANK = (222, 860, 78, 108)
    AREA_TEXT_STAGE_TITLE = (170, 6, 370, 72)
