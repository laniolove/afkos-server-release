from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


# 不能灰色区分，估计要从颜色下手结合辨认
class RolesAssets:
    prefix_path = "tasks/afkos/assets/roles/"
    I_ROLE = RecogImage(
        name="I_ROLE",
        match_mode="sift",
        roi_area=(38, 340, 432, 218),
        prefix_path=prefix_path,
        files=["xiezi_bg_0.png"],
    )
