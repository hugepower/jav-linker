import re


class JavInfoExtractor:
    def __init__(self, text):
        """
        初始化 JavInfoExtractor 实例。

        :param text: 要解析的文本字符串，包含演员姓名和视频编号。
        """
        self.text = text
        self.star_pattern = re.compile(r"[一-龥ぁ-んァ-ヴー゛゙]+")
        self.video_id_pattern = re.compile(r"[A-Za-z]+-\d+")

    def extract_stars(self):
        """
        提取文本中的所有姓名。

        :return: 包含所有匹配姓名的列表。
        """
        stars = self.star_pattern.findall(self.text)
        return stars

    def extract_video_id(self):
        """
        提取文本中的视频编号。

        :return: 匹配到的视频编号字符串，如果没有匹配则返回 None。
        """
        match = self.video_id_pattern.search(self.text)
        return match.group(0) if match else None

    def get_movie_info(self):
        """
        综合调用其他方法，返回包含演员姓名和视频编号的元组。

        :return: 包含演员姓名列表和视频编号的元组 (stars, video_id)。
        """
        stars = self.extract_stars()
        video_id = self.extract_video_id()
        return stars, video_id
