'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_vertex_shader'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_shader',False)
_p.unpack_constants( """GL_VERTEX_SHADER_ARB 0x8B31
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB 0x8B4A
GL_MAX_VARYING_FLOATS_ARB 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB 0x8B4D
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB 0x8B89
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB 0x8B8A""", globals())
glget.addGLGetConstant( GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB, (1,) )
glget.addGLGetConstant( GL_MAX_VARYING_FLOATS_ARB, (1,) )
glget.addGLGetConstant( GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB, (1,) )
glget.addGLGetConstant( GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB, (1,) )
@_f
@_p.types(None,_cs.GLhandleARB,_cs.GLuint,arrays.GLcharARBArray)
def glBindAttribLocationARB( programObj,index,name ):pass
@_f
@_p.types(None,_cs.GLhandleARB,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLintArray,arrays.GLuintArray,arrays.GLcharARBArray)
def glGetActiveAttribARB( programObj,index,maxLength,length,size,type,name ):pass
@_f
@_p.types(_cs.GLint,_cs.GLhandleARB,arrays.GLcharARBArray)
def glGetAttribLocationARB( programObj,name ):pass


def glInitVertexShaderARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
