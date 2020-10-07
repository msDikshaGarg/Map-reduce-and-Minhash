# Map-reduce
Upload files in the hdfs system then:  
To run:  
hjs -D mapreduce.job.reduces=1 -file ~/dir/src -mapper "src/mapper.py 5" -file ~/dir/src -reducer "src/reducer.py 5" -input cookbook_text/*.txt -output xyz.out  
This is a simple implementation of map reduce for cookbook.txt.  
The program samples the data from a bigger datas set of recipes in a cookbook.  
The program also detects duplicate recipes using Minhash.
