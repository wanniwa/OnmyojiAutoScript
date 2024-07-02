from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class WantedQuestsAssets: 


	# Click Rule Assets
	# 秘闻的挑战对话 
	C_SECRET_CHAT = RuleClick(roi_front=(597,296,59,100), roi_back=(597,296,59,100), name="secret_chat")
	# 特殊的庭院需要点击，然后才能找到这个悬赏 
	C_SPECIAL_MAIN = RuleClick(roi_front=(409,572,32,30), roi_back=(404,569,41,35), name="special_main")


	# Ocr Rule Assets
	# 挑战券的数量 
	O_WQ_NUMBER = RuleOcr(roi=(569,13,50,32), area=(569,13,50,32), mode="Digit", method="Default", keyword="", name="wq_number")
	# 悬赏封印 
	O_WQ_WANTED = RuleOcr(roi=(9,145,123,381), area=(9,145,123,381), mode="Full", method="Default", keyword="", name="wq_wanted")
	# Ocr-description 
	O_WQ_TEXT_1 = RuleOcr(roi=(67,233,52,32), area=(67,233,52,32), mode="Single", method="Default", keyword="封印", name="wq_text_1")
	# Ocr-description 
	O_WQ_TEXT_2 = RuleOcr(roi=(66,377,52,32), area=(66,377,52,32), mode="Single", method="Default", keyword="封印", name="wq_text_2")
	# Ocr-description 
	O_WQ_NUM_1 = RuleOcr(roi=(32,260,72,27), area=(32,260,72,27), mode="DigitCounter", method="Default", keyword="", name="wq_num_1")
	# Ocr-description 
	O_WQ_NUM_2 = RuleOcr(roi=(34,406,65,24), area=(34,406,65,24), mode="DigitCounter", method="Default", keyword="", name="wq_num_2")
	# Ocr-description 
	O_WQ_TYPE_1 = RuleOcr(roi=(544,238,55,36), area=(544,238,55,36), mode="Single", method="Default", keyword="", name="wq_type_1")
	# Ocr-description 
	O_WQ_TYPE_2 = RuleOcr(roi=(544,311,55,30), area=(544,311,55,30), mode="Single", method="Default", keyword="", name="wq_type_2")
	# Ocr-description 
	O_WQ_TYPE_3 = RuleOcr(roi=(544,382,54,30), area=(544,382,54,30), mode="Single", method="Default", keyword="", name="wq_type_3")
	# Ocr-description 
	O_WQ_TYPE_4 = RuleOcr(roi=(545,452,52,32), area=(545,452,52,32), mode="Single", method="Default", keyword="", name="wq_type_4")
	# Ocr-description 
	O_WQ_INFO_1 = RuleOcr(roi=(609,236,309,45), area=(609,236,309,45), mode="Single", method="Default", keyword="", name="wq_info_1")
	# Ocr-description 
	O_WQ_INFO_2 = RuleOcr(roi=(612,308,298,41), area=(612,308,298,41), mode="Single", method="Default", keyword="", name="wq_info_2")
	# Ocr-description 
	O_WQ_INFO_3 = RuleOcr(roi=(612,376,305,44), area=(612,376,305,44), mode="Single", method="Default", keyword="", name="wq_info_3")
	# Ocr-description 
	O_WQ_INFO_4 = RuleOcr(roi=(613,446,315,44), area=(613,446,315,44), mode="Single", method="Default", keyword="", name="wq_info_4")


	# Image Rule Assets
	# description 
	I_WQC_LOCK = RuleImage(roi_front=(620,528,27,31), roi_back=(620,528,27,31), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/chanllenge/chanllenge_wqc_lock.png")
	# description 
	I_WQC_UNLOCK = RuleImage(roi_front=(621,527,26,28), roi_back=(621,527,26,28), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/chanllenge/chanllenge_wqc_unlock.png")
	# 挑战 
	I_WQC_FIRE = RuleImage(roi_front=(893,503,123,64), roi_back=(871,485,164,91), threshold=0.7, method="Template matching", file="./tasks/WantedQuests/chanllenge/chanllenge_wqc_fire.png")


	# Image Rule Assets
	# description 
	I_WQ_INVITE_1 = RuleImage(roi_front=(137,361,39,47), roi_back=(108,338,100,100), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_invite_1.png")
	# description 
	I_WQ_INVITE_2 = RuleImage(roi_front=(462,361,37,47), roi_back=(435,336,100,100), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_invite_2.png")
	# description 
	I_WQ_INVITE_3 = RuleImage(roi_front=(754,366,39,42), roi_back=(728,339,100,100), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_invite_3.png")
	# description 
	I_WQ_FRIEND_1 = RuleImage(roi_front=(240,185,180,80), roi_back=(240,185,180,80), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_friend_1.png")
	# description 
	I_WQ_FRIEND_2 = RuleImage(roi_front=(530,185,180,80), roi_back=(530,185,180,80), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_friend_2.png")
	# description 
	I_WQ_FRIEND_3 = RuleImage(roi_front=(240,285,180,80), roi_back=(240,285,180,80), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_friend_3.png")
	# description 
	I_WQ_FRIEND_4 = RuleImage(roi_front=(530,285,180,80), roi_back=(530,285,180,80), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_friend_4.png")
	# description 
	I_WQ_FRIEND_5 = RuleImage(roi_front=(240,385,180,80), roi_back=(240,385,180,80), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/invite_wq_friend_5.png")
	# 悬赏封印邀请确定按钮 
	I_WQ_INVITE_ENSURE = RuleImage(roi_front=(500,540,132,60), roi_back=(500,540,140,65), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_invite_ensure.png")
	# 悬赏封印邀请取消按钮 
	I_WQ_INVITE_CANCEL = RuleImage(roi_front=(230,540,132,60), roi_back=(230,540,140,65), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_invite_cancel.png")
	# 邀请好友被选中标记 
	I_WQ_INVITE_SELECTED = RuleImage(roi_front=(380,185,32,32), roi_back=(380,185,345,350), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_invite_selected.png")
	# 邀请同服好友,由于选中与未选中亮度有区别,查找图片可能会出错,建议只使用位置信息 
	I_WQ_INVITE_SAME_SVR = RuleImage(roi_front=(170,90,60,35), roi_back=(170,90,105,65), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_invite_same_svr.png")
	# 邀请跨服好友,由于选中与未选中亮度有区别,查找图片可能会出错,建议只使用位置信息 
	I_WQ_INVITE_DIFF_SVR = RuleImage(roi_front=(280,90,60,35), roi_back=(280,90,105,65), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_invite_diff_svr.png")
	# 从左到右第一个协作任务的类型 
	I_WQ_COOPERATION_TYPE_GOLD_1 = RuleImage(roi_front=(195,505,180,90), roi_back=(195,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_gold.png")
	# 从左到右第一个协作任务的类型 
	I_WQ_COOPERATION_TYPE_JADE_1 = RuleImage(roi_front=(195,505,180,90), roi_back=(195,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_jade.png")
	# 从左到右第一个协作任务的类型为狗粮 
	I_WQ_COOPERATION_TYPE_DOG_FOOD_1 = RuleImage(roi_front=(195,505,180,90), roi_back=(195,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_dog_food.png")
	# 从左到右第一个协作任务的类型为猫粮 
	I_WQ_COOPERATION_TYPE_CAT_FOOD_1 = RuleImage(roi_front=(195,505,180,90), roi_back=(195,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_cat_food.png")
	# 从左到右第一个协作任务的类型 
	I_WQ_COOPERATION_TYPE_SUSHI_1 = RuleImage(roi_front=(195,505,180,90), roi_back=(195,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_sushi.png")
	# 从左到右第二个协作任务的类型 
	I_WQ_COOPERATION_TYPE_GOLD_2 = RuleImage(roi_front=(490,505,180,90), roi_back=(490,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_gold.png")
	# 从左到右第二个协作任务的类型 
	I_WQ_COOPERATION_TYPE_JADE_2 = RuleImage(roi_front=(490,505,180,90), roi_back=(490,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_jade.png")
	# 从左到右第二个协作任务的类型为狗粮 
	I_WQ_COOPERATION_TYPE_DOG_FOOD_2 = RuleImage(roi_front=(490,505,180,90), roi_back=(490,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_dog_food.png")
	# 从左到右第二个协作任务的类型为猫粮 
	I_WQ_COOPERATION_TYPE_CAT_FOOD_2 = RuleImage(roi_front=(490,505,180,90), roi_back=(490,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_cat_food.png")
	# 从左到右第二个协作任务的类型 
	I_WQ_COOPERATION_TYPE_SUSHI_2 = RuleImage(roi_front=(490,505,180,90), roi_back=(490,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_sushi.png")
	# 从左到右第三个协作任务的类型 
	I_WQ_COOPERATION_TYPE_GOLD_3 = RuleImage(roi_front=(790,505,180,90), roi_back=(790,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_gold.png")
	# 从左到右第三个协作任务的类型 
	I_WQ_COOPERATION_TYPE_JADE_3 = RuleImage(roi_front=(790,505,180,90), roi_back=(790,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_jade.png")
	# 从左到右第三个协作任务的类型为狗粮 
	I_WQ_COOPERATION_TYPE_DOG_FOOD_3 = RuleImage(roi_front=(790,505,180,90), roi_back=(790,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_dog_food.png")
	# 从左到右第三个协作任务的类型为猫粮 
	I_WQ_COOPERATION_TYPE_CAT_FOOD_3 = RuleImage(roi_front=(790,505,180,90), roi_back=(790,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_cat_food.png")
	# 从左到右第三个协作任务的类型 
	I_WQ_COOPERATION_TYPE_SUSHI_3 = RuleImage(roi_front=(790,505,180,90), roi_back=(790,505,180,90), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/invite/wq_cooperation_type_sushi.png")


	# Ocr Rule Assets
	# 邀请好友界面 好友列表第一列 
	O_WQ_INVITE_COLUMN_1 = RuleOcr(roi=(240,185,190,340), area=(240,185,190,340), mode="FULL", method="Default", keyword="", name="wq_invite_column_1")
	# 邀请好友界面 好友列表第二列 
	O_WQ_INVITE_COLUMN_2 = RuleOcr(roi=(520,185,190,340), area=(520,185,190,340), mode="FULL", method="Default", keyword="", name="wq_invite_column_2")


	# Image Rule Assets
	# 封印 
	I_WQ_SEAL = RuleImage(roi_front=(244,181,40,40), roi_back=(56,152,664,396), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_wq_seal.png")
	# 勾号 
	I_WQ_DONE = RuleImage(roi_front=(248,183,37,39), roi_back=(107,147,570,389), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_wq_done.png")
	# 一键追踪 
	I_TRACE_ENABLE = RuleImage(roi_front=(1097,588,101,70), roi_back=(1097,588,101,70), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_trace_enable.png")
	# 取消追踪 
	I_TARCE_DISENABLE = RuleImage(roi_front=(1091,586,108,70), roi_back=(1091,586,108,70), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_tarce_disenable.png")
	# 奖励宝箱 
	I_WQ_BOX = RuleImage(roi_front=(48,187,43,38), roi_back=(20,137,100,397), threshold=0.7, method="Template matching", file="./tasks/WantedQuests/wq/wq_wq_box.png")
	# 小号追踪 
	I_TRACE_TRUE = RuleImage(roi_front=(173,187,28,29), roi_back=(173,187,28,29), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_trace_true.png")
	# 小号不追踪 
	I_TRACE_FALSE = RuleImage(roi_front=(170,186,31,32), roi_back=(170,186,31,32), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_trace_false.png")
	# description 
	I_GOTO_1 = RuleImage(roi_front=(978,234,87,45), roi_back=(978,234,87,45), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_goto_1.png")
	# description 
	I_GOTO_2 = RuleImage(roi_front=(979,305,88,43), roi_back=(979,305,88,43), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_goto_2.png")
	# description 
	I_GOTO_3 = RuleImage(roi_front=(979,373,88,47), roi_back=(979,373,88,47), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_goto_3.png")
	# description 
	I_GOTO_4 = RuleImage(roi_front=(979,447,87,42), roi_back=(979,447,87,42), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_goto_4.png")
	# 判断是否还有任务 
	I_WQ_CHECK_TASK = RuleImage(roi_front=(110,154,21,125), roi_back=(73,122,69,459), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_wq_check_task.png")


	# Image Rule Assets
	# 奇怪了之前的不能用 
	I_WQSE_FIRE = RuleImage(roi_front=(1041,556,100,100), roi_back=(1016,534,147,138), threshold=0.8, method="Template matching", file="./tasks/WantedQuests/wq/wq_wqse_fire.png")


