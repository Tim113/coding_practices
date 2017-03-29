# cassandra-spark
Scala Cassandra Spark Connector 

Requires:
  - `spark 2.0.0`
    - Download source code from http://spark.apache.org/downloads.html 
    - `cd` into spark root and build using `./build/mvn -DskipTests clean package`
    - Add spark binaries to path with something like `echo "PATH=$PATH:~/spark-2.0.0/bin" >> ~/.bashrc`
  - `cassandra 3.0+`
    - Get familiar with set up [here](https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-0)
  - `sbt 0.13`
    - Set up and good official documentation found [here](http://www.scala-sbt.org/0.13/docs/Setup.html) 

Built using `sbt`. Run `sbt package` in the project root directory and submit the compiled jar to `spark-submit`. Default Cassandra port should be `9042`. Check firewall options if failure to connect error.

### Set Preparing example Cassandra schema

Create a simple keyspace and table in Cassandra. Run the following statements in cqlsh:

```
CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1 };
CREATE TABLE test.kv(key text PRIMARY KEY, value int);
```

Then insert some example data:

```
INSERT INTO test.kv(key, value) VALUES ('key1', 1);
INSERT INTO test.kv(key, value) VALUES ('key2', 2);
```

### Submit spark job

```
spark-submit \
  --packages com.datastax.spark:spark-cassandra-connector_2.11:2.0.0-M3 \
  --master "local[*]" \
  --class org.snoopy.spark.SparkMeApp \
  target/scala-2.11/hello_2.11-1.0.jar \
  2>/dev/null
```

### Next steps

Dockeriser, running cassandra and spark on the same node
 - https://github.com/clakech/sparkassandra-dockerized

