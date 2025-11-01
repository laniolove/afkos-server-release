from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage

# I_TASK_SEL = RecogImage(
#     name="I_TASK_SEL",
#     match_mode="sift",
#     roi_type="A",
#     sift_goods=20,
#     prefix_path=prefix_path,
#     files=["I_TASK_SEL.png"],
# )
# I_TASK_LONG_CLICK = RecogImage(name="I_TASK_LONG_CLICK", roi_type="A", threshold=0.75, prefix_path=prefix_path, files=["I_TASK_LONG_CLICK.png"])
# T_TASK_AUTO_ROAD = RecogText(keywords=["追踪"], roi_type="A")


class MainAssets:
    prefix_path = "tasks/afkos/assets/main/"
    I_TASKICON = RecogImage(
        name="任务图标", roi_area=(496, 8, 218, 292), threshold=0.75, prefix_path=prefix_path, files=["task_icon.png", "task_icon_0.png", "main_sun.png"]
    )
    I_BACKBUTTON = RecogImage(
        name="返回图标", roi_area=[0, 1105, 165, 168], threshold=0.57, prefix_path=prefix_path, files=["back_button_0.png", "back_button_1.png"]
    )
    I_GOU_OK = RecogImage(name="提示选择✓", roi_type="D", threshold=0.75, prefix_path=prefix_path, files=["tips_gou.png"])
    I_IS_GOU = RecogImage(name="提示✓", roi_type="LU", threshold=0.75, prefix_path=prefix_path, files=["I_IS_GOU.png"])
    I_CHA_CANCEL = RecogImage(name="提示选择x", roi_type="D", threshold=0.75, prefix_path=prefix_path, files=["tips_x.png"])
    I_SETTING = RecogImage(name="设置进入", roi_area=[575, 1146, 145, 134], threshold=0.75, prefix_path=prefix_path, files=["set_enter.png"])
    T_HANGUP = RecogText(keywords=["当前进度", "托管", "无尽", "先锋", "关卡"], roi_area=[4.0, 1188.0, 154.0, 92.0])
    # I_HOME_FLAG = RecogImage(name="I_HOME_FLAG", roi_type="RU", match_mode="sift", threshold=0.75, prefix_path=prefix_path, files=["I_HOME_FLAG.png"])
    T_BG_HANGUP = RecogText(keywords=["托管中"], roi_area=[4.0, 1188.0, 154.0, 92.0])
    T_BG_HANGUP_END = RecogText(keywords=["结束"], roi_area=[4.0, 1188.0, 154.0, 92.0])
    T_WANFA = RecogText(keywords=["玩法目录", "目录"], roi_area=[209.0, 1191.0, 201.0, 89.0])
    T_HERO = RecogText(keywords=["英雄厅堂"], roi_area=(311.0, 1191.0, 199.0, 89.0))
    T_LOADING = RecogText(keywords=["加载中"], roi_area=[0, 960, 720, 320])
    T_CLOSE_0 = RecogText(keywords=["点击空白处", "白处继续"], roi_area=[221.0, 1108.0, 279.0, 143.0])
    T_CLOSE_1 = RecogText(keywords=["点击屏幕退出"], roi_area=[194.0, 1138.0, 296.0, 142.0])
    T_CLOSE_2 = RecogText(keywords=["点击屏幕恢复"], roi_area=[194.0, 1138.0, 296.0, 142.0])
    T_CLOSE_3 = RecogText(keywords=["点击屏幕跳过"], roi_area=(233.0, 1132.0, 261.0, 146.0))
    T_REMIND_GOU = RecogText(keywords=["不再提醒"], roi_type="LU", offset_area=[-35, -6, 30, 30])
    T_Battling = RecogText(keywords=["秒"], roi_area=(561.0, 0, 159.0, 129.0))
    T_GAME_ENTER = RecogText(keywords=["点击开始游戏"], roi_area=(194.0, 978.0, 333.0, 160.0))
    T_ARENA_ENTER = RecogText(keywords=["竞技场"], roi_type="A")
    T_MAZE_ENTER = RecogText(keywords=["异界迷宫"], roi_type="A")
    T_TOWER_ENTER = RecogText(keywords=["天穹试炼", "天空试炼", "天空", "天穹"], roi_type="A")
    T_GOD_ENTER = RecogText(keywords=["女神", "女神试炼", "女"], roi_type="A")
    T_SANDBOX_ENTER = RecogText(keywords=["沙盘", "演兵", "沙盘演兵"], roi_type="A")
    T_WAIT_OPEN = RecogText(keywords=["即将开放"], roi_type="A")
    T_HOME_FLAG = RecogText(keywords=["世界", "离开"], roi_area=(404, 2, 344, 320))
    T_WORLD_FLAG = RecogText(keywords=["家园"], roi_area=(370, 4, 342, 320))
