The code given uses python 3.11. All the external libraraies are there in requirements.txt.
You have to go to notebooks/main_driver.ipynb and run it. Please go through comments and markdowns to understand the code better.

Few details of code and experiment design:
We are using different range of nonce for different experiments. This has been done to make sure, not all the nodes are able to propose blocks. Also, make sure some blocks are able to propose blocks. This also enables us to do the experiment without other issues like taking too much time.
For experiment 1 (different n(s)), we are limiting it to 2^16
For experiment 2 (different k(s)), the upper limit is 2^32.


The repo mainly has four folders.
    1. inputs - folder containing the input file used to ruin the program in PART1.
    2. outputs - all the outputs generated in varuious runs are stored here including output.txt
    3. src - folder containing the classes and methods to be used while proposing block and generating the plots.
    4. notebooks - folder containing driver program to run all the experiment asked in the assignment.


NOTE: The assignment code has been divided in 3 parts. 
Below are the details: 

Briefly, 
PART 1: This part runs the code for fixed values of n, m, k given in the input.txt file. Logs the output in the required format in the output.txt file in the outputs folder. For this, nonce < 2^16.

PART 2:
    PART 2.a: Here, we run experiment where we are changing the value of n, keeping m and k fixed. 
            Effects on the block proposers are shown in the report. Plots and observationd are there in the notebook also. For this nonce < 2^16.
            All the logs  are stored in part2a_vary_n_op_file*.txt. 
            csv file of part2a_vary_n contains the details of block proposers in table format, to be used for plotting.

    PART 2.b: Here, we run the experiment whwere we are changing the values k, keeping n and m fixed.
            Effects on the block proposers are shown in the report. Plots and observationd are there in the notebook also. For this, nonce < 2^24.
            All the logs  are stored in part2b_vary_k_op_file*.txt. 
            csv file of part2b_vary_k*.csv contains the details of block proposers in table format, to be used for plotting.

In the notebook also, you will find details to understand the code better. 

I hope this helps, if there is any doubt, feel free to reach out to me via email cs21mds14002@iith.ac.in.
