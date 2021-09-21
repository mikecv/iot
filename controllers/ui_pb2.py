# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ui.proto',
  package='ui',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08ui.proto\x12\x02ui\"-\n\x13\x43ontrollerStatusCmd\x12\x16\n\x03\x63md\x18\x01 \x01(\x0e\x32\t.ui.UiCmd\"X\n\x14\x43ontrollerStatusResp\x12#\n\x06status\x18\x01 \x01(\x0e\x32\x13.ui.StatusCmdStatus\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t*\'\n\x05UiCmd\x12\n\n\x06U_NONE\x10\x00\x12\x12\n\x0eU_CNTRL_STATUS\x10\x01*[\n\x0fStatusCmdStatus\x12\x0b\n\x07US_NONE\x10\x00\x12\x0b\n\x07US_GOOD\x10\x01\x12\x15\n\x11US_UNEXPECTED_CMD\x10\x62\x12\x17\n\x13US_SERVER_EXCEPTION\x10\x63\x32X\n\nUiMessages\x12J\n\x13GetControllerStatus\x12\x17.ui.ControllerStatusCmd\x1a\x18.ui.ControllerStatusResp\"\x00\x62\x06proto3'
)

_UICMD = _descriptor.EnumDescriptor(
  name='UiCmd',
  full_name='ui.UiCmd',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='U_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='U_CNTRL_STATUS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=192,
)
_sym_db.RegisterEnumDescriptor(_UICMD)

UiCmd = enum_type_wrapper.EnumTypeWrapper(_UICMD)
_STATUSCMDSTATUS = _descriptor.EnumDescriptor(
  name='StatusCmdStatus',
  full_name='ui.StatusCmdStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='US_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US_GOOD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US_UNEXPECTED_CMD', index=2, number=98,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US_SERVER_EXCEPTION', index=3, number=99,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=194,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_STATUSCMDSTATUS)

StatusCmdStatus = enum_type_wrapper.EnumTypeWrapper(_STATUSCMDSTATUS)
U_NONE = 0
U_CNTRL_STATUS = 1
US_NONE = 0
US_GOOD = 1
US_UNEXPECTED_CMD = 98
US_SERVER_EXCEPTION = 99



_CONTROLLERSTATUSCMD = _descriptor.Descriptor(
  name='ControllerStatusCmd',
  full_name='ui.ControllerStatusCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='ui.ControllerStatusCmd.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=61,
)


_CONTROLLERSTATUSRESP = _descriptor.Descriptor(
  name='ControllerStatusResp',
  full_name='ui.ControllerStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ui.ControllerStatusResp.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ui.ControllerStatusResp.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='ui.ControllerStatusResp.state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=151,
)

_CONTROLLERSTATUSCMD.fields_by_name['cmd'].enum_type = _UICMD
_CONTROLLERSTATUSRESP.fields_by_name['status'].enum_type = _STATUSCMDSTATUS
DESCRIPTOR.message_types_by_name['ControllerStatusCmd'] = _CONTROLLERSTATUSCMD
DESCRIPTOR.message_types_by_name['ControllerStatusResp'] = _CONTROLLERSTATUSRESP
DESCRIPTOR.enum_types_by_name['UiCmd'] = _UICMD
DESCRIPTOR.enum_types_by_name['StatusCmdStatus'] = _STATUSCMDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControllerStatusCmd = _reflection.GeneratedProtocolMessageType('ControllerStatusCmd', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLLERSTATUSCMD,
  '__module__' : 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.ControllerStatusCmd)
  })
_sym_db.RegisterMessage(ControllerStatusCmd)

ControllerStatusResp = _reflection.GeneratedProtocolMessageType('ControllerStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLLERSTATUSRESP,
  '__module__' : 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.ControllerStatusResp)
  })
_sym_db.RegisterMessage(ControllerStatusResp)



_UIMESSAGES = _descriptor.ServiceDescriptor(
  name='UiMessages',
  full_name='ui.UiMessages',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=287,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetControllerStatus',
    full_name='ui.UiMessages.GetControllerStatus',
    index=0,
    containing_service=None,
    input_type=_CONTROLLERSTATUSCMD,
    output_type=_CONTROLLERSTATUSRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UIMESSAGES)

DESCRIPTOR.services_by_name['UiMessages'] = _UIMESSAGES

# @@protoc_insertion_point(module_scope)