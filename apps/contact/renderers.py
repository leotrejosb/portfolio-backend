# apps/contact/renderers.py

from rest_framework.renderers import BaseRenderer

class PassthroughRenderer(BaseRenderer):
    """
    Renderer that simply returns the data stream as-is.
    Used for Django's FileResponse.
    """
    media_type = '*/*'
    format = None
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data