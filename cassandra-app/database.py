from cassandra.cqlengine import connection
from cassandra.cqlengine.management import (
    sync_table, create_keyspace_simple)
from datetime import datetime

class CQL(object):

    def __init__(self, app=None):
        self.app = app
        self.cluster = None
        self.session = None
        self.keyspace = None
        if app is not None:
            self.init_app(app)
        # Convienience
        self.create_keyspace_simple = create_keyspace_simple

    def init_app(self, app):
        # Scrape parameters from app as defined by config.py
        self.cluster = app.config['CASSANDRA_HOSTS']
        self.keyspace = app.config['CASSANDRA_KEYSPACE']

    def connect(self, ks=None):
        """
        Create a connection object with the app parameters and set a default
        keyspace to work within.
        The connection either works with a provided keyspace or the default.
        """

        if ks is None:
            # If no keyspace is provided, use the default
            ks = self.keyspace

        # Connection object which can be harvested
        connection.setup(self.cluster, ks, protocol_version=3)
        self.session = connection.session
        # Creates a keyspace with if not exists, then sets it
        self.create_keyspace_simple(ks, 1)
        self.session.set_keyspace(ks)

    def sync_table(self, model):
        """
        Use the native python-cassandra function to sync a cassandra model
        as a table.
        The environment variable CQLENG_ALLOW_SCHEMA_MANAGEMENT must be set True
        """
        sync_table(model)

    def add(self, model):
        # Example to show data is piped into the database
        model.create(type=0, description="example1", created_at=datetime.now())
        model.create(type=0, created_at=datetime.now())
        model.create(type=0, description="example3", created_at=datetime.now())


cdb = CQL()
