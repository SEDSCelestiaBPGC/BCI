# BCI-Bot: 
------------------------------------------------------------------------------------------------

## organization of the directory:
```
|--- datasets - all the datasets are provided here

|--- Signal acquisition - in this folder, all the schematics of the EEG designs and the EEG visualisation tools and codes are there.
|	|---circuits
|	|	|--- prototype EEG components - all the component circuits needed in the construction of an EEG is here.
|	|	|	|--- DRL_circuit.sch
|	|	|	|--- RFI_filter.sch
|	|	|	|--- Instrumentation_Amplifier.sch
|	|	|	|--- Variable_amp_circut.sch
|	|	|	|--- HighPassFilter.sch
|	|	|	|--- LowPassFilter.sch
|	|	|	|--- CMR_circut.sch
|	|	|	|--- Buffer_circuit.sch
|	|	|	|--- Clamp_circuit.sch
|	|	|	|--- REF_circuit.sch
|	|	|	|--- analogue_digital_convert.sch
|	|	|	|--- IsolateCircuit.sch
|	|	|	|--- ProtectionCircuit.sch
|	|	|--- complete EEG circuit diagram
|	|	|	|--- EEG_circuit.sch - this file has the circuit design for a single channel EEG circuit
|	|	|	|--- EEG.pcb - this file contains the compiled EEG biosensing board with at least 8 channels. 
|	|--- visualisation tools 
|	|	|--- plot.py - this file is for the visualisation of the given dataset 

|--- feature extraction - this folder is for processing the data from EEG 
|	|--- training.py - This is an example of training a model with our training data.
|	|--- Models - This is the folder where your training models will stay
|	|	|--- Model01 - This is our first model
|	|	|	|--- training.py - This is script we used to training our first model
|	|	|	|--- analysis.py - This is the script we used to run test and get the confusion matrix
|	|	|	|--- result.jpeg - The resulting confusion matrix

|--- feature translation - this contains all the files for classifying signals and arduino programming 

|--- device output - contains the files related to robotics. 
```
---------------------------------------------------------------------------------


## Prerequisits:

- DL/ML and related python libraries (PyTorch, TensorFlow, scipy, sklearn, or some more)
- Basic understanding of BCI and EEG devices
- PCB design using Autodesk Eagle
- understanding of Arduino 
- ROS basics (optional)
- a general idea of time domain circuits. 
- classification algorithms (like CNN, SVM, k-clustering, and so on).
- shell script (UNIX commands)

----------------------------------------------------------------


## Guidlines: 
**Firstly, the project is divided into 3 parts:** 
  1) EEG circuit building
  2) Brain Signal analysis
  3) robotics and controls subsystem  

***You choose any of the parts and start working on it according to the instructions and resources provided.***

---------------------------------------------------------------------------------------------------------------------


## Before making the contributions the following is required to go through:

- This is a must read about general layout of a BCI as a system, EEG channel selection, different signal classification algorithms, etc -  
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3304110/

- Brain Computer Interface w/ Python and OpenBCI. (This will get you familiar with using DL models on EEG signals.) 
https://www.youtube.com/playlist?list=PLQVvvaa0QuDeU-QCAwZl2UmSpfb4sWbxY 

- Deep learning for electroencephalogram (EEG) classification tasks: a review (This has in-depth analysis of DL techniques people have used so far) https://iopscience.iop.org/article/10.1088/1741-2552/ab0ab5
 






































