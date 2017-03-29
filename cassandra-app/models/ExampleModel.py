import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


# Define a model using the cqlengine types
class ExampleModel(Model):
    id          = columns.TimeUUID(primary_key=True, default=uuid.uuid1)
    type        = columns.Integer(index=True)
    created_at  = columns.DateTime()
    description = columns.Text(required=False)
