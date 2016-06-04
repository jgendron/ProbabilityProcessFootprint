# ProbabilityProcessFootprint

[Code base](process_sim.py) for work on blending the directionality of the process mining footprint with the stochastic nature of Markov models and state transition probabilities. The code is based on this Pseudocode formulation 

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
