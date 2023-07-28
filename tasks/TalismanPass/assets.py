from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class TalismanPassAssets: 


	# Image Rule Assets
	# 领取全部 
	I_TP_GET_ALL = RuleImage(roi_front=(903,599,70,71), roi_back=(903,599,70,71), threshold=0.8, method="Template matching", file="./tasks/TalismanPass/tp/tp_tp_get_all.png")
	# 任务 的右上方红点 
	I_RED_POINT_TASK = RuleImage(roi_front=(1226,312,23,24), roi_back=(1226,312,23,24), threshold=0.8, method="Template matching", file="./tasks/TalismanPass/tp/tp_red_point_task.png")
	# 今日 的右上方红点 
	I_RED_POINT_DAY = RuleImage(roi_front=(632,157,23,26), roi_back=(632,157,23,26), threshold=0.8, method="Template matching", file="./tasks/TalismanPass/tp/tp_red_point_day.png")
	# 本周 的右上方红点 
	I_RED_POINT_WEEK = RuleImage(roi_front=(795,156,24,25), roi_back=(795,156,24,25), threshold=0.8, method="Template matching", file="./tasks/TalismanPass/tp/tp_red_point_week.png")


