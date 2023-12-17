# OurCulture
About
--
OurCulture app will help users to learn more about Balinese traditions, customs, and art forms. OurCulture is designed not only for educational image classification, but also as a dynamic marketplace where users can upload and sell authentic Balinese products. OurCulture app is equipped with a machine learning model that can detect cultural objects in Bali. Simply by take a picture with your phone, the machine learning model will automatically detect the object, and then the application will display complete information related to the detected object. The implementation of this machine learning model will certainly make it easier for users to learn various aspects of culture in Bali.


Machine Learning Development Documentation
--
The project is based from Google Colab (due to limited system requirements of our laptop/PC). Using Machine Learning with TensorFlow as framework to classify the image of culture

1. Load Dataset
   - Link : [https://drive.google.com/drive/folders/14QNe840UxAj_Xr1O48hXKkKKSbzrGzn4?usp=drive_link](https://drive.google.com/drive/folders/14QNe840UxAj_Xr1O48hXKkKKSbzrGzn4?usp=drive_link)
2. Pre-processing Data
   - Spliting dataset using library split-folder into
       - 80% training data
       - 20% validation data
    - Data augmantion using ImageDataGenerator class of Keras
    - Resizing the images into 150x150x3 and resizing by 1/255.
4. Training
   - Using transfer learning
   - Using base model Inception v3
   - Using binary_crossentropy as loss
   - Using Adam as optimizer
   - Added more layer to make the model accuracy better
      - Added Conv2D(32, (3, 3), activation='relu') layer
      - Added MaxPooling2D(2,2) layer
      - Added Conv2D(64, (2, 2), activation='relu') layer
      - Added flatten layer
      - Added Dense(2048, activation='relu') layer
      - Added Dropout(0.2) layer
      - Added output layer Dense(30, activation='softmax')
    - Trainign with 50 epochs
    - The result:
        - training accuracy: 95%
        - validation accuracy: 91%
        - training loss: 1%
        - validation loss: 5%
6. Save the Model
   - Saved the model in .h5 format
