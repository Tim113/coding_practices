name := "hello"

version := "1.0"

scalaVersion := "2.11.8"

organization := "org.snoopy"

resolvers ++= Seq(
  "Spark Packages Repo" at "https://dl.bintray.com/spark-packages/maven",
  "Spark Packages Repo sgd" at "https://mvnrepository.com/artifact/com.datastax.spark/spark-cassandra-connector_2.11",
  Resolver.mavenLocal
)

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "2.0.0",
  "org.apache.spark" %% "spark-sql" % "2.0.0",
  "com.datastax.spark" % "spark-cassandra-connector_2.11" % "2.0.0-M3"
)
