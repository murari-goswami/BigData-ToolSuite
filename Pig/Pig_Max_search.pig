$ hadoop fs -mkdir /user/cloudera/class5/input/ip_history/
$ hadoop fs -put /home/cloudera/class5/input-data/ip_history.txt /user/cloudera/class5/input/ip_history
$ pig -x mapreduce
2014-09-14 06:38:30,761 [main] INFO  org.apache.pig.Main - Logging error messages to: /home/cloudera/pig_1410701910760.log
2014-09-14 06:38:30,990 [main] INFO  org.apache.pig.backend.hadoop.executionengine.HExecutionEngine - Connecting to hadoop file system at: hdfs://localhost:8020
2014-09-14 06:38:31,188 [main] INFO  org.apache.pig.backend.hadoop.executionengine.HExecutionEngine - Connecting to map-reduce job tracker at: localhost:8021
grunt> REL_IP_HISTORY = LOAD '/user/cloudera/class5/input/ip_history/ip_history.txt' using PigStorage(',')as (ip_add : chararray, date : chararray);
grunt> STORE REL_IP_HISTORY into '/user/cloudera/class5/pig/ip_history/' using PigStorage(',');
grunt > A = GROUP REL_IP_HISTORY by ip_add;
grunt> B = FOREACH A generate FLATTEN(group), COUNT(REL_IP_HISTORY) as Count;
grunt> C = ORDER B by Count DESC;
grunt> DUMP C
grunt > STORE C into '/user/cloudera/class5/pig/ip_history/Counted_result.txt' using PigStorage(',');
grunt > RES = LIMIT C 5;
grunt > STORE RES into '/user/cloudera/class5/pig/ip_history/Top_5_IP.txt' using PigStorage(',');
