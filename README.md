#Improve Test Results by Piloting
*How to Simulate Field Data in the Lab

-------

A Python program to simulate process traces for process mining techniques using Markov-styled transitions

####Overview

The code blends the directionality of the process mining footprint with the stochastic nature of Markov models and state transition probabilities. Code of this type was used to simulate a pilot study to help a team plan for a testing event. The team had no access to field data and no resources to conduct a formal pilot event prior to the main test. Recognizing the inherent risks of entering a test “cold”, the team innovated a technique to develop a synthetic dataset for use as if it were actual field data. The project focused on testing standard operating procedures that are process-oriented, which require the careful completion of a series of activities to attain a desired end state. The code is based on this Pseudocode formulation [Code base](process_sim.py):

```
INIT Traces to empty list
SET Paths equal footprints possible in Markov transition state matrix
SET Probabilities equal probability for each state transition
SET Start to A
SET End to P
SET Event to Start
SET Replication to number of simulated traces desired
FOR 1 to Replication size
INIT Trace to empty list
STORE first element of Trace as Start
		WHILE Event NOT EQUAL End
			OBTAIN Event as randomly drawn element from Paths
			APPEND Event to Trace
ENDWHILE
COMPUTE string transformation of list Trace
APPEND Trace to Traces
SET Event to Start
ENDFOR
COMPUTE frequency of each occurrence of Traces
WRITE list of frequencies to file
```

The code is part of a larger project explained in the paper entitled _Improve Test Results by Piloting: How to Simulate Field Data in the Lab_ presented during the [MODSIM 2016 World Conference](http://www.modsimworld.org/). The full paper is freely available at the conference's published [online proceedings](http://www.modsimworld.org/papers/2016/How_to_Simulate_Field_Data_in_the_Lab.pdf). The value of this project is in the innovations, approaches, and results that are extensible to other process-centric tests or studies.

####About the Paper's Authors

__Jay Gendron__ is a data scientist with Booz Allen Hamilton. He is a business leader, artist, and author who writes on
perspectives of how good questions and compelling visualization make analytics accessible to decision makers. He
is an award-winning speaker who has presented internationally. Jay volunteers with Code for America - contributing
data science skills to improve civic and municipal access to data. He is the founder of the Meetup [try.Py - Learn
Python](http://www.meetup.com/tryPy-Learn-Python/). Jay is authoring a book entitled _Introduction to R for Business Intelligence_ due for release this summer by [Packt Publishing](). For additional information, please visit Jay on  [LinkedIn](https://www.linkedin.com/in/jaygendron), [Twitter](@jaygendron), or his [Community Site for Data Science Managers](http://www.datasciencemanagement.com).

__Tammy Crane__ is an aeronautical engineer and operations research systems analyst at SRC. She uses engineering
and data analytics expertise to improve human performance in scenario-based M&S training, electronic warfare, weapons
testing, and wargaming. She often advises decision makers on requirements analysis, project management, and risk
identification. Tammy volunteers with the Society of Women Engineers and endeavors to research: the science and
cognition effects on decision-risk analysis, and advanced experimentation for immersive training environments,
future sensors, and autonomous systems. Connect with Tammy by [LinkedIn](https://www.linkedin.com/in/tammycrane).

__Gerrod Seifert__ is a senior defense research analyst working for Booz Allen Hamilton. He served in the U.S. Navy
as a Surface Warfare Officer. Gerrod is experienced in joint integrated air and missile defense and defense
acquisition operational testing and evaluation. He has an M.S. in Natural Resources (Hydrogeology), and is a
certified Project Management Professional (PMP). Gerrod is pursuing a Ph.D. in Environmental Engineering to
improve water resources. He co-authored the evaluations of drinking water and wastewater assets in the 2016 Report
Card for D.C.’s Infrastructure (American Society of Civil Engineers, 2016).

License
-------
GNU GENERAL PUBLIC LICENSE; Version 2, June 1991
