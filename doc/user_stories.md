## Software User Story

Vicky is a researcher interested in intrinsically disordered proteins. She wants this software 
to tell her if the protein she is working with is disordered. She is familiar with protein 
research and is interested in a simple command line interface that would require sequence input and produce 
a clear indication of whether the sequence is predicted to be disordered or not.


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


## Technician User Story
Patrick is a computer science postdoc with graduate-level experience in machine learning. He is 
capable of training the model initially and maintaining the model if a user encounters an error. 
He is also capable of retraining the model if more/better data or better network architectures 
are available.


## Technician Use Case
Technician: Has idea about better machine learning algorithm for prediction tasks.

ML: Has clearly documented code describing where the existing network structure is.

Technician: Edits the code.

ML: Runs tests on the code to make sure it is operable.

Technician: Tells model to train on the dataset.

ML: Access dataset stored on GitHub. Creates a new network which can be saved for future use.
