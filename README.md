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



The neural network works by taking a square image, resizing it to 32x32, and uses machine learning to classify the image. It was trained using the **CIFAR10** data set.


Note: Because the images are resized to 32x32 to save processing time, fine details are lost. This makes detailed images a lot more likely to be classified incorrectly



HOW TO RUN PROGRAM
Download the files,  unzip it, and open the resulting folder. Inside, put any **SQUARE IMAGE** into the folder. There is a test folder with some starter images that you have to move out into the same folder as the code files. **IT MUST BE A .jpg FILE.** Then, remember to **RENAME THE IMAGE TO photo.jpg**. Next, open command prompt if on windows and terminal on mac. run the command:

	cd <directory of the unzipped folder>

making sure to replace with the directory of the unzipped folder. Next, the following command will run the program:

	python "Image Recognition.py"
	
If you get an error, you might have to install python or if it is already installed, type the following:

	pip install pip
	 
	pip install tensorflow
	 
	pip install numpy
	
	pip install matplotlib
	
	pip install keras



Enjoy!
