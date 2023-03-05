# machine_learning_image_classification

The main objective of this workshop is to create an image classification system based on
Machine Learning and Data Mining algorithms. Classification is the process of predicting
of the class of a given image. Classes are sometimes called labels or categories. As
classification will be performed based on the image descriptor vector instead of using the image.
instead of using the image.<br>
The classification can be supervised or unsupervised; for supervised classification we have
already classified with their labels in advance while for the case of unsupervised classification the
unsupervised classification the elements are not classified and we try to group them into classes.
In this workshop, our objective is to develop a supervised classification system. In this
system, two parts (or 3) will be developed: <br><br>
1-Learning: Create a model based on the descriptors of the image database. This
phase consists of the approximation of a mapping function between the matrix of features (input variables)
(input variables) and the labels (output variables)<br>
2-Classification (prediction): predict the label of a new input (image) by the model
developed.<br>
![image](https://user-images.githubusercontent.com/108405071/222991128-3bc7f0c9-1a7b-47fa-902a-23361a36af67.png)
<br>
The validation and evaluation of a classification system is performed by dividing the training image base into two parts
into two parts: a training part and a test part.
test or validation base. Knowing that the images are labeled beforehand, in the training base, the images and the labels are stored in the test base.
<br>
the images and the labels will be used to build the classification model, while the images of the
while the images of the test database will be used to predict the labels of each image.
The predicted labels will be compared with the original labels to measure the
the performance of the developed model. The figure below presents the general scheme of the classification/model validation process.
classification/validation process.<br>
![image](https://user-images.githubusercontent.com/108405071/222991264-357efc83-9812-4989-8746-e17dcc3b7dd9.png) <br<br>
<br>
In this classification workshop, we will use only two groups of images (two classes).
class); the first class will contain the images of type (class) "car" and the second class will contain the images of type "boat".<br>
will contain the images of type "boat". Each class will be put in a folder with the names
successively with the names "obj_car" for cars and "obj_ship" for boats. The class
"obj_car" contains 400 images and "obj_ship" contains 90 images. The figure below
shows some images of the two classes <br>

![image](https://user-images.githubusercontent.com/108405071/222991409-bc4c1222-ac99-462e-8ec1-9d740a4544c4.png)

<b>Objective</b><br>
The objective of the supervised classification is to be able to correctly predict the class of a (new) image
(new) image from the knowledge (training already established based on the classes
of the images in the database). Thus, we need to establish a classification model using the two classes
"and "ship" of the database. The classifier chosen for this task is the SVM.
As for the CBIR, we will first build an index matrix based on the features of the images.
features of the images. The chosen features are : The statistical moments of
in the RGB space, the color histogram in the HSV space, the statistical measures of the
of the GLCM matrix for the texture and the Hu moments for the shape (see workshop
CBIR). This feature matrix (Features) will be passed with the labels (classes) to the
classifier to build a classification model that will be used for prediction (see Figure.
1)
