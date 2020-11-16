#导入OpenCV视觉库
import cv2
#捕捉帧率，笔记本电脑摄像头设置为0
capture = cv2.VideoCapture(0)
#循环显示帧率
while(True):
	ret, frame = capture.read()
	#显示窗口第一个参数是窗口名，第二个参数是内容
	cv2.imshow('JERRY_Ai', frame)
	if cv2.waitKey(1) == ord('q'): #按Q退出
		break