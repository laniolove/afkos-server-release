from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class BXZYAssets:
    prefix_path = "tasks/brush/assets/bxzy/"
    T_AGAIN_0_BTL = RecogText(keywords=["继续挑战"], roi_area=(235.0, 917.0, 250.0, 158.0))
    T_AGAIN_1_BTL = RecogText(keywords=["再次挑战"], roi_area=(243.0, 1157.0, 235.0, 123.0))
    T_AGAIN_2_BTL = RecogText(keywords=["继续"], roi_area=(268.0, 1155.0, 184.0, 125.0))
    T_START_0_BTL = RecogText(keywords=["战斗开始"], roi_area=(366.0, 1159.0, 230.0, 121.0))
    # T_START_1_BTL = RecogText(keywords=["战斗开始"], roi_area=(243.0, 1159.0, 235.0, 121.0))
    T_NEXT_0_LEVEL = RecogText(
        keywords=["下一关"],
        roi_area=(258.0, 1156.0, 208.0, 124.0),
    )
    # T_NEXT_1_LEVEL = RecogText(
    #     keywords=["下一关"],
    #     roi_area=(243.0, 1159.0, 235.0, 121.0),
    # )
    # T_JUMP = RecogText(keywords=["跳过"], roi_area=(579.0, 661.0, 141.0, 146.0))
    # T_OK = RecogText(keywords=["确定"], roi_area=(411.0, 731.0, 190.0, 162.0))
