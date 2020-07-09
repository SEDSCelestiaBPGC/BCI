# BCI-Bot: 
------------------------------------------------------------------------------------------------

## organization of the directory:

|--- datasets - all the datasets are provided here

|--- Signal acquisition - in this folder, all the schematics of the EEG designs and the EEG visualisation tools and codes are there.

|	|---circuits

|	|	|--- prototype EEG 

|	|	|	|--- DRL_circuit.sch

|	|	|	|--- 

|	|--- visualisation tools 

|	|	|--- plot.py - this file is for the visualisation of the given dataset  


|--- feature extraction - this folder is for processing the data from EEG 

|	|--- training.py - This is an example of training a model with our training data.

|	|--- Models - This is the folder where your training models will stay

|	|	|--- Model01 - This is our first model

|	|	|	|--- training.py - This is script we used to training our first model

|	|	|	|--- analysis.py - This is the script we used to run test and get the confusion matrix

|	|	|	|--- result.jpeg - The resulting confusion matrix


|--- feature translation - this contains all the files for classifying signals


|--- device output - contains the files related to robotics. 

