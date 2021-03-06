'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_transform_feedback3'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_transform_feedback3',False)
_p.unpack_constants( """GL_MAX_TRANSFORM_FEEDBACK_BUFFERS 0x8E70
GL_MAX_VERTEX_STREAMS 0x8E71""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glDrawTransformFeedbackStream( mode,id,stream ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBeginQueryIndexed( target,index,id ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEndQueryIndexed( target,index ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetQueryIndexediv( target,index,pname,params ):pass


def glInitTransformFeedback3ARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
