'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_EXT_bgra'
_p.unpack_constants( """GL_BGR_EXT 0x80E0
GL_BGRA_EXT 0x80E1""", globals())


def glInitBgraEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
