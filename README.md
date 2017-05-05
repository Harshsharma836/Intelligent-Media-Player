# Intelligent Media Player
Have you ever thought that if you are watching a movie and as soon as you look away for some reason like someone called you or fetching a glass of water for yourself, the computer understands it and the movie pauses by itself? This project helps you to achieve it. Intelligent media player is developed for Linux based system and uses haar casade from Open CV to detect face position and control the media player (VLC Media Player)  accordingly. If the user is seeing the screen the media plays but as soon as the user changes his face position  ( looks away from the screen ) the media player pauses and waits until the user see's back to the screen. 

## Packages and software required to run the application
  1. Python 2
  2. Open CV 
  3. vlc-ctrl
  4. VLC Media player
  
## Future vision of the project 
 This project can be further enhanced to detect the eye movement and control the media player according to the gestures. 

## Links to the packages and method to install vlc-ctrl
  
  1) This has a detailed procedure for instaling Open CV in Linux
    * http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html
    
  2) Installing vlc-ctrl packagae for linux using pip install
    * pip2 install vlc-ctrl ( If you have both python2 and python3 installed )
    * pip install vlc-ctrl ( If you have only python2 installed )
   
  3) I have used Python 2 because I had insalled opencv in it.
  
  4) Any VLC Media player is fine for running the application just make sure that it is not too outdated. 
  
  5) You can get the haar cascade classifier from the link https://github.com/opencv/opencv/tree/master/data/haarcascades
    
## This is how I did it

  Here I have used frontal face classifier to detect the face of the person who is watching a media player. If the person is having his/her face position in front then using this particular classifier which is trained to detect only frontal faces lets the video to play continuesly but as soon he face position is not facing front to the screen then clasifier is unable to detect the face hence it pauses the video. 
  
 ## Restrications of the developed application
 
  * This system is developed only for linux based systems.
  * You should put your video which you want to play in the folder assigned by me.
  * Must download a shell file which will be running in background for checking if you have clicked VLC Media player. 
  * Works only for VLC Media player. 
  * The lighting of the room and camera resolution effects the program. 

#### NOTE: You have to change the path to which the video is contained in the code. *Happy Coding*!!!!
