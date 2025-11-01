from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class ProcessAssets:
    prefix_path = "tasks/afkos/assets/process/"
    startLists = [
        RecogImage(
            name="I_XiGua_ENTER", roi_area=(277, 355, 170, 170), match_mode="sift", threshold=0.75, prefix_path=prefix_path, files=["I_XiGua_ENTER.png"]
        ),
        # I_XiGua_ENTER = RecogImage(name="进入擂台", roi_type="A", threshold=0.75, prefix_path=prefix_path, files=["I_XiGua_ENTER.png"])
        RecogText(keywords=["学徒"], roi_area=(254.0, 372.0, 194.0, 142.0)),
        RecogText(keywords=["学徒"], roi_area=(251.0, 640.0, 217.0, 149.0)),
        RecogText(keywords=["为我寻找对手"], roi_area=(240.0, 861.0, 256.0, 142.0)),
        RecogText(keywords=["挑战"], roi_area=(389.0, 1102.0, 195.0, 118.0)),
        RecogText(keywords=["点击空白处", "白处继续"], roi_area=[221.0, 1108.0, 279.0, 118.0]),
        RecogText(keywords=["再次挑战"], black_list=["天赋挑战", "挑战", "自动挑战", "动挑战"], roi_area=[391.0, 1155.0, 216.0, 118.0]),
    ]
    endLists = [
        RecogText(keywords=["体力不足"], roi_area=(254.0, 316.0, 212.0, 145.0)),
    ]
