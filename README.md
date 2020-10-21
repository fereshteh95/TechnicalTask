# TechnicalTask

## Task 1

A common method for content based image retrieval is using CNNs and Deep Learning to extract the features of the query image and compare the features with the image features in the database. The architecture for such network is show blew.

![](https://github.com/fereshteh95/TechnicalTask/blob/main/Images/ARCHITECTURE.JPG)

So when a user submits a query image, it extracts features from the image and then we compare query features with the features in the database and then we rank the relevant results and return them.

To train such network we need to use a positive and negative image as well as the query image. Positive image is an image similar to query and negative image is different from the query.

![](https://github.com/fereshteh95/TechnicalTask/blob/main/Images/TRAIN.JPG)

The network is then trained to minimize the distance between query feature and positive feature while, simultaneously, maximizing the distance between query feature and negative feature. This method ensureds that the extracted features from an image are accurate enough. 

However, since I do not have access to a database large enough to train a deep neural network, I will be using a simplre yet effective method via OpenCV and predefined cv2.matchTemplate() method.It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image. Several comparison methods are implemented in OpenCV. (You can check docs for more details). It returns a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel match with template. 
