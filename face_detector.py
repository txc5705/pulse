import cv2
import data_parser

class faceDetector:
    def __init__(self, cascade):
        self.training_data = data_parser.cascadeParser().parse(cascade)

    def evaluateFeature(self,x,y,w,h,rects,scale):
        

    def evaluate(self,x,y,w,h,scale):
        stage_pass = True
        for stage in self.training_data[0]:
            threshold = stage.threshold
            sum = 0

            for classifier in stage.weakClassifiers:
                value = 0
                i = 0

                while True:
                    feature_sum,inv_area,vnorm = evaluateFeature(x,y,w,h,stage[1][classifier.index],scale)

                    if feature_sum*inv_area < classifier.threshold*vnorm:
                        value = classifier.left
                        break
                    else:
                        value = classifier.right
                        break

                sum += value

            stage_pass = sum >= threshold
            if not stage_pass:
                return stage_pass

        return stage_pass

    def detect_face(self, photo):
        results = []
        norm = cv2.normalize(photo, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        integral = cv2.integral(norm)
        stages = self.training_data[0]
        scale = 1
        factor = 1.25
        window_size = 20 # Default for our data
        window_width,window_height = 20,20
        width, height = integral.shape
        while window_width < width and window_height < height:
            window_width = window_height = int(scale*20)
            step = int(scale*2.4)
            x = 0
            while x < height-scale*24:
                y = 0
                while y < width-scale*24:
                    if evaluate(x,y,window_width,window_height,scale):
                        results.append((x,y,window_width,window_height))

if __name__ == "__main__":
    d = faceDetector("haarcascade_frontalface_default.xml")
    print(d.detect_face(cv2.imread('download.jpg',0)))