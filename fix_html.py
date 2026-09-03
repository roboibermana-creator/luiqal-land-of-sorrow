import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add ID to dashboard-wrapper
html = html.replace(
    '''<div style="position: relative; width: 100vw; max-width: 1400px; aspect-ratio: 1024/516; background: url('gambarpixel/mockup_dashboard.png') center/cover no-repeat; box-shadow: 0 0 20px #000; overflow: hidden; display: flex;">''',
    '''<div id="dashboard-wrapper" style="position: relative; width: 100vw; max-width: 1400px; aspect-ratio: 1024/516; background: url('gambarpixel/mockup_dashboard.png') center/cover no-repeat; box-shadow: 0 0 20px #000; overflow: hidden; display: flex; transition: background 0.3s ease;">'''
)

# Fix right sidebar click
html = html.replace(
    '''onclick="alert('Profil kalian berdua ada di sini!')"''',
    '''id="btn-profile" title="Lihat Profil"'''
)

# Generate Photobooth Images
photobooth_files = os.listdir(r'd:\coupleweb\photo\photobooth')
photo_tags = []
for file in photobooth_files:
    if file.endswith('.jpg') or file.endswith('.png'):
        photo_tags.append(f'<img src="photo/photobooth/{file}" class="photobooth-img" style="width: 100%; height: auto; border: 4px solid #fff; box-shadow: 2px 2px 5px #000; cursor: pointer; border-radius: 8px;">')

photo_html = '\\n                            '.join(photo_tags)

# Replace Photobooth section
new_photobooth = f'''
                <!-- GALLERY PHOTOBOOTH -->
                <div id="view-gallery-photobooth" class="view-section hidden" style="position: absolute; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; background: url('gambarpixel/bagian photobooth/background/assets_bg_castle_balcony.png') center/cover no-repeat;">
                    <div style="width: 90%; height: 90%; overflow-y: auto; padding: 2vw; display: grid; grid-template-columns: repeat(3, 1fr); gap: 2vw; background: rgba(0,0,0,0.6); border-radius: 10px; border: 4px solid #8b5a2b; box-shadow: inset 0 0 10px #000;">
                        {photo_html}
                    </div>
                </div>

                <!-- GALLERY RANDOM (Empty overlay since wrapper bg handles it) -->
                <div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 100%;"></div>
                
                <!-- GALLERY ROMANCE (Empty overlay since wrapper bg handles it) -->
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
    r'<!-- GALLERY PHOTOBOOTH -->.*?<!-- GALLERY ROMANCE -->\s*</div>',
    new_photobooth + '\\n            </div>',
    html,
    flags=re.DOTALL
)

# Fix script logic
script_start = html.find('function showView(viewElement) {')
script_end = html.find('// 4. Aksi Logout')
if script_start != -1 and script_end != -1:
    new_script = '''
            const dashboardWrapper = document.getElementById('dashboard-wrapper');
            const viewProfile = document.getElementById('view-profile');
            const btnProfile = document.getElementById('btn-profile');

            function showView(viewElement, bgImage = null) {
                allViews.forEach(v => v.classList.add('hidden'));
                if(viewProfile) viewProfile.classList.add('hidden');
                
                if (viewElement) viewElement.classList.remove('hidden');
                
                if (bgImage) {
                    dashboardWrapper.style.backgroundImage = url('gambarpixel/');
                } else {
                    dashboardWrapper.style.backgroundImage = url('gambarpixel/mockup_dashboard.png');
                }
            }

            // 1. Aksi Title Screen ke Login
            btnStart.addEventListener('click', () => {
                screenTitle.classList.add('hidden');
                screenTitle.classList.remove('active');
                
                screenLogin.classList.remove('hidden');
                screenLogin.classList.add('active');
                
                inputPassword.value = '';
                errorMsg.classList.add('hidden');
                inputPassword.focus();
            });
            
            // Aksi Cancel Login
            if(btnCancel) {
                btnCancel.addEventListener('click', () => {
                    screenLogin.classList.add('hidden');
                    screenLogin.classList.remove('active');
                    
                    screenTitle.classList.remove('hidden');
                    screenTitle.classList.add('active');
                });
            }
            
            // 2. Aksi Login Validasi
            const attemptLogin = () => {
                if (inputPassword.value === '01052026') {
                    screenLogin.classList.add('hidden');
                    screenLogin.classList.remove('active');
                    
                    screenMain.classList.remove('hidden');
                    screenMain.classList.add('active');
                    
                    showView(viewDashboard);
                    
                    bgmAudio.volume = 0.3;
                    bgmAudio.play().catch(e => console.log('Autoplay blocked:', e));
                } else {
                    errorMsg.classList.remove('hidden');
                }
            };
            
            btnLogin.addEventListener('click', attemptLogin);
            inputPassword.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') attemptLogin();
            });
            
            // 3. Aksi Sidebar
            btnDashboardView.addEventListener('click', () => showView(viewDashboard));
            if(btnPhotoboothGallery) btnPhotoboothGallery.addEventListener('click', () => showView(viewGalleryPhotobooth));
            if(btnRandomGallery) btnRandomGallery.addEventListener('click', () => showView(viewGalleryRandom, 'mockup_gallery_random.png'));
            if(btnRomanceGallery) btnRomanceGallery.addEventListener('click', () => showView(viewGalleryRomance, 'mockup_gallery_romance.png'));
            
            if(btnProfile) {
                btnProfile.addEventListener('click', () => {
                    allViews.forEach(v => v.classList.add('hidden'));
                    viewProfile.classList.remove('hidden');
                    dashboardWrapper.style.backgroundImage = url('gambarpixel/mockup_dashboard.png');
                });
            }
            
            '''
    html = html[:script_start] + new_script + html[script_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
