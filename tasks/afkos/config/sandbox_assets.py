from re import T
from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class SandboxAssets:
    prefix_path = "tasks/afkos/assets/sandbox/"
    I_BUFF_SEL = RecogImage(name="I_BUFF_SEL", roi_type="D", threshold=0.7, prefix_path=prefix_path, files=["I_BUFF_SEL.png"])

    T_FLAG = RecogText(keywords=["战利品"], roi_area=(494, 1102, 160, 66))
    T_SEL = RecogText(keywords=["领取"], roi_area=(366, 1140, 344, 116))
    T_BTL = RecogText(keywords=["快速战斗"], roi_area=(366, 1140, 344, 116))
    T_NEED_SEL_FLAG = RecogText(keywords=["选择"], roi_area=(272, 1142, 432, 102))
    T_OK_SEL_BTN = RecogText(keywords=["确认"], roi_area=(272, 1142, 432, 102))
    T_POWER_FLAG = RecogText(keywords=["今日可"], roi_area=(162, 1154, 204, 94))
    T_BUFF_PAGE_FLAG = RecogText(keywords=["本轮增益"], roi_area=(4, 376, 328, 154))
    T_BUFF_SEL_PAGE_FLAG = RecogText(keywords=["请选择"], roi_area=(4, 440, 108, 52))
    T_TRANSIT_PAGE = RecogText(keywords=["历史"], roi_area=(140, 1160, 106, 92), exact_name="战斗胜利过度界面")
    T_TRANSIT_0_PAGE = RecogText(keywords=["贡献"], roi_area=(484, 1138, 108, 128), exact_name="战斗胜利过度界面")
    AREA_POWER_COUNT = (202, 1186, 110, 60)  # 4545,去掉/,去前两位，就是真实体力
    CLICK_AREA_SEL_BUFF = (38, 518, 648, 162)
