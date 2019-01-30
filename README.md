# Woolamaloo University 

## Getting Started

Hi there! This repository answers the Woolamaloo University test used to assess students knowledge for an internship at CMC.
Before running this project, you will need to have the steps below done.   

## Step-by-step installation

 - If you want to use an IDE like PyCharm or another one, since it runs Python 3.6.x, clone this repository, install both  pandas and numpy packages then run script.py.
 - However, if you're using an Linux/Ubuntu based OS and want to run it from the terminal you can do the following:
 
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
## During the execution
   - The script only will ask you for the directories of both files (the simplified one - which I considered using .txt - and .csv). If the files are in the same script directory, just insert their names without the extensios, i.e simplified_file, csv_file;
   
## The Script
   - The script consists in importing data from the files, sort them and compare the rows of the imported data.
   
   - Pandas and numpy packages provides data structures responsible for keeping data from files treating the data as well.
   
   - The rows of both files contain  employees's id's, names, admission_date, etc
   
   - After sorting the DataFrame (the structure that holds the data) by the employees's id's we've got to start comparing them
   
   - For such, it's used two iterators with the purpose of scrolling through the DataFrames, that there will be incremented based on lines matchs.
   
   - If a line exists in the system's data and it doesn't on the web data, then the dataframe's iterators are incremented 'till it find out a line match.
   
   - Depending on wich DataFrame has a line that the other doesn't, the script will find out if there are a new employee or a missing one, changing the status.
   
   - If both lines match, the department and positions relocations are searched. This also will change the status.
   
   - There are three auxiliary variables that holds the id's, names and status strings that will be printed in the end of the loop.
