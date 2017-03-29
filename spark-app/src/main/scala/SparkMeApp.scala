package org.snoopy.spark

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

import com.datastax.spark.connector._


object SparkMeApp {

  def main(args: Array[String]) {
    val conf = new SparkConf()
        .set("spark.cassandra.connection.host", "127.0.0.1")
        // .set("spark.cassandra.connection.port", "9042")
    
    val sc = new SparkContext(conf)

    val rdd = sc.cassandraTable("test", "kv")
    println(rdd.count)
    println(rdd.first)
    println(rdd.map(_.getInt("value")).sum)   

  }
}

// spark-submit --packages com.datastax.spark:spark-cassandra-connector_2.11:2.0.0-M3 --master "local[*]" --class org.snoopy.spark.SparkMeApp target/scala-2.11/hello_2.11-1.0.jar 2>/dev/null
