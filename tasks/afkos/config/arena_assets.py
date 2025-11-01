from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class ArenaAssets:
    prefix_path = "tasks/afkos/assets/arena/"
    I_NOT_RESET = RecogImage(name="不能重置", roi_area=[556, 1103, 164, 177], threshold=0.75, prefix_path=prefix_path, files=["notReset.png"])
    I_SEL_ROLE = RecogImage(name="选择对手战斗", roi_area=[556, 1103, 164, 177], threshold=0.75, prefix_path=prefix_path, files=["selRoleBattle.png"])
    I_0_TIPS = RecogImage(name="0钻石提示", roi_type="A", threshold=0.75, prefix_path=prefix_path, files=["cost0zuan.png"])
    I_20_TIPS = RecogImage(name="20钻石提示", roi_type="A", threshold=0.75, prefix_path=prefix_path, files=["cost20zuan.png"])
    T_BATTLE_ENTER = RecogText(keywords=["继续挑战", "开始挑战"], roi_area=[356.0, 1108.0, 256.0, 158.0])
    T_RESET = RecogText(keywords=["重置"], roi_area=[549.0, 1152.0, 171.0, 128.0])
    T_BTL_START = RecogText(keywords=["战斗", "战牛"], roi_area=[325.0, 1110.0, 194.0, 169.0])
    T_JUMP = RecogText(keywords=["跳过"], roi_type="A")
    T_FANGQI = RecogText(keywords=["放弃"], roi_type="A")
    T_SEL_ROLE_FLAG = RecogText(keywords=["选择对手"], roi_area=(179.0, 8.0, 356.0, 190.0))
