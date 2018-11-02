
#!/usr/bin/python
# -*- coding: utf-8 -*-


class programs:

	def __init__(self, types, name, url):
		self.types = types
		self.name = name
		self.url = url


google = programs('Browser', 'Google Browser', 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B827996B2-6E3E-A687-4E48-87336A256AEB%7D%26lang%3Dru%26browser%3D2%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dtrue%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Ddefaultbrowser/update2/installers/ChromeSetup.exe')
yandex = programs('Browser', 'Yandex', 'https://cache-novosibrt04.cdn.yandex.net/download.cdn.yandex.net/browser/back-sea-35-1366-base/ru/lite/Yandex.exe?browser=GoogleChrome/64/70.0.3538.77&a-type=uncommercial&banerid=6302000000:5bdd221b34f76400199953cb&broexp=8&statpromo=true&pps=installID%3D984408191505035890_1541218848992&yandexuid=984408191505035890&hash=aa419e8adddabc32fac30a988a3d559b&download_date=1541218848&.exe')
sevenZip = programs('Archivers', '7-Zip', 'https://www.7-zip.org/a/7z1801.exe')
winRar = programs('Archivers', 'Win-RAR', 'http://www.rarlab.com/rar/wrar540.exe')
codecPack = programs('Media', 'Codec-Pack', 'http://files2.codecguide.com/K-Lite_Codec_Pack_1405_Full.exe')
qBittorrent = programs('Media', 'qBittorrent', 'https://datapacket.dl.sourceforge.net/project/qbittorrent/qbittorrent-win32/qbittorrent-4.0.4/qbittorrent_4.0.4_setup.exe')
python3 = programs('Development', 'Python 3', 'https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe')
sublimetext = programs('Development', 'SublimeText', 'https://download.sublimetext.com/Sublime%20Text%20Build%203176%20Setup.exe')
colorMania = programs('Development', 'ColorMania', 'http://www.blacksunsoftware.com/downloads/ColorManiaSetup.exe')