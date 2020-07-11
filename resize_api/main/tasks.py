from datetime import datetime
from io import BytesIO
from PIL import Image

from django.core.files.base import ContentFile

from resize_api.celery import app
from .models import Resize

@app.task
def resize_image(pk):
    r = Resize.objects.get(pk=pk)
    original_image = Image.open(r.original)
    resized_image = original_image.resize((r.height, r.width), Image.ANTIALIAS)
    resized_io = BytesIO()
    if r.format == 'jpg':
        f = 'jpeg'
        resized_image.save(resized_io, f, quality=100)
    else:
        resized_image.save(resized_io, r.format, quality=100)
    r.result.save(str(datetime.now()) + '.' + r.format, ContentFile(resized_io.getvalue()), save=False)
    r.save()
