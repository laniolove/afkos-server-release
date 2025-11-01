from module.recog.recog_text import RecogText
from module.recog.recog_image import RecogImage


class E9Assets:
    prefix_path = "./tasks/record/assets/e9/"
    IMAGES = {
        "sel_skill_role": RecogImage(
            name="sel_skill_role", match_mode="sift", roi_area=(2, 400, 200, 320), threshold=0.7, prefix_path=prefix_path, files=["sel_skill_role.png"]
        ),
    }
    TEXTS = {
        "helplevel": RecogText(keywords=["#01"], roi_area=(0, 0, 1280, 720)),
    }
