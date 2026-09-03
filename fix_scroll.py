import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the dashboard-wrapper structure
old_wrapper_start = '''<div id="dashboard-wrapper" style="position: relative; width: 100vw; max-width: 1400px; aspect-ratio: 1024/516; background: url('gambarpixel/mockup_dashboard.png') center/cover no-repeat; box-shadow: 0 0 20px #000; overflow: hidden; display: flex; transition: background 0.3s ease;">'''
new_wrapper_start = '''<div id="dashboard-wrapper" style="position: relative; width: 100vw; max-width: 1400px; aspect-ratio: 1024/516; box-shadow: 0 0 20px #000; overflow: hidden;">
            <div id="scrolling-bg" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('gambarpixel/mockup_dashboard.png') top left / 100% 100% repeat-y; z-index: 0; transition: background-image 0.3s ease;"></div>
            
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; z-index: 10; pointer-events: none;">
                <!-- Re-enable pointer events for interactive areas -->
                <style>
                    #main-content-area { pointer-events: auto; overflow-y: auto; scrollbar-width: none; -ms-overflow-style: none; }
                    #main-content-area::-webkit-scrollbar { display: none; }
                    .sidebar-interactive { pointer-events: auto; }
                </style>
'''
html = html.replace(old_wrapper_start, new_wrapper_start)

# Add sidebar-interactive class to sidebars
html = html.replace('''<div style="width: 22%; height: 100%; position: relative; z-index: 10; display: flex; flex-direction: column; padding-top: 15%; padding-left: 3%;">''',
                    '''<div class="sidebar-interactive" style="width: 22%; height: 100%; position: relative; z-index: 10; display: flex; flex-direction: column; padding-top: 15%; padding-left: 3%;">''')

html = html.replace('''<div style="width: 20%; height: 100%; position: relative; z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: space-evenly; padding-top: 5%;">''',
                    '''<div class="sidebar-interactive" style="width: 20%; height: 100%; position: relative; z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: space-evenly; padding-top: 5%;">''')

# Close the new foreground UI layer div at the end of WADAH 3
# It should be placed right before the closing tag of dashboard-wrapper
html = re.sub(r'(<!-- WADAH 4.*?-->)', r'</div>\n        \1', html, flags=re.DOTALL)
# Wait, dashboard-wrapper closing tag is right before WADAH 4? Let's assume so, or just close it before the last </div> of screen-main.
# Let's do it precisely using regex.
html = html.replace('''                </div>
            </div>
        </div>
    </div>

    <!-- AUDIO BGM -->''',
    '''                </div>
            </div>
            </div>
        </div>
    </div>

    <!-- AUDIO BGM -->''')

# Update view-sections to have multiple pages
html = html.replace('''<div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 100%;"></div>''',
                    '''<div id="view-gallery-random" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;"></div>''')

html = html.replace('''<div id="view-gallery-romance" class="view-section hidden" style="position: absolute; width: 100%; height: 100%;"></div>''',
                    '''<div id="view-gallery-romance" class="view-section hidden" style="position: absolute; width: 100%; height: 300%;"></div>''')

# Update script logic to target scrolling-bg instead of dashboard-wrapper
html = html.replace('''dashboardWrapper.style.backgroundImage = 'url("gambarpixel/' + bgImage + '")';''',
                    '''document.getElementById('scrolling-bg').style.backgroundImage = 'url("gambarpixel/' + bgImage + '")';''')
html = html.replace('''dashboardWrapper.style.backgroundImage = "url('gambarpixel/mockup_dashboard.png')";''',
                    '''document.getElementById('scrolling-bg').style.backgroundImage = "url('gambarpixel/mockup_dashboard.png')";''')

# Add scroll sync logic
scroll_sync = '''
            // Sync background scroll
            const mainContentArea = document.getElementById('main-content-area');
            const scrollingBg = document.getElementById('scrolling-bg');
            mainContentArea.addEventListener('scroll', (e) => {
                scrollingBg.style.backgroundPositionY = -px;
            });
'''
html = html.replace('// 1. Aksi Title Screen ke Login', scroll_sync + '\n            // 1. Aksi Title Screen ke Login')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
