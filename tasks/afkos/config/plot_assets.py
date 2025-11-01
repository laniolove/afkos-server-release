from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class PlotAssets:
    prefix_path = "tasks/afkos/assets/plot/"
    I_TASK_SEL_FLAG = RecogImage(
        name="I_TASK_SEL_FLAG",
        match_mode="sift",
        roi_area=(0, 846, 129, 170),
        sift_goods=2,
        prefix_path=prefix_path,
        files=[
            "I_TASK_SEL_FLAG_0.png",
            "I_TASK_SEL_FLAG_1.png",
            "I_TASK_SEL_FLAG_2.png",
            "I_TASK_SEL_FLAG_3.png",
            "I_TASK_SEL_FLAG_4.png",
            "I_TASK_SEL_FLAG_5.png",
        ],
    )
    I_MAJOR_TASK_SEL = RecogImage(
        name="命运路线选择",
        match_mode="sift",
        roi_area=(0, 846, 129, 170),
        sift_goods=15,
        prefix_path=prefix_path,
        files=["I_MAJOR_TASK_SEL.png"],
    )

    I_TASK_LONG_CLICK = RecogImage(
        name="I_TASK_LONG_CLICK", roi_area=(275, 723, 176, 188), threshold=0.75, prefix_path=prefix_path, files=["I_TASK_LONG_CLICK.png"]
    )
    I_TASK_GET_FLAG = RecogImage(
        name="I_TASK_GET_FLAG",
        match_mode="sift",
        roi_type="R",
        sift_goods=14,
        prefix_path=prefix_path,
        files=["I_TASK_GET_FLAG.png"],
    )
    I_TASK_SEL = RecogImage(name="I_TASK_SEL", roi_area=(0, 597, 143, 138), threshold=0.75, prefix_path=prefix_path, files=["I_TASK_SEL.png"])
    I_TASK_DRIVE_GAME_2 = RecogImage(name="I_TASK_DRIVE", roi_area=(0, 921, 132, 174), threshold=0.75, prefix_path=prefix_path, files=["I_TASK_DRIVE.png"])
    I_TASK_BATTLE_BTN = RecogImage(
        name="I_TASK_BATTLE_BTN",
        roi_area=(264, 734, 186, 176),
        threshold=0.75,
        prefix_path=prefix_path,
        files=["I_TASK_BATTLE_BTN.png", "I_TASK_BATTLE_BTN_0.png"],
    )
    I_TASK_TYPE_FALG = RecogImage(
        name="I_TASK_TYPE_FALG",
        roi_area=(200, 200, 200, 200),
        threshold=0.75,
        prefix_path=prefix_path,
        files=["I_TASK_TYPE_FALG.png"],
    )
    I_TASK_RUN = RecogImage(name="I_TASK_RUN", roi_area=(300, 500, 300, 300), threshold=0.75, prefix_path=prefix_path, files=["I_TASK_RUN.png"])
    T_TASK_AUTO_ROAD = RecogText(keywords=["追踪"], roi_area=(440.0, 901.0, 158.0, 142.0))
    T_TASK_SKIP = RecogText(keywords=["跳过"], roi_area=(583.0, 1160.0, 137.0, 120.0))
    T_TASK_SKIP_FLAG = RecogText(keywords=["跳过"], roi_area=(172.0, 508.0, 388.0, 147.0))
    T_ADDR_FLY_FLAG = RecogText(keywords=["传送"], roi_area=(95.0, 554.0, 541.0, 149.0))
    T_TASK_LONG_CLICK = RecogText(keywords=["长按"], roi_area=(277.0, 660.0, 164.0, 146.0))
    T_TASK_GAME_0 = RecogText(keywords=["收纳挑战"], roi_area=(202.0, 66.0, 310.0, 172.0))
    T_TASK_GAME_1 = RecogText(keywords=["开始收集"], roi_area=(80.0, 19.0, 319.0, 172.0))
    T_TASK_GAME_2 = RecogText(keywords=["比赛", "暂停"], roi_area=(0, 1152.0, 165.0, 128.0))
    T_TASK_GAME_3 = RecogText(keywords=["雪球"], roi_area=(193.0, 99.0, 351.0, 141.0))
    T_TASK_BTL_START = RecogText(keywords=["战斗"], roi_area=(325.0, 1110.0, 194.0, 169.0))
    T_TASK_SWITCH_TIME = RecogText(keywords=["切换"], roi_area=(229.0, 930.0, 286.0, 156.0))
    T_TASK_TYPE = RecogText(keywords=["冬夜残响"], roi_type="D")
    T_TASK_0 = RecogText(keywords=["任务"], roi_area=(100.0, 1009.0, 235.0, 152.0))
    T_TASK_1 = RecogText(keywords=["声望"], roi_area=(458.0, 1015.0, 234.0, 151.0))
    T_TASK_GET = RecogText(keywords=["领取任务"], roi_type="A")
    T_TASK_REWARD = RecogText(keywords=["前往领奖"], roi_area=(237.0, 913.0, 245.0, 158.0))
    T_TASK_DOING = RecogText(keywords=["追踪中"], roi_type="RD")
    T_TASK_TYPE_FALG = RecogText(keywords=["白山亡", "白山公"], roi_area=(254.0, 236.0, 213.0, 146.0))
    AREA_T_DIFF = (317, 490, 80, 70)
