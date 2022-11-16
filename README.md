
# Correction System for Multiple Choice Question exams

The system applies Computer Vision techniques to carry out the correction process,
 where a continuous stream of exam papers images are entered into the system via the scanner, smartphone camera or laptop
and are sent as input to the system.
 The image processing algorithms perform alignment and segmentation of the exam papers after converting them to gray scale.
In order to discover the important points in the paper (features) and extract the distinctive marks in it (the student's name and ID number - spatially areas of the answer boxes - form number...). 
The OpenCV library were used to discover the content of the image from points that define the corners of the image, 
student numbers and check boxes, in addition to the mark placed on it as a correct answer. 
After identifying the numbers and answers, they are stored in text matrices, and using the Numby library, the students' answers are compared with the correction scale previously entered into the system.
The system provides the ability to export students’ scores as PDF to share with students or CSV that helps in building statistical reports for scores i.e. mean, minimum, maximum, and standard deviation


## Installation

This project files requires Python 3.6 and the following Python libraries installed:

```bash
  sudo apt-get install python3-opencv
  sudo apt-get install python3-pyqt5
  sudo apt-get install python3-numpy
  sudo apt-get install python3-xlrd
```
    
## implemintation

computer vision
It is one of the fields of computer science(Artificial Intelligence) that includes methods of obtaining, processing, analyzing and understanding images, 
and computer vision aims to build applications capable of understanding the content of images as understood by humans, 
with the aim of benefiting from them in various applications. and industrial.



1- When reading the image, it is dealt with at the gray scale. 
   Apply the Bilateral Filter as shown in the following figure because it helps to show the edges well and also helps in increasing the color differences.
   
![App Screenshot](https://github.com/Thaar-Abo-shah/correction-system-for-Multiple-Choice-Question-exams-/blob/main/screen/1.jpg)


2-(threshold) to increase clarity and distinguish between the base color of the paper and the distinguishing marks (the dots fixed on the paper and students' entries).

![App Screenshot](https://github.com/Thaar-Abo-shah/correction-system-for-Multiple-Choice-Question-exams-/blob/main/screen/2.png)

3-(threshold) to increase clarity and distinguish between the base color of the paper and the distinguishing marks (the dots fixed on the paper and students' entries)

4-The four corners of the picture were searched in order to determine the full shape of the paper:
To verify the correctness of the imaging process in the event of the presence of the four angles, by searching in each of these angles with a specific value (pixel 50 * 50) and this value was approved after experimenting with several values, so that if values greater than these values were chosen, part of answers and thus distorting the paper and losing some data

5-(warp perspective) to crop and align the image

6-Convert the image into an array so that it can be used to obtain the required information from the image (the answers and (ID) locations) that are pre-defined on the basic template.

7-The assigned squares are divided as in the paper and the values of (threshold) are counted, in order to compare them with the correction scale and match the correct answers.

## Documentation

I built the application to correct the automated examination papers by performing a scan of the papers and entering them into the system through the graphical interface, with several steps:
1- When you open the application, the main interface appears

2-When you click on the correction button, the following graphic interface appears:
![App Screenshot](https://github.com/Thaar-Abo-shah/correction-system-for-Multiple-Choice-Question-exams-/blob/main/screen/3.jpg)

In this interface, the number of students, the number of questions, the name of the course, the number of grades of correction and the total mark are entered.
When specifying the number of forms, the section for entering correction forms, correction scales, and papers to be corrected is activated, bearing in mind that there are two ways to enter the correction scale:

Reading from an image and inserting the correction scale, knowing that the marks are distributed equally as a default value, with the possibility of modifying these values.

Insert the correction scale as a matrix (the answer with its mark).

3-After entering the entire correction scale, press the correction button to complete the correction process.
![App Screenshot](https://github.com/Thaar-Abo-shah/correction-system-for-Multiple-Choice-Question-exams-/blob/main/screen/4.jpg)

In the previous interface, the correction process appears. It also contains the practical part of the students’ marks and the classification of the students as pass or fail, knowing that the user can enter the practical mark into the system with the student’s name. Students who are not applying, which is approximate to know the number of students who will apply for the next course.
2- The application provides the possibility of knowing the arithmetic mean, standard deviation, the highest mark and the success rate for each subject, after entering the practical grades file.
We can also save the file as excel or pdf or print the results.

## Accuracy, precision, recall

![App Screenshot](https://github.com/Thaar-Abo-shah/correction-system-for-Multiple-Choice-Question-exams-/blob/main/screen/testing.jpg)


## Author

- [Thaar Abo Shah](https://github.com/Thaar-Abo-shah)
