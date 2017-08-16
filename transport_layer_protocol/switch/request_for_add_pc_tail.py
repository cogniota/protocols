from protobuf3.message import Message
from protobuf3.fields import StringField


class request_for_add_pc_tail(Message):
    pass

request_for_add_pc_tail.add_field('ua', StringField(field_number=1, optional=True))
request_for_add_pc_tail.add_field('encoded_pc_tail', StringField(field_number=2, optional=True))
