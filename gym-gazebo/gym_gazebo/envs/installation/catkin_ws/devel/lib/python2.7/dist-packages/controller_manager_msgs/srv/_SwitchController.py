# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from controller_manager_msgs/SwitchControllerRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SwitchControllerRequest(genpy.Message):
  _md5sum = "36d99a977432b71d4bf16ce5847949d7"
  _type = "controller_manager_msgs/SwitchControllerRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# The SwitchController service allows you stop a number of controllers
# and start a number of controllers, all in one single timestep of the
# controller_manager control loop.

# To switch controllers, specify
#  * the list of controller names to start,
#  * the list of controller names to stop, and
#  * the strictness (BEST_EFFORT or STRICT)
#    * STRICT means that switching will fail if anything goes wrong (an invalid
#      controller name, a controller that failed to start, etc. )
#    * BEST_EFFORT means that even when something goes wrong with on controller,
#      the service will still try to start/stop the remaining controllers
#  * start the controllers as soon as their hardware dependencies are ready, will
#    wait for all interfaces to be ready otherwise
#  * the timeout in seconds before aborting pending controllers. Zero for infinite

# The return value "ok" indicates if the controllers were switched
# successfully or not.  The meaning of success depends on the
# specified strictness.


string[] start_controllers
string[] stop_controllers
int32 strictness
int32 BEST_EFFORT=1
int32 STRICT=2
bool start_asap
float64 timeout
"""
  # Pseudo-constants
  BEST_EFFORT = 1
  STRICT = 2

  __slots__ = ['start_controllers','stop_controllers','strictness','start_asap','timeout']
  _slot_types = ['string[]','string[]','int32','bool','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       start_controllers,stop_controllers,strictness,start_asap,timeout

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SwitchControllerRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.start_controllers is None:
        self.start_controllers = []
      if self.stop_controllers is None:
        self.stop_controllers = []
      if self.strictness is None:
        self.strictness = 0
      if self.start_asap is None:
        self.start_asap = False
      if self.timeout is None:
        self.timeout = 0.
    else:
      self.start_controllers = []
      self.stop_controllers = []
      self.strictness = 0
      self.start_asap = False
      self.timeout = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.start_controllers)
      buff.write(_struct_I.pack(length))
      for val1 in self.start_controllers:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.stop_controllers)
      buff.write(_struct_I.pack(length))
      for val1 in self.stop_controllers:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self
      buff.write(_get_struct_iBd().pack(_x.strictness, _x.start_asap, _x.timeout))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.start_controllers = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.start_controllers.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.stop_controllers = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.stop_controllers.append(val1)
      _x = self
      start = end
      end += 13
      (_x.strictness, _x.start_asap, _x.timeout,) = _get_struct_iBd().unpack(str[start:end])
      self.start_asap = bool(self.start_asap)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.start_controllers)
      buff.write(_struct_I.pack(length))
      for val1 in self.start_controllers:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      length = len(self.stop_controllers)
      buff.write(_struct_I.pack(length))
      for val1 in self.stop_controllers:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.Struct('<I%ss'%length).pack(length, val1))
      _x = self
      buff.write(_get_struct_iBd().pack(_x.strictness, _x.start_asap, _x.timeout))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.start_controllers = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.start_controllers.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.stop_controllers = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1 = str[start:end]
        self.stop_controllers.append(val1)
      _x = self
      start = end
      end += 13
      (_x.strictness, _x.start_asap, _x.timeout,) = _get_struct_iBd().unpack(str[start:end])
      self.start_asap = bool(self.start_asap)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_iBd = None
def _get_struct_iBd():
    global _struct_iBd
    if _struct_iBd is None:
        _struct_iBd = struct.Struct("<iBd")
    return _struct_iBd
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from controller_manager_msgs/SwitchControllerResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SwitchControllerResponse(genpy.Message):
  _md5sum = "6f6da3883749771fac40d6deb24a8c02"
  _type = "controller_manager_msgs/SwitchControllerResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool ok

"""
  __slots__ = ['ok']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SwitchControllerResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
    else:
      self.ok = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ok
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _get_struct_B().unpack(str[start:end])
      self.ok = bool(self.ok)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SwitchController(object):
  _type          = 'controller_manager_msgs/SwitchController'
  _md5sum = 'b29a7abc673b2c54c14b54e50f8d06a5'
  _request_class  = SwitchControllerRequest
  _response_class = SwitchControllerResponse