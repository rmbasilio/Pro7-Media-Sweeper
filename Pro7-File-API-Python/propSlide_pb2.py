# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propSlide.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import slide_pb2 as slide__pb2
import effects_pb2 as effects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpropSlide.proto\x12\x07rv.data\x1a\x0bslide.proto\x1a\reffects.proto\"X\n\tPropSlide\x12\"\n\nbase_slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12\'\n\ntransition\x18\x02 \x01(\x0b\x32\x13.rv.data.Transitionb\x06proto3')



_PROPSLIDE = DESCRIPTOR.message_types_by_name['PropSlide']
PropSlide = _reflection.GeneratedProtocolMessageType('PropSlide', (_message.Message,), {
  'DESCRIPTOR' : _PROPSLIDE,
  '__module__' : 'propSlide_pb2'
  # @@protoc_insertion_point(class_scope:rv.data.PropSlide)
  })
_sym_db.RegisterMessage(PropSlide)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROPSLIDE._serialized_start=56
  _PROPSLIDE._serialized_end=144
# @@protoc_insertion_point(module_scope)
