# Capstone Final Project- Using Django Python

## The APP:- Dr. Mood

## The Function:- Detect faces and show the expression chart!

This application uses Google vision API where you can analyze faces in a picture. This API gives the response back in a Json file which I am using to draw a polygon around the faces found and I have picked up few emotions from the response Json file like ‘JoyLikelyhood’,” SorrowLikelihood’, “SurpriseLikeHood’ and ‘AngerLikeHood’. To display these emotions, I have drawn a pie-chart which shows how happy you are and so on. There are chances where API is not able to detect any face due to very bad resolution or any other reason, I have a default image for that situation and a default chart so that it does not break the application.

## Requirements

The code is written using Python version 3.4 and Django 1.10.3. The API is a google API and you need a google API key to run this program. I have used PIL module to draw the polygon around the detected faces and I have used MATPLOTLIB to draw the chart. I also used PIL to stitch the charts together if there are more than one face.

## Known issues
I am not sure but the API does not detect all the faces and can break the code. Though I have done some error handling, it can still break the code as the image format dependencies are yet unknown. Needs more testing’s and error handlings.

• One bug I found out yesterday that if the uploaded picture has a resolution more than 720*600, the chart displays the labels twice/thrice. 


## Future development
•	I have installed Simple CV and Open CV to use a live camera to take the picture and upload the pic from there but here is some issue while importing it. Need to fix that.


•	I need to test the application more to see where it fails and fix the issue. I am sure it’s not 100 % robust right now.


•	I want to figure out a way so that I can display as many as charts I want so that people can see it. Right now it’s coded in such a way that it displays only 4 charts or else it would appear so small that the user will not be able to see the data on chart.


• Last but not the least, I want to use my Raspberry -pi to use the camera and send the pic to the Django server.
