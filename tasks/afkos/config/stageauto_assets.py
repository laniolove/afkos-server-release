from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class StageAutoAssets:
    prefix_path = "tasks/afkos/assets/stageauto/"
    T_AUTO_BTL = RecogText(keywords=["自动挑战"], roi_area=(249.0, 1111.0, 253.0, 160.0))
    T_HANGUP_BTN = RecogText(keywords=["挂机托管"], roi_area=(520.0, 792.0, 200.0, 148.0))
    T_USE_JOB = RecogText(keywords=["一键采用"], roi_area=[302.0, 986.0, 250.0, 159.0])
    T_NOT_HAVE = RecogText(keywords=["未拥有"], roi_type="D")
    T_CANCEL_HAVE = RecogText(keywords=["取消"], roi_area=(143.0, 760.0, 184.0, 154.0))
    T_UNLOCK_WORD = RecogText(keywords=["新词条解锁"], roi_area=[181.0, 984.0, 332.0, 138.0])
    T_CLOSE_WORD = RecogText(keywords=["关闭"], roi_area=[275.0, 1124.0, 171.0, 147.0])
    T_EXT_NOT_HAVE = RecogText(keywords=["未拥有"], roi_area=(264.0, 549.0, 182.0, 143.0))
    T_OP_FLAG_BTL = RecogText(keywords=["手动战斗"], roi_area=(36.0, 927.0, 211.0, 140.0))
    I_MOVE_L = RecogImage(name="切换左边作业", roi_area=[0, 598, 131, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_left_0.png"])
    I_MOVE_R = RecogImage(name="切换右边作业", roi_area=[574, 598, 146, 177], threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    I_NEW_WORD_R = RecogImage(name="新词条切换右边", roi_type="R", threshold=0.75, prefix_path=prefix_path, files=["sel_record_right_0.png"])
    T_JOB_ENTER = RecogText(keywords=["通关"], roi_area=[123.0, 1169.0, 151.0, 100.0])
    # T_ENTER_BTL = RecogText(keywords=["挑战"], roi_area=(0, 0, 720, 1280))
