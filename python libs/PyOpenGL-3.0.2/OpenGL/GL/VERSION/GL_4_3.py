'''OpenGL extension VERSION.GL_4_3

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_4_3 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_4_3.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_4_3 import *
### END AUTOGENERATED SECTION

from OpenGL.GL.ARB.arrays_of_arrays import *
from OpenGL.GL.ARB.fragment_layer_viewport import *
from OpenGL.GL.ARB.shader_image_size import *
from OpenGL.GL.ARB.ES3_compatibility import *
from OpenGL.GL.ARB.clear_buffer_object import *
from OpenGL.GL.ARB.compute_shader import *
from OpenGL.GL.ARB.copy_image import *
from OpenGL.GL.ARB.debug_group import *
from OpenGL.GL.ARB.debug_label import *
from OpenGL.GL.KHR.debug import *
from OpenGL.GL.ARB.debug_output2 import *
from OpenGL.GL.ARB.explicit_uniform_location import *
from OpenGL.GL.ARB.framebuffer_no_attachments import *
from OpenGL.GL.ARB.internalformat_query2 import *
from OpenGL.GL.ARB.invalidate_subdata import *
from OpenGL.GL.ARB.multi_draw_indirect import *
from OpenGL.GL.ARB.program_interface_query import *
from OpenGL.GL.ARB.robust_buffer_access_behavior import *
from OpenGL.GL.ARB.shader_storage_buffer_object import *
from OpenGL.GL.ARB.stencil_texturing import *
from OpenGL.GL.ARB.texture_buffer_range import *
from OpenGL.GL.ARB.texture_query_levels import *
from OpenGL.GL.ARB.texture_storage_multisample import *
from OpenGL.GL.ARB.texture_view import *
from OpenGL.GL.ARB.vertex_attrib_binding import *
