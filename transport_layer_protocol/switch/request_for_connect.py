from protobuf3.message import Message
from protobuf3.fields import StringField


class request_for_connect(Message):
    pass

request_for_connect.add_field('ua', StringField(field_number=1, optional=True))
request_for_connect.add_field('pubkey', StringField(field_number=2, optional=True))
