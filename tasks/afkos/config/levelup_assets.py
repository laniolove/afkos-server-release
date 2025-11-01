from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class LevelUpAssets:
    prefix_path = "tasks/afkos/assets/levelup/"
    T_LEVEL_UP = RecogText(keywords=["快速升级"], roi_area=(243.0, 1036.0, 233.0, 151.0))
    AREA_COLOR_NOT_LEVELUP = {"location": T_LEVEL_UP, "area": (418, 1062, 22, 16), "color": [103, 103, 103]}
    AREA_COLOR_LEVELUP = {"location": T_LEVEL_UP, "area": (418, 1062, 22, 16), "color": [203, 118, 49]}
    AREA_COLOR_TEST = {"location": T_LEVEL_UP, "area": (418, 1062, 22, 16), "color": [49, 9, 5]}
