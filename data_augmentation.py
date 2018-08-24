import glob
import os
import cv2
import random
import numpy as np
#Takes the images from source directory and creates the image by data augmentation techniques which will increase the robustness in training the CNN.
def sp_noise(img,prob):
    output = np.zeros(img.shape,np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            for k in range(3):
                if rdn < prob:
                    output[i][j][k] = 0
                elif rdn > thres:
                    output[i][j][k] = 255
                else:
                    output[i][j][k] = img[i][j][k]
    return output
def main():
	out= "/Users/sriramreddy/Downloads/523/augmented_data_set/"
	for fruit_dir_path in glob.glob("/Users/sriramreddy/Downloads/523/augmented_data_set/*"):
	    fruit_label = fruit_dir_path.split("/")[-1]
	    for image_path in glob.glob(os.path.join(fruit_dir_path, "*.png")):
	        final=image_path.split("/")[-1]
	        #print("final", final)
	        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
	        #vertical_img = img.copy()
	        vertical_img = cv2.flip( img, 1 )
	        cv2.imwrite(out+fruit_label+"/vertical_flip_" + final, vertical_img)
	        (h, w) = img.shape[:2]
	        center = (w / 2, h / 2)
	        for i in range(15,90,15):
	            M = cv2.getRotationMatrix2D(center, i, 1.0)
	            rotated= cv2.warpAffine(img, M, (w, h))
	            cv2.imwrite(out+fruit_label+"/rotated_by_" + str(i)+"_" + final, rotated)
	        M = np.float32([[1,0,30],[0,1,30]])
	        dst = cv2.warpAffine(img,M,(w,h))
	        cv2.imwrite(out+fruit_label+"/translation_" + final, dst)
	        spn = sp_noise(img,0.003)
	        cv2.imwrite(out + fruit_label+ "/saltandpepper_" + final, spn)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
