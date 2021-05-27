# in-out-degree-time-digraph
Find the in and out Degree on a Directed Graph with Map-Reduce

===============================

# RUN Mapper local - test data
$ python3 mapper.py < ./data/manunited_cont_test.csv | sort
$ python3 mapper.py <  ./data/manunited_cont_test.csv | sort > ./data/mapper_results_test.csv

# RUN Reducer local - test data
$ python3 reducer.py < ./data/mapper_results_test.csv
$ python3 reducer.py < ./data/mapper_results_test.csv  > ./data/reducer_results_test.csv

===============================

# RUN Mapper local
$ python3 mapper.py < ./data/manunited_cont.csv | sort
$ python3 mapper.py <  ./data/manunited_cont.csv | sort > ./data/mapper_results.csv

# RUN Reducer local
$ python3 reducer.py < ./data/mapper_results.csv
$ python3 reducer.py < ./data/mapper_results.csv  > ./data/reducer_results.csv

===============================

