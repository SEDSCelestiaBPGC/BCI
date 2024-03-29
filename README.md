# BCI
## CONTROLLING MOTION OF A ROVER USING BRAIN-COMPUTER INTERFACE
BCI is a computing system that is based on the brain signals that are extracted, analysed then translated into computer commands that are passed through the interface to give the desired output. Intuitively, it can be perceived as a computer that does stuff with a flick of a thought.

A BCI system consists of 4 sequential components:
  
  1) ***Signal acquisition:*** 
  ​is the measurement of brain signals using a particular sensor modality. The signals are amplified to levels suitable for electronic processing (and they may also be subjected to filtering to remove electrical noise or other undesirable signal characteristics). The signals are then digitized and transmitted to a computer.
  
  2) ***Feature extraction:*** 
  is the process of analyzing the digital signals to distinguish relevant signal characteristics (ie, signal features related to the person's intent) from extraneous content and representing them in a compact form suitable for translation into output commands. These features should have strong correlations with the user's intent.
  
  3) ***Feature translation:*** 
  The resulting signal features are then passed to the feature translation algorithm, which converts the features into the appropriate commands for the output device (ie, commands that accomplish the user's intent). For example, a power decrease in a given frequency band could be translated into a forward displacement of an electronic cart. The translation algorithm should be dynamic to accommodate and adapt to spontaneous or learned changes in the signal features and to ensure that the user's possible range of feature values covers the full range of device control.
  
  4) ***Device output:*** 
  The commands from the feature translation algorithm operate the external device, providing functions such as robotic arm operation, motion control in cars, cursor movement, letter selection, and so forth.

These 4 components are controlled by an operating protocol that defines the onset and timing of operation, the details of signal processing, the nature of the device commands, and the oversight of performance.

------------------------------------------------------------------------------------------------------------------------------------------------------------

### Signal acquisition: 

#### Brain Signal Recording Techniques to Control BCI Systems

  - Electrical and magnetic signals
  - Intracortical electrode array
  - Electrocorticography
  - Electroencephalography
  - Magnetoencephalography
  - Metabolic signals
  - Functional magnetic resonance imaging
  - Functional near-infrared imaging

In principle, any type of brain signal could be used for BCI. These include electrical and magnetic signals as well transfer of neurotransmitters. ​We, however, would be using electroencephalography (EEG) to acquire data from the brain. ​EEG has several benefits compared to other imaging techniques or pure behavioral observations. The most central benefit of EEG is its excellent time resolution, that is, it can take hundreds to thousands of snapshots of electrical activity from multiple electrodes within a single second. This renders EEG an ideal technology to study the precise time-course of cognitive and emotional processing underlying behavior.

#### Electroencephalography (EEG):

  #### Neural activation and electrical fields
  
  ​Synaptic transmission triggers the release of neurotransmitters (dopamine, epinephrine, acetylcholine, etc), which can cause a voltage change across the cell membrane. Synaptic activity often generates a subtle electrical field, which is also called a postsynaptic potential (post = behind). Postsynaptic potentials typically last tens to hundreds of milliseconds.
The postsynaptic potential of a single neuron is too tiny to even be noticed. However, whenever the voltage change associated with a postsynaptic potential occurs for a smaller group of neurons (about 1000 or more), the resulting electric field becomes much stronger.
Not all electrical fields generated by the brain are strong enough to spread all the way through tissue, bone and skull towards the scalp surface. Research indicates that it is primarily the synchronized activity of pyramidal neurons in cortical brain regions which can
be measured from the outside (i.e. from EEG devices). Their name stems from the pyramidal/triangular shape of their cell body. This unique orientation of the cells generates an electrical field with a very stable orientation. As a result, the electrical fields are more likely to spread into various directions and cancel out instead of projecting in a stable way towards the scalp surface – even if hundreds of thousands of neurons in these deeper regions show synchronized activity.

**The EEG recording system consists of electrodes, amplifiers, A/D converter, and a recording device. The electrodes acquire the signal from the scalp, the amplifiers process the analog signal to enlarge the amplitude of the EEG signals so that the A/D converter can digitalize the signal in a more accurate way. Finally, the recording device, which may be a personal computer or similar, stores, and displays the data.**

------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Feature extraction: 

***Different thinking activities result in different patterns of brain signals.*** 
 BCI is seen as a pattern recognition system that classifies each pattern into a class according to its features. BCI extracts some features from brain signals that reflect similarities to a certain class as well as differences from the rest of the classes. The features are measured or derived from the properties of the signals which contain the discriminative information needed to distinguish their different types.
 
 ***The design of a suitable set of features is a challenging issue.***
 ​The information of interest in brain signals is hidden in a highly noisy environment, and brain signals comprise a large
number of simultaneous sources. A signal that may be of interest could be overlapped in time and space by multiple signals from different brain tasks. For that reason, in many cases, it is not enough to use simple methods such as a band pass filter to extract the desired band power.

***Brain signals are inherently non-stationary.*** 
Time information about when a certain feature occurs should be obtained. Our adaptive approach of using support vector machines(SVM) for segmenting the signals from multiple electrodes into a scatter plot then determining which group of signals represent what feature is a commonly used novel approach in BCIs. But before classification of these ever changing signals, it is compulsory to exterminate any unwanted information signals such as noise which occurs due to eye movements, muscle contractions, blood flow, transfer of neurotransmitters. They are minute, generally, but can become significant in some environments. Such unwanted signals can be removed using both linear ( such as band-pass filters) and non-linear filtration techniques.

### Datasets to use for training

[**1. Left/Right Hand MI (subject 1)**](https://drive.google.com/drive/folders/19MpbN892wGTjioDRvq2qjnbEIwsujywR)

**If you're using colab, then you can download this data directly to your colab session storage. The script for this is in the Datasets directory.**

**Description:** This contains Motor Imagery data of the left and right hand of a subject.
Each of the npy files is of the shape `(99,64,3584)`. These are 99 trials, each consisting of 64 channels of eeg data recorded at sampling rate of 512 Hz.

This is only a part of the original published data, where a total of 52 subjects were studied. Various mental tasks were recorded in EEG (Motor Imagery data is only one of the tasks). The complete dataset can be found [here](http://gigadb.org/dataset/view/id/100295). **An in-depth description of the data is provided in the [accompanying article](https://academic.oup.com/gigascience/article/6/7/gix034/3796323).**

### Output Decive
*The rover we are using is a simple wheeled cart that has a robotic pincer which can open, close, or rotate.* 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Add-ons: 

- To make our project more engaging and innovative, we planned to design our own EEG with at least 4 channels in probably the most crude way possible. And to design its schematics, we planned to use Eagle software by Autodesk.
