from paddleocr import PaddleOCR
import cv2
import numpy as np
import requests
from io import BytesIO

class OCRDataExtractor:
    def __init__(self):
        # 初始化OCR，启用中文识别
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    
    def extract_data_from_image(self, img_path):
        """
        从图片中提取数据，忽略水印
        
        Args:
            img_path (str): 图片路径或URL
            
        Returns:
            list: 识别出的文本数据结构
        """
        # 读取图片
        if img_path.startswith('http'):
            # 从网络URL读取图片
            response = requests.get(img_path)
            img_array = np.array(bytearray(response.content), dtype=np.uint8)
            image = cv2.imdecode(img_array, -1)
        else:
            # 从本地路径读取图片
            image = cv2.imread(img_path)
        
        if image is None:
            raise ValueError("无法读取图片")
        
        # 预处理图片以减少水印影响（可选）
        # 这里可以添加一些图像处理来减弱水印效果
        processed_image = self._preprocess_image(image)
        
        # 执行OCR识别
        result = self.ocr.ocr(processed_image)
        
        # 将结果转换为数据结构
        extracted_data = self._format_ocr_result(result)
        
        return extracted_data
    
    def _preprocess_image(self, image):
        """
        预处理图片以减少水印影响
        
        Args:
            image: 原始图片
            
        Returns:
            processed_image: 处理后的图片
        """
        # 这里可以添加图像处理逻辑来减弱水印
        # 目前直接返回原图
        return image
    
    def _format_ocr_result(self, ocr_result):
        """
        格式化OCR结果为数据结构
        
        Args:
            ocr_result: OCR识别结果
            
        Returns:
            list: 格式化后的数据
        """
        formatted_data = []
        
        # 检查ocr_result是否为None或空
        if ocr_result is None:
            return formatted_data
            
        # 检查ocr_result是否为列表
        if not isinstance(ocr_result, list):
            return formatted_data
            
        # 遍历OCR结果
        for idx in range(len(ocr_result)):
            res = ocr_result[idx]
            # 检查res是否为None
            if res is None:
                continue
            # 检查res是否为列表
            if not isinstance(res, list):
                continue
            # 遍历每一行结果
            for line in res:
                # 检查line是否有足够的元素
                if line is None or len(line) < 2:
                    continue
                    
                # 安全地提取文本和位置信息
                try:
                    # 检查line[0]和line[1]是否存在
                    if len(line) >= 2 and line[1] is not None and len(line[1]) >= 2:
                        text = line[1][0]
                        confidence = line[1][1]
                        position = line[0] if len(line) > 0 else None
                        
                        data_item = {
                            "text": text,
                            "confidence": confidence,
                            "position": position  # 文本在图片中的位置坐标
                        }
                        
                        formatted_data.append(data_item)
                except (IndexError, TypeError) as e:
                    # 忽略无法处理的行
                    continue
        
        return formatted_data

def main():
    # 创建数据提取器实例
    extractor = OCRDataExtractor()
    
    # 图片URL（带有水印）
    img_path = 'https://jiucaigongshe.oss-cn-beijing.aliyuncs.com/AE1852AD-0B4C-450A-9770-9363EC42D5BE.png'
    
    try:
        # 提取数据
        extracted_data = extractor.extract_data_from_image(img_path)
        
        # 打印提取的数据
        print("=== 提取的OCR数据 ===")
        for item in extracted_data:
            print(f"文本: {item['text']}, 置信度: {item['confidence']:.2f}")
            
        # 返回数据结构
        return extracted_data
        
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return []

if __name__ == "__main__":
    data = main()