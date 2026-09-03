
        document.addEventListener('DOMContentLoaded', () => {
            const screenTitle = document.getElementById('screen-title');
            const screenLogin = document.getElementById('screen-login');
            const screenMain = document.getElementById('screen-main');
            
            const btnStart = document.getElementById('btn-start');
            const btnLogin = document.getElementById('btn-login');
            const btnCancel = document.getElementById('btn-cancel');
            const inputPassword = document.getElementById('password-input');
            const errorMsg = document.getElementById('error-msg');
            
            const viewDashboard = document.getElementById('view-dashboard');
            const viewGalleryRandom = document.getElementById('view-gallery-random');
            const viewGalleryRomance = document.getElementById('view-gallery-romance');
            const viewGalleryPhotobooth = document.getElementById('view-gallery-photobooth');
            const allViews = document.querySelectorAll('.view-section');
            
            const btnDashboardView = document.getElementById('btn-dashboard-view');
            const btnLogout = document.getElementById('btn-logout');
            const btnRandomGallery = document.getElementById('btn-random-gallery');
            const btnRomanceGallery = document.getElementById('btn-romance-gallery');
            const btnPhotoboothGallery = document.getElementById('btn-photobooth-gallery');
            
            const bgmAudio = document.getElementById('bgm-audio');
            const btnMute = document.getElementById('btn-mute');
            
            function showView(viewElement) {
                allViews.forEach(v => v.classList.add('hidden'));
                if (viewElement) viewElement.classList.remove('hidden');
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
                    
                    // Reset View ke Dashboard
                    showView(viewDashboard);
                    
                    // Play BGM (volume 30%)
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
            
            // 3. Aksi Sidebar menu Gambar & Home
            btnDashboardView.addEventListener('click', () => showView(viewDashboard));
            btnRandomGallery.addEventListener('click', () => showView(viewGalleryRandom));
            btnRomanceGallery.addEventListener('click', () => showView(viewGalleryRomance));
            btnPhotoboothGallery.addEventListener('click', () => showView(viewGalleryPhotobooth));
            
            // 4. Aksi Logout kembali ke Title Screen
            if (btnLogout) {
                btnLogout.addEventListener('click', () => {
                    screenMain.classList.add('hidden');
                    screenMain.classList.remove('active');
                    
                    screenTitle.classList.remove('hidden');
                    screenTitle.classList.add('active');
                    
                    // Hentikan musik saat kembali ke judul
                    bgmAudio.pause();
                    bgmAudio.currentTime = 0;
                    btnMute.textContent = '[ 🔊 ]';
                });
            }

            // 5. Aksi Tombol Mute Audio
            btnMute.addEventListener('click', () => {
                if (bgmAudio.paused) {
                    bgmAudio.play();
                    btnMute.textContent = '[ 🔊 ]';
                } else {
                    bgmAudio.pause();
                    btnMute.textContent = '[ 🔇 ]';
                }
            });
        });
    
