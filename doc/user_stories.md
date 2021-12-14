## Software user story

Vicky is a researcher interested in intrinsically disordered proteins. They want this software 
to tell them if the protein they are working with is disordered. They are familiar with protein 
research and are interested in a simple interface that would require sequence input and produce 
clear labels for each region of the sequence.


## Software Use Case: 

User: Goes to website with user interface 

ML: Display "input protein sequence or file containing multiple sequences" with a box for a 
single typed sequence or a button for uploading fasta files

User: Inputs protein sequence into a box or clicks on a button and uploads protein sequence file 
from computer

ML: For each valid input sequence, it first tests to make sure the input sequence is valid.
    If a protein sequence is invalid, displays the input sequence and a message reading "Invalid
    protein sequence." If a protein sequence is valid, the interface displays the original sequence with certain regions of the 
    protein labeled underneath as intrinsically disordered along with an overall percentage of 
    how much of the sequence is intrinsically disordered.

### Functional diagram:
![alt text](https://github.com/Intrinsically-Disordered/main-project/blob/main/doc/images/chart.jpg?raw=True)


## Technician user story
Patrick is a computer science postdoc with graduate-level experience in machine learning. He is 
capable of training the model initially and maintaining the model if a user encounters an error. 
He is also capable of retraining the model if more/better data or better network architectures 
are available.


## Technician use case -- do we need this?
