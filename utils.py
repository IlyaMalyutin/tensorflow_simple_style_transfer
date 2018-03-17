import PIL
import io
import urllib

def download_image(url):
    """
    url -> PIL.Image
    """
    response = urllib.request.urlopen(url)
    return PIL.Image.open(io.BytesIO(urllib.request.urlopen(url).read()))
    