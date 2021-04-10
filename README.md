# KaushalJadhav-CV-Workshop-Task-2
P.S.-Making a whiteboard using the ball in the user’s hand as a pen pointer to write  on air and perform various functions  such as deletion and clear screen.
<br>Following is the youtube video demonstration link for the task-https://youtu.be/DzGZApHaiWs
<br>This task is developed using OpenCV-Python(Python Version- 3.6.9 OpenCV Version-4.5.1).
The code is written to track the direction of movement of ball which is an object here.The ball is moved in front of webcam by the user.The computer screen displays the track traversed by the ball while moving. The code comprises of- 
<br>1)Frame extraction from the video. 
<br>2)Color based image segmentation to detect the ball.
<br>3)Finding the contour with maximum area.
<br>4)Plotting the mean position of all pixels in the contour with maximum area to display the track of object.
<br>5) Options are also made available to clear the screen by deleting the track completely, to delete desired part of the track etc.
