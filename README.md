# Woolamaloo University 

## Getting Started

Hi there! This repository answers the Woolamaloo University test used to assess students knowledge for an internship at CMC.
Before running this project, you will need to have the steps below done.   

## Prerequisites

 - First of all, you'll want to have MySQL installed on your machine. For such, considering that you're using a Linux OS version, run the following: 
```
 $ sudo apt install mysql-server
```
  You can check if everything worked fine running the following:
```
 $ systemctl status mysql.service
```
  You'll see something like that if everything is right:
```
 ● mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: en
   Active: active (running) since Wed 2018-04-23 21:21:25 UTC; 30min ago
 Main PID: 3754 (mysqld)
    Tasks: 28
   Memory: 142.3M
      CPU: 1.994s
   CGroup: /system.slice/mysql.service
           └─3754 /usr/sbin/mysqld
``` 
