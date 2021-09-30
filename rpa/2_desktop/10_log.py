import logging 
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s ")
# logging.debug("aaaa")
# logging.info("자동화 수행 준비")
# logging.warning("경고 메세지")
# logging.error("에러메세지")
# logging.critical("복구가 불가능한 심각한 에러")

# 시간  [로그레벨] 메세지 형태 로그
# logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# logger = logging.getLogger()

# # 로그레벨 설정
# logger.setLevel(logging.DEBUG)

# # 스트림 
# streamHandler = logging.StreamHandler()
# streamHandler.setFormatter(logFormatter)
# logger.addHandler(streamHandler)

# # 파일 
# filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
# fileHandler = logging.FileHandler(filename, encoding="utf-8")
# fileHandler.setFormatter(logFormatter)
# logger.addHandler(fileHandler)

# logger.debug("로그")
