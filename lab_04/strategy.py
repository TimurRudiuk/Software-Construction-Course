from observer import LightElementNode

from abc import ABC, abstractmethod

class ImageLoadingStrategy(ABC):
    @abstractmethod
    def load_image(self, href):
        pass

class FileSystemImageLoader(ImageLoadingStrategy):
    def load_image(self, href):
        print(f"Loading image from file system: {href}")
        return f"Image data from file: {href}"

class NetworkImageLoader(ImageLoadingStrategy):
    def load_image(self, href):
        print(f"Loading image from network: {href}")
        return f"Image data from network: {href}"

class LightImageNode(LightElementNode):
    def __init__(self, href, strategy=None):
        super().__init__("img", "inline", "single")
        self.href = href
        self.strategy = strategy or self._determine_strategy(href)
        self.image_data = None

    def _determine_strategy(self, href):
        if href.startswith(("http://", "https://")):
            return NetworkImageLoader()
        else:
            return FileSystemImageLoader()

    def load(self):
        self.image_data = self.strategy.load_image(self.href)
        return self.image_data

local_image = LightImageNode("images/photo.jpg")
local_image.load()

web_image = LightImageNode("https://example.com/image.png")
web_image.load()