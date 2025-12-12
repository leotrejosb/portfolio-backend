from rest_framework import renderers

class PassthroughRenderer(renderers.BaseRenderer):
    # --- LA LÍNEA QUE FALTABA Y CAUSABA EL ERROR 500 ---
    media_type = 'application/octet-stream' 
    # ---------------------------------------------------
    format = 'file'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data