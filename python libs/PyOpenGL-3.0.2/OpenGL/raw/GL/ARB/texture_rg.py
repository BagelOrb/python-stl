'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_ARB_texture_rg'
_p.unpack_constants( """GL_RG 0x8227
GL_RG_INTEGER 0x8228
GL_R8 0x8229
GL_R16 0x822A
GL_RG8 0x822B
GL_RG16 0x822C
GL_R16F 0x822D
GL_R32F 0x822E
GL_RG16F 0x822F
GL_RG32F 0x8230
GL_R8I 0x8231
GL_R8UI 0x8232
GL_R16I 0x8233
GL_R16UI 0x8234
GL_R32I 0x8235
GL_R32UI 0x8236
GL_RG8I 0x8237
GL_RG8UI 0x8238
GL_RG16I 0x8239
GL_RG16UI 0x823A
GL_RG32I 0x823B
GL_RG32UI 0x823C""", globals())


def glInitTextureRgARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )