import sys, os, time
os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))
print(os.getcwd())
import pywinauto


os.chdir(r'cd_rom\\KWSEMU')
print(os.getcwd())

app = pywinauto.Application().start(r'setup.exe')

interval = 1.0
wizard = app[r'Kシリーズ端末エミュレータ(64bit) V7.2 - InstallShield Wizard']
print(r'初期化中...')
wizard.window(title_re='次へ').wait('ready', 60)

print(r'Kシリーズ端末エミュレータ(64bit) V7.2 セットアップへようこそ')
time.sleep(interval)
wizard.window(title_re='次へ').click()

print(r'ソフトウェア説明書')
time.sleep(interval)
wizard.window(title_re='次へ').click()

print(r'インストール先の選択')
time.sleep(interval)
wizard.window(title_re='次へ').click()

time.sleep(interval)

install_dir = r'C:\\Program Files\\Fujitsu\\KWSEMU'
if os.path.isdir(install_dir) == False : 
    app.window(title_re=r'新しいフォルダ').window(title_re=r'はい').click()
    print(r'新しいフォルダの作成')
    time.sleep(interval)

print(r'Kシリーズ端末エミュレータ(64bit) V7.2 インストールのショートカット')
wizard.window(title_re='次へ').click()

print(r'インストール準備の完了')
time.sleep(interval)
wizard.window(title_re=r'インストール').click()

print(r'インストール中...')

wizard.window(title_re=r'完了').wait('ready', 60)
print(r'完了？')
time.sleep(interval)
wizard.window(title_re=r'完了').click()

print(r'完了した！')
