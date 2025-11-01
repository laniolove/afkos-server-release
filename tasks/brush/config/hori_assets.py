from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class HoriAssets:
    prefix_path = "./tasks/brush/assets/hori/"
    I_img_01 = RecogImage(name="hori:img_01", match_mode="sift", roi_area=(743, 352, 170, 170), prefix_path=prefix_path, files=["I_img_01.png"])
    I_img_02 = RecogImage(name="hori:img_02", match_mode="sift", roi_area=(1159, 487, 121, 120), prefix_path=prefix_path, files=["I_img_02.png"])
    # I_img_03 = RecogImage(name="hori:img_03", match_mode="template", roi_area=(0, 0, 1280, 720), prefix_path=prefix_path, files=["I_img_03.png"])
    I_img_04 = RecogImage(name="hori:img_04", match_mode="sift", roi_area=(856, 458, 170, 170), prefix_path=prefix_path, files=["I_img_04.png"])
    # I_img_05 = RecogImage(name="hori:img_05", match_mode="sift", roi_area=(0, 0, 1280, 720), prefix_path=prefix_path, files=["I_img_05.png"])
    I_img_06 = RecogImage(name="hori:img_06", match_mode="sift", roi_area=(1109, 158, 170, 170), prefix_path=prefix_path, files=["I_img_06.png"])
    I_img_07 = RecogImage(
        name="hori:img_07", match_mode="sift", sift_goods=5, roi_area=(739, 356, 170, 170), prefix_path=prefix_path, files=["I_img_07.png", "I_img_08.png"]
    )
    # I_img_08 = RecogImage(name="hori:img_08", match_mode="sift", roi_area=(739, 356, 170, 170), prefix_path=prefix_path, files=["I_img_08.png"])
    I_img_09 = RecogImage(name="hori:img_09", match_mode="sift", roi_area=(415, 224, 170, 170), prefix_path=prefix_path, files=["I_img_09.png"])
    I_img_010 = RecogImage(name="hori:img_010", match_mode="sift", sift_goods=8, roi_area=(0, 0, 1280, 720), prefix_path=prefix_path, files=["I_img_010.png"])
    I_img_011 = RecogImage(name="hori:img_011", match_mode="sift", roi_area=(868, 458, 170, 184), prefix_path=prefix_path, files=["I_img_011.png"])
    I_img_012 = RecogImage(name="hori:img_012", match_mode="template", roi_area=(536, 264, 208, 222), prefix_path=prefix_path, files=["I_img_012.png"])
    I_img_013 = RecogImage(
        name="hori:img_013", match_mode="sift", sift_goods=6, roi_area=(1016, 503, 170, 170), prefix_path=prefix_path, files=["I_img_013.png"]
    )
    I_img_014 = RecogImage(
        name="hori:img_014", match_mode="sift", sift_goods=5, roi_area=(509, 563, 170, 157), prefix_path=prefix_path, files=["I_img_014.png"]
    )
    # I_img_015 = RecogImage(name="hori:I_img_015", match_mode="sift", roi_area=(0, 0, 1280, 720), prefix_path=prefix_path, files=["I_img_015.png"])
    # I_img_016 = RecogImage(name="hori:I_img_016", match_mode="sift", roi_area=(0, 0, 1280, 720), prefix_path=prefix_path, files=["I_img_016.png"])
    I_img_017 = RecogImage(
        name="hori:I_img_017", match_mode="sift", sift_goods=40, roi_area=(896, 505, 170, 170), prefix_path=prefix_path, files=["I_img_017.png"]
    )
    I_img_018 = RecogImage(name="hori:I_img_018", match_mode="sift", roi_area=(508, 13, 170, 170), prefix_path=prefix_path, files=["I_img_018.png"])
    I_img_019 = RecogImage(name="hori:I_img_019", match_mode="sift", roi_area=(0, 600, 1280, 120), prefix_path=prefix_path, files=["I_img_019.png"])
    I_img_020 = RecogImage(name="hori:I_img_020", match_mode="template", roi_area=(1062, 25, 170, 168), prefix_path=prefix_path, files=["I_img_020.png"])
    I_img_021 = RecogImage(name="hori:I_img_021", match_mode="template", roi_area=(978, 0, 164, 141), prefix_path=prefix_path, files=["I_img_021.png"])
    I_img_022 = RecogImage(
        name="hori:I_img_022", sift_goods=5, match_mode="sift", roi_area=(576, 307, 170, 170), prefix_path=prefix_path, files=["I_img_022.png"]
    )
    I_img_023 = RecogImage(name="hori:I_img_023", match_mode="template", roi_area=(404, 92, 178, 182), prefix_path=prefix_path, files=["I_img_023.png"])
    I_img_024 = RecogImage(name="hori:I_img_024", match_mode="template", roi_area=(58, 569, 204, 151), prefix_path=prefix_path, files=["I_img_024.png"])
    I_img_025 = RecogImage(name="hori:I_img_025", match_mode="sift", roi_area=(634, 210, 170, 170), prefix_path=prefix_path, files=["I_img_025.png"])
    I_img_026 = RecogImage(name="hori:I_img_026", match_mode="template", roi_area=(197, 393, 168, 170), prefix_path=prefix_path, files=["I_img_026.png"])
    I_img_027 = RecogImage(name="hori:I_img_027", match_mode="template", roi_area=(273, 73, 170, 156), prefix_path=prefix_path, files=["I_img_027.png"])
    I_img_028 = RecogImage(name="hori:I_img_028", match_mode="template", roi_area=(1096, 158, 170, 156), prefix_path=prefix_path, files=["I_img_027.png"])
    I_img_029 = RecogImage(name="hori:I_img_029", match_mode="sift", roi_area=(1126, 0, 154, 111), prefix_path=prefix_path, files=["I_img_029.png"])
    I_img_030 = RecogImage(name="hori:I_img_030", match_mode="sift", roi_area=(933, 581, 170, 139), prefix_path=prefix_path, files=["I_img_030.png"])
    I_img_031 = RecogImage(name="hori:I_img_031", match_mode="sift", roi_area=(1122, 558, 158, 162), prefix_path=prefix_path, files=["I_img_031.png"])
    I_img_032 = RecogImage(name="hori:I_img_032", match_mode="sift", roi_area=(744, 396, 170, 170), prefix_path=prefix_path, files=["I_img_032.png"])
    I_img_033 = RecogImage(name="hori:I_img_033", match_mode="template", roi_area=(0, 0, 114, 120), prefix_path=prefix_path, files=["I_img_033.png"])
    T_RT_NEW = RecogText(keywords=["NEW", "New"], roi_area=(946.0, 0, 173.0, 130.0))
    T_SELROLE_NEW = RecogText(keywords=["NEW", "New"], roi_area=(0, 350, 1280, 70))
    T_FINISH_SEL = RecogText(keywords=["完成"], roi_area=(1052.0, 294.0, 228.0, 151.0))
    T_QIANMING_FIRST = RecogText(keywords=["FIRSTNAME", "FIRST NAME"], roi_area=(0, 0, 1280, 720))
    T_QIANMING_LAST = RecogText(keywords=["LASTNAME", "LAST NAME"], roi_area=(0, 0, 1280, 720))
    T_QIANMING_FILISH = RecogText(keywords=["名"], roi_area=(533.0, 516.0, 200.0, 143.0))
    # T_SEL_TITLE = RecogText(keywords=["请"], roi_area=(0, 0, 1280, 720))
