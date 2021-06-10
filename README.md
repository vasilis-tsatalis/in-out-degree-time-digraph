# in-out-degree-time-digraph
Find the in or out Degree on a Directed Graph with Map-Reduce

===============================

# RUN Mapper - Reducer local

Quickstart and execution steps
----------

1. $ cd in-out-degree-time-graph
2. $ chmod +x ./mapper.py
3. $ chmod +x ./reducer.py

# Extract and calculate output degree
4. $ python3 mapper.py < ./data/manunited_cont.csv --degree out | sort > ./data/mapper_out_results.csv
5. $ python3 reducer.py < ./data/mapper_out_results.csv  > ./data/reducer_out_results.csv

# Extract and calculate input degree
4. $ python3 mapper.py < ./data/manunited_cont.csv --degree in | sort > ./data/mapper_in_results.csv
5. $ python3 reducer.py < ./data/mapper_in_results.csv  > ./data/reducer_in_results.csv

===============================
