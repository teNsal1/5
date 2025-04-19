import os
from typing import Tuple
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    supported_formats: Tuple[str, ...] = ('.jpg', '.jpeg', '.png')
    

    def __init__(self, quality: int) -> None:
        self.__quality = quality
    

    @property
    def quality(self) -> int:
        return self.__quality
    

    @quality.setter
    def quality(self, value: int) -> None:
        if 1 <= value <= 100:
            self.__quality = value
        else:
            raise ValueError("Качество должно быть в диапазоне от 1 до 100")