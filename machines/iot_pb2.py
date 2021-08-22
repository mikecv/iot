# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='iot.proto',
  package='iot',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tiot.proto\x12\x03iot\">\n\x0bRegisterCmd\x12\x1c\n\x03\x63md\x18\x01 \x01(\x0e\x32\x0f.iot.MachineCmd\x12\x11\n\tmachineIP\x18\x02 \x01(\t\"?\n\x0cRegisterResp\x12\"\n\x06status\x18\x01 \x01(\x0e\x32\x12.iot.MachineStatus\x12\x0b\n\x03uID\x18\x02 \x01(\r\".\n\x0bWatchdogCmd\x12\x1f\n\x03\x63md\x18\x01 \x01(\x0e\x32\x12.iot.ControllerCmd\"3\n\x0cWatchdogResp\x12#\n\x06status\x18\x01 \x01(\x0e\x32\x13.iot.ControllerResp*(\n\nMachineCmd\x12\n\n\x06M_NONE\x10\x00\x12\x0e\n\nM_REGISTER\x10\x02*Y\n\rMachineStatus\x12\x0b\n\x07MS_NONE\x10\x00\x12\x0b\n\x07MS_GOOD\x10\x01\x12\x15\n\x11MS_UNEXPECTED_CMD\x10\x62\x12\x17\n\x13MS_SERVER_EXCEPTION\x10\x63*+\n\rControllerCmd\x12\n\n\x06\x43_NONE\x10\x00\x12\x0e\n\nC_WATCHDOG\x10\x01**\n\x0e\x43ontrollerResp\x12\x0b\n\x07\x43S_NONE\x10\x00\x12\x0b\n\x07\x43S_GOOD\x10\x01\x32K\n\x0fMachineMessages\x12\x38\n\x0fRegisterMachine\x12\x10.iot.RegisterCmd\x1a\x11.iot.RegisterResp\"\x00\x32K\n\x12\x43ontrollerMessages\x12\x35\n\x0cKickWatchdog\x12\x10.iot.WatchdogCmd\x1a\x11.iot.WatchdogResp\"\x00\x62\x06proto3'
)

_MACHINECMD = _descriptor.EnumDescriptor(
  name='MachineCmd',
  full_name='iot.MachineCmd',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_REGISTER', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=248,
  serialized_end=288,
)
_sym_db.RegisterEnumDescriptor(_MACHINECMD)

MachineCmd = enum_type_wrapper.EnumTypeWrapper(_MACHINECMD)
_MACHINESTATUS = _descriptor.EnumDescriptor(
  name='MachineStatus',
  full_name='iot.MachineStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MS_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MS_GOOD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MS_UNEXPECTED_CMD', index=2, number=98,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MS_SERVER_EXCEPTION', index=3, number=99,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=290,
  serialized_end=379,
)
_sym_db.RegisterEnumDescriptor(_MACHINESTATUS)

MachineStatus = enum_type_wrapper.EnumTypeWrapper(_MACHINESTATUS)
_CONTROLLERCMD = _descriptor.EnumDescriptor(
  name='ControllerCmd',
  full_name='iot.ControllerCmd',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='C_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='C_WATCHDOG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=381,
  serialized_end=424,
)
_sym_db.RegisterEnumDescriptor(_CONTROLLERCMD)

ControllerCmd = enum_type_wrapper.EnumTypeWrapper(_CONTROLLERCMD)
_CONTROLLERRESP = _descriptor.EnumDescriptor(
  name='ControllerResp',
  full_name='iot.ControllerResp',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CS_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CS_GOOD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=426,
  serialized_end=468,
)
_sym_db.RegisterEnumDescriptor(_CONTROLLERRESP)

ControllerResp = enum_type_wrapper.EnumTypeWrapper(_CONTROLLERRESP)
M_NONE = 0
M_REGISTER = 2
MS_NONE = 0
MS_GOOD = 1
MS_UNEXPECTED_CMD = 98
MS_SERVER_EXCEPTION = 99
C_NONE = 0
C_WATCHDOG = 1
CS_NONE = 0
CS_GOOD = 1



_REGISTERCMD = _descriptor.Descriptor(
  name='RegisterCmd',
  full_name='iot.RegisterCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='iot.RegisterCmd.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='machineIP', full_name='iot.RegisterCmd.machineIP', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=80,
)


_REGISTERRESP = _descriptor.Descriptor(
  name='RegisterResp',
  full_name='iot.RegisterResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='iot.RegisterResp.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uID', full_name='iot.RegisterResp.uID', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=82,
  serialized_end=145,
)


_WATCHDOGCMD = _descriptor.Descriptor(
  name='WatchdogCmd',
  full_name='iot.WatchdogCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='iot.WatchdogCmd.cmd', index=0,
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
  serialized_start=147,
  serialized_end=193,
)


_WATCHDOGRESP = _descriptor.Descriptor(
  name='WatchdogResp',
  full_name='iot.WatchdogResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='iot.WatchdogResp.status', index=0,
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
  serialized_start=195,
  serialized_end=246,
)

_REGISTERCMD.fields_by_name['cmd'].enum_type = _MACHINECMD
_REGISTERRESP.fields_by_name['status'].enum_type = _MACHINESTATUS
_WATCHDOGCMD.fields_by_name['cmd'].enum_type = _CONTROLLERCMD
_WATCHDOGRESP.fields_by_name['status'].enum_type = _CONTROLLERRESP
DESCRIPTOR.message_types_by_name['RegisterCmd'] = _REGISTERCMD
DESCRIPTOR.message_types_by_name['RegisterResp'] = _REGISTERRESP
DESCRIPTOR.message_types_by_name['WatchdogCmd'] = _WATCHDOGCMD
DESCRIPTOR.message_types_by_name['WatchdogResp'] = _WATCHDOGRESP
DESCRIPTOR.enum_types_by_name['MachineCmd'] = _MACHINECMD
DESCRIPTOR.enum_types_by_name['MachineStatus'] = _MACHINESTATUS
DESCRIPTOR.enum_types_by_name['ControllerCmd'] = _CONTROLLERCMD
DESCRIPTOR.enum_types_by_name['ControllerResp'] = _CONTROLLERRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterCmd = _reflection.GeneratedProtocolMessageType('RegisterCmd', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERCMD,
  '__module__' : 'iot_pb2'
  # @@protoc_insertion_point(class_scope:iot.RegisterCmd)
  })
_sym_db.RegisterMessage(RegisterCmd)

RegisterResp = _reflection.GeneratedProtocolMessageType('RegisterResp', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESP,
  '__module__' : 'iot_pb2'
  # @@protoc_insertion_point(class_scope:iot.RegisterResp)
  })
_sym_db.RegisterMessage(RegisterResp)

WatchdogCmd = _reflection.GeneratedProtocolMessageType('WatchdogCmd', (_message.Message,), {
  'DESCRIPTOR' : _WATCHDOGCMD,
  '__module__' : 'iot_pb2'
  # @@protoc_insertion_point(class_scope:iot.WatchdogCmd)
  })
_sym_db.RegisterMessage(WatchdogCmd)

WatchdogResp = _reflection.GeneratedProtocolMessageType('WatchdogResp', (_message.Message,), {
  'DESCRIPTOR' : _WATCHDOGRESP,
  '__module__' : 'iot_pb2'
  # @@protoc_insertion_point(class_scope:iot.WatchdogResp)
  })
_sym_db.RegisterMessage(WatchdogResp)



_MACHINEMESSAGES = _descriptor.ServiceDescriptor(
  name='MachineMessages',
  full_name='iot.MachineMessages',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=470,
  serialized_end=545,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterMachine',
    full_name='iot.MachineMessages.RegisterMachine',
    index=0,
    containing_service=None,
    input_type=_REGISTERCMD,
    output_type=_REGISTERRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MACHINEMESSAGES)

DESCRIPTOR.services_by_name['MachineMessages'] = _MACHINEMESSAGES


_CONTROLLERMESSAGES = _descriptor.ServiceDescriptor(
  name='ControllerMessages',
  full_name='iot.ControllerMessages',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=547,
  serialized_end=622,
  methods=[
  _descriptor.MethodDescriptor(
    name='KickWatchdog',
    full_name='iot.ControllerMessages.KickWatchdog',
    index=0,
    containing_service=None,
    input_type=_WATCHDOGCMD,
    output_type=_WATCHDOGRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLLERMESSAGES)

DESCRIPTOR.services_by_name['ControllerMessages'] = _CONTROLLERMESSAGES

# @@protoc_insertion_point(module_scope)
