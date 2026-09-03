import re

romance_photos = [
    "1-20260627-210208-dtmtckm34vbvc1fy.jpg",
    "1-20260627-210720-jxh3p8rg3di8uzzu.jpg",
    "4-20260627-210208-dtmtckm34vbvc1fyl2a07OdG.jpg",
    "4-20260627-210208-dtmtckm34vbvc1fyx295CU3C.jpg",
    "4-20260627-210720-jxh3p8rg3di8uzzu0JkynbUz.jpg",
    "4-20260627-210720-jxh3p8rg3di8uzzueLzusGBE.jpg",
    "4-20260627-210720-jxh3p8rg3di8uzzuOQngPvQz.jpg",
    "4-20260627-210720-jxh3p8rg3di8uzzuwjlKI30y.jpg",
    "IMG-20260713-WA0023.jpg"
]

random_photos = [
    "IMG_0748.jpg", "IMG_0749.jpg", "IMG_0750.jpg", "IMG_0751.jpg",
    "IMG_0752.jpg", "IMG_0753.jpg", "IMG_0754.jpg", "IMG_0755.jpg",
    "IMG_0756.jpg", "IMG_0757.jpg", "IMG_0758.jpg", "IMG_0759.jpg"
]

romance_html = ""
for i in range(3):
    romance_html += '                    <div style="position: relative; width: 100%; height: 33.333%;">\\n'
    # Vase 1 (Left)
    romance_html += f'                        <img src="photo/photobooth/{romance_photos[i*3]}" style="position: absolute; left: 17.8%; top: 63.9%; width: 20.2%; height: 23.2%; transform: translate(-50%, -50%); object-fit: cover; border-radius: 4px; box-shadow: inset 0 0 10px rgba(0,0,0,0.5);">\\n'
    # Vase 2 (Middle)
    romance_html += f'                        <img src="photo/photobooth/{romance_photos[i*3+1]}" style="position: absolute; left: 48.4%; top: 45.7%; width: 23.5%; height: 27.1%; transform: translate(-50%, -50%); object-fit: cover; border-radius: 4px; box-shadow: inset 0 0 10px rgba(0,0,0,0.5);">\\n'
    # Vase 3 (Right)
    romance_html += f'                        <img src="photo/photobooth/{romance_photos[i*3+2]}" style="position: absolute; left: 79.1%; top: 63.9%; width: 20.2%; height: 23.2%; transform: translate(-50%, -50%); object-fit: cover; border-radius: 4px; box-shadow: inset 0 0 10px rgba(0,0,0,0.5);">\\n'
    romance_html += '                    </div>\\n'


random_html = ""
for i in range(3):
    random_html += '                    <div style="position: relative; width: 100%; height: 33.333%;">\\n'
    # Scroll 1
    random_html += f'                        <img src="photo/photobooth/{random_photos[i*4]}" style="position: absolute; left: 21%; top: 38%; width: 18%; height: 20%; transform: translate(-50%, -50%) rotate(-12deg); object-fit: cover; opacity: 0.9;">\\n'
    # Scroll 2
    random_html += f'                        <img src="photo/photobooth/{random_photos[i*4+1]}" style="position: absolute; left: 43%; top: 48%; width: 18%; height: 20%; transform: translate(-50%, -50%) rotate(5deg); object-fit: cover; opacity: 0.9;">\\n'
    # Scroll 3
    random_html += f'                        <img src="photo/photobooth/{random_photos[i*4+2]}" style="position: absolute; left: 24%; top: 67%; width: 18%; height: 20%; transform: translate(-50%, -50%) rotate(-8deg); object-fit: cover; opacity: 0.9;">\\n'
    # Scroll 4
    random_html += f'                        <img src="photo/photobooth/{random_photos[i*4+3]}" style="position: absolute; left: 62%; top: 63%; width: 18%; height: 20%; transform: translate(-50%, -50%) rotate(10deg); object-fit: cover; opacity: 0.9;">\\n'
    random_html += '                    </div>\\n'

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace empty Random view
html = html.replace(
    '<div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;"></div>',
    f'<div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;">\\n{random_html}                </div>'
)

# Replace empty Romance view
html = html.replace(
    '<div id="view-gallery-romance" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;"></div>',
    f'<div id="view-gallery-romance" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;">\\n{romance_html}                </div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
