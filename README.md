# **CIFAR10 Image Recognition**
this project uses machine learning and a convolutional neural network to  classify images provided to it into one of 10 categories. I made this while learning about AI and machine learning as the final project of a summer camp. This version of the project on github also includes the source code used to generate the .h5 neural network file. The project is also on itch.io [here](https://spaceshark123.itch.io/cifar10-image-recognition)

### **The categories are:**

- airplane
- automobile
- bird
- cat
- deer
- dog
- frog
- horse
- ship
- truck



The neural network works by taking an image, resizing it to a 32x32 jpeg, and uses machine learning to classify the image. It was trained using the **CIFAR10** data set.


**Note: Because the images are resized to 32x32 to save processing time, fine details are lost. This makes detailed images a lot more likely to be classified incorrectly. Additionally, non-square images will be stretched/compressed to make them square so the algorithm might misclassify them because of that, and png transparency will be lost in the conversion to jpeg.**



## HOW TO RUN PROGRAM
Download the files,  unzip it, and open the resulting folder. Inside, put any image into the folder. There is a test folder with some starter images that you have to move out into the same folder as the code files. Note that the default name of the image that is searched for is **photo.jpg**, but an optional filename can be added for a different image with a different file format (png, webp, etc). Next, open command prompt if on windows and terminal on mac. run the command:

	cd <directory of the unzipped folder>

making sure to replace with the directory of the unzipped folder. Next, the following command will run the program:

	python "Image Recognition.py" <optional filename>
	
The optional filename can be left out, and the program will default to photo.jpg. If you get an error, you might have to install python or if it is already installed, the image might not have been found, so you need to enter a proper file path. If it still doesn't work, type the following:

	pip install pip
	 
	pip install tensorflow
	 
	pip install numpy
	
	pip install matplotlib
	
	pip install keras



Enjoy!
