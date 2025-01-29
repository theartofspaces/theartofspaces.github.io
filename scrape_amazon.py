import requests
from PIL import Image
from io import BytesIO
import time

def save_img(url, name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.amazon.com/'
    }
    
    # Convert WebP URL to JPG URL by modifying the URL parameters
    url = url.replace('_FMwebp', '').replace('.webp', '.jpg')
    if '_SX300_SY300' in url:
        url = url.replace('_SX300_SY300', '_SL1500')
    
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        i = Image.open(BytesIO(response.content))
        i.save(f'{name}.png', 'PNG')
        print(f"Saved image: {name}.png")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

# Direct image URLs from Amazon's media server
images = [
    {
        "url": "https://m.media-amazon.com/images/I/71YHdsPKXBL._AC_SL1500_.jpg",
        "name": "Gold Framed Landscape Wall Art"
    },
    {
        "url": "https://m.media-amazon.com/images/I/81J5kf1mSQL._AC_SL1500_.jpg",
        "name": "Cotton Knitted Round Pouf"
    }
]

for img in images:
    print(f"\nProcessing {img['name']}...")
    if save_img(img['url'], img['name']):
        print(f"Successfully processed {img['name']}")
    else:
        print(f"Failed to process {img['name']}")
    time.sleep(2) 