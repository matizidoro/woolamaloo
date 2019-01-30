# Woolamaloo University 

## Getting Started

Hi there! This repository answers the Woolamaloo University test used to assess students knowledge for an internship at CMC.
Before running this project, you will need to have the steps below done.   

## Step-by-step

 - If you want to use an IDE like PyCharm or another one, since it runs Python 3.6.x, clone this repository, install both  pandas and numpy packages then run script.py.
 - However, if you use an Linux/Ubuntu based OS and want to run it from the terminal you can do the following:
 
    - Make sure that you have Python 3.6.x installed;
    ```
      python3 --version
    ```
    - Install pip with the command:
    ```
      sudo apt install python3-pip
    ```
    - Now, you got to install virtualenv:
    ```
      sudo pip3 install virtualenv
    ```
    - Navigate to the repository project folder and create a virtual environment:
    ```  
      virtualenv venv
    ```
    - Activate the virtual environment with:
    ```
      source venv/bin/activate
    ```
    - Install and upgrade the necessary packages:
    ```
      pip3 install --upgrade numpy
      pip3 install --upgrade pandas
    ```
    - Then run script.py:
    ```  
      python3 script.py
    ```
