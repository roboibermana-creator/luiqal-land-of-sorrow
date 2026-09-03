import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('photobooth_images.html', 'r', encoding='utf-8') as f:
    photo_html = f.read()

new_photobooth = f'''
                <!-- GALLERY PHOTOBOOTH -->
                <div id="view-gallery-photobooth" class="view-section hidden" style="position: absolute; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; background: url('gambarpixel/bagian photobooth/background/assets_bg_castle_balcony.png') center/cover no-repeat;">
                    <div style="width: 90%; height: 90%; overflow-y: auto; padding: 2vw; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2vw; background: rgba(0,0,0,0.6); border-radius: 10px; border: 4px solid #8b5a2b; box-shadow: inset 0 0 10px #000;">
                        {photo_html}
                    </div>
                </div>

                <!-- GALLERY RANDOM -->
                <div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 100%;"></div>
                
                <!-- GALLERY ROMANCE -->
                <div id="view-gallery-romance" class="view-section hidden" style="position: absolute; width: 100%; height: 100%;"></div>

                <!-- PROFILE VIEW -->
                <div id="view-profile" class="view-section hidden" style="position: absolute; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; background: rgba(0,0,0,0.7);">
                    <div style="background: #e8d0aa; border: 6px solid #8b5a2b; padding: 3vw; width: 70%; display: flex; justify-content: space-around; box-shadow: 0 0 20px #000; border-radius: 12px;">
                        <div style="text-align: center; width: 40%;">
                            <h3 class="pixel-text" style="color: #4a3b2c;">PRINCE</h3>
                            <img src="gambarpixel/bagian landing page/icons/couple_prince_princess.png" style="width: 80%; clip-path: inset(0 50% 0 0); filter: drop-shadow(2px 2px 0px rgba(0,0,0,0.5));">
                            <p style="font-size: 1.2rem; font-weight: bold; color: #333;">Sang Ksatria</p>
                        </div>
                        <div style="text-align: center; width: 40%;">
                            <h3 class="pixel-text" style="color: #4a3b2c;">PRINCESS</h3>
                            <img src="gambarpixel/bagian landing page/icons/couple_prince_princess.png" style="width: 80%; clip-path: inset(0 0 0 50%); filter: drop-shadow(2px 2px 0px rgba(0,0,0,0.5)); transform: scaleX(-1);">
                            <p style="font-size: 1.2rem; font-weight: bold; color: #333;">Sang Tuan Putri</p>
                        </div>
                    </div>
                </div>
'''

html = re.sub(
    r'<!-- GALLERY PHOTOBOOTH -->.*?<!-- GALLERY ROMANCE -->.*?(?=</div>\s*<!-- RIGHT UI PANEL)',
    new_photobooth + '\\n            ',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
