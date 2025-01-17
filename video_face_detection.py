import numpy as np
import cv2

def detect_face():
	cap = cv2.VideoCapture(0)
	while True:

		ret, image = cap.read()
		
		prototxt = "deploy.prototxt.txt"
		model = "res10_300x300_ssd_iter_140000.caffemodel"
		confidence_img = 0.5

		net = cv2.dnn.readNetFromCaffe(prototxt, model)
	
		(h, w) = image.shape[:2]
	
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, 
			(300, 300), (104.0, 177.0, 123.0))
	
		net.setInput(blob)
		detections = net.forward()
	
		for i in range(0, detections.shape[2]):
			confidence = detections[0, 0 , i, 2]
			if confidence > confidence_img:
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY)  = box.astype("int")
	
				text = "{:.2f}%".format(confidence * 100)
				y = startY - 10 if startY - 10 > 10 else startY + 10
				cv2.rectangle(image, (startX, startY), (endX, endY),
					(0, 255, 0), 2)
				cv2.putText(image, text, (startX, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
	
			cv2.imshow("Output", image)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
	

if __name__ == '__main__':
	detect_face()
	

	

	

	