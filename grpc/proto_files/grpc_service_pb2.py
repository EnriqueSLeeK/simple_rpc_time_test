# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12grpc_service.proto\"\x1f\n\tint32Data\x12\x12\n\nint32_data\x18\x01 \x01(\x05\"!\n\ndoubleData\x12\x13\n\x0b\x64ouble_data\x18\x01 \x01(\x01\"\xa8\x01\n\x0eint32MultiSend\x12\x11\n\tint32_d_0\x18\x01 \x01(\x05\x12\x11\n\tint32_d_1\x18\x02 \x01(\x05\x12\x11\n\tint32_d_2\x18\x03 \x01(\x05\x12\x11\n\tint32_d_3\x18\x04 \x01(\x05\x12\x11\n\tint32_d_4\x18\x05 \x01(\x05\x12\x11\n\tint32_d_5\x18\x06 \x01(\x05\x12\x11\n\tint32_d_6\x18\x07 \x01(\x05\x12\x11\n\tint32_d_7\x18\x08 \x01(\x05\"!\n\nstringData\x12\x13\n\x0bstring_data\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xdd\x01\n\x0bserviceTest\x12\x1d\n\x0b\x65mptyReturn\x12\x06.Empty\x1a\x06.Empty\x12(\n\x0c\x64oubleReturn\x12\x0b.doubleData\x1a\x0b.doubleData\x12\x34\n\x15int32MultiToOneReturn\x12\x0f.int32MultiSend\x1a\n.int32Data\x12(\n\x0cstringReturn\x12\x0b.stringData\x1a\x0b.stringData\x12%\n\x0bint32Return\x12\n.int32Data\x1a\n.int32Datab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INT32DATA._serialized_start=22
  _INT32DATA._serialized_end=53
  _DOUBLEDATA._serialized_start=55
  _DOUBLEDATA._serialized_end=88
  _INT32MULTISEND._serialized_start=91
  _INT32MULTISEND._serialized_end=259
  _STRINGDATA._serialized_start=261
  _STRINGDATA._serialized_end=294
  _EMPTY._serialized_start=296
  _EMPTY._serialized_end=303
  _SERVICETEST._serialized_start=306
  _SERVICETEST._serialized_end=527
# @@protoc_insertion_point(module_scope)