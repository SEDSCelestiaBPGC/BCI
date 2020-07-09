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
