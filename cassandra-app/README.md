# Skeletal App with Cassandra back-end

This example was created on Ubuntu `14.04` using Python `2.7` and Cassandra `3.7`

Cassandra `3.7` should be [installed](https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04) globally, which requirements Java version `8` (current) or above.

Set up and activate a virtual environment 
 - `virtualenv venv`
 - `source venv/bin/activate`

`virtualenv` may first need to be installed using `pip install virtualenv`.

When in the `venv`, as denoted by `(venv)` in the terminal screen, install the required packages
 - `pip install -f requirements.txt`

Try to access `cqlsh` in the virtual environment by typing `cqlsh` into the terminal. `venv/bin/cqlsh` may have to be edited to set the supported CQL version (the `CQLVER` parameter).

`cqlsh` should only show some configuration and metadata keyspaces.  Run `python run.py` and query `cqlsh` again with 

`SELECT * FROM test.example_model`

to see the data the app pushes into the database.
