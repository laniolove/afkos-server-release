from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class GodAssets:
    prefix_path = "tasks/afkos/assets/god/"
    I_SWEEP_SEL_MAX = RecogImage(name="I_SWEEP_SEL_MAX", roi_area=(38, 1024, 658, 84), threshold=0.7, prefix_path=prefix_path, files=["I_SWEEP_SEL_MAX.png"])
    I_FORCE_SWEEP = RecogImage(name="I_FORCE_SWEEP", roi_area=(0, 728, 688, 300), threshold=0.8, prefix_path=prefix_path, files=["I_FORCE_SWEEP.png"])
    T_GOD_FLAG = RecogText(keywords=["魔饰"], roi_type="RU")
    T_ENTER_BTL = RecogText(keywords=["挑战"], roi_area=(328.0, 994.0, 193.0, 161.0))
    T_NEXT_STAGE = RecogText(keywords=["下一层"], roi_area=(0, 0, 720, 1280))
    T_SWEEP = RecogText(keywords=["扫荡"], roi_area=(328.0, 992.0, 192.0, 162.0))
    T_SWEEP_FLAG = RecogText(keywords=["扫荡次数"], roi_area=(226.0, 916.0, 267.0, 140.0))
    T_SWEEP_BTL = RecogText(keywords=["扫荡"], roi_area=(332.0, 1102.0, 193.0, 162.0))
    # T_ENTER_BTL = RecogText(keywords=["挑战"], roi_area=(0, 0, 720, 1280))
    AREA_SWEEP_COUNT = (584, 10, 90, 50)
