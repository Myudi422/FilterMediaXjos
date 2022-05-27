class Script(object):
    START_TXT = """Hello {},

saya bot ᴄᴄɢɴɪᴍᴇx v2.0, untuk penggunaan lebih lanjut, silahkan klik tombol bantuan dibawah!.

Jika kalian suka dengan bot ini, silahkan dukung kami dengan cara, share bot ini, ataupun support kami & juga berdonasi agar server tetap hidup & kami meningkatkan bot ini lebih baik.

Saya sarankan, Silahkan Daftar/Login Anilist terlebih dahulu (/auth), untuk menikmati fitur bot ini sepenuhnya."""

    HELP_TXT = """Hey {}

<b>Inilah Bantuan Untuk Perintah Saya.</b>"""

    ABOUT_TXT = """<b>➥ My name: {}
➥ Library: <a href='https://docs.pyrogram.org/'>Pyrogram</a>
➥ Language: Python 𝟹
➥ Data Base: <a href='https://www.mongodb.com/'>MongoDB</a>
➥ Bot Server: <a href='https://heroku.com'>Heroku</a>
➥ Build Status: v2.0 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>
<b>DEVS:</b>
- <a href='https://t.me/Rizki_Wahyudi03'>Owner</a>

<b>SUPPORT GROUP</b>
- <a href='https://t.me/+y53tWFUw6Q43NzE9'>ᴄɢɴɪᴍᴇx - [ᴄʜᴀᴛ] 🇮🇩</a>"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter adalah fitur di mana pengguna dapat mengatur balasan otomatis untuk kata kunci tertentu dan Dingdi akan merespons setiap kali kata kunci ditemukan pesan

<b>CATATAN:</b>
1. ccgnimex harus memiliki hak istimewa admin.
2. Hanya admin yang dapat menambahkan filter dalam obrolan.
3. Tombol peringatan memiliki batas 64 karakter.

<b>Perintah dan Penggunaan:</b>
• /filter - menambahkan filter dalam obrolan.
• /filters - daftar semua filter obrolan.
• /del - menghapus filter tertentu dalam obrolan.
• /delall - menghapus seluruh filter dalam obrolan (khusus pemilik obrolan)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- ccgnimex mendukung tombol url dan peringatan sebaris.

<b>CATATAN:</b>
1. Telegram tidak akan mengizinkan Anda mengirim tombol tanpa konten apa pun, jadi konten itu wajib.
2. ccgnimex mendukung tombol dengan jenis media telegram apa pun.
3. Tombol harus diuraikan dengan benar sebagai format penurunan harga.

<b>Tombol URL:</b>
<code>[Teks Tombol](buttonurl:https://t.me/otakuindonew)</code>

<b>Tombol peringatan:</b>
<code>[Teks Tombol](buttonalert:Ini adalah pesan peringatan)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

Anda juga dapat menyesuaikan konten pesan Anda dengan data kontekstual. Misalnya, Anda dapat menyebutkan nama pengguna di pesan filter, atau menyebutkannya di filter!

<b>Tambalan yang didukung:</b>
- <code>{first}</code>: Nama depan pengguna.
- <code>{last}</code>: Nama belakang pengguna.
- <code{username}</code>: Nama pengguna pengguna.
- <code>{mention}</code>: Menyebut pengguna dengan nama depannya.
- <code>{id}</code>: ID pengguna.
- <code>{dcid}</code>: ID DC pengguna.
- <code>{chatname}</code>: Nama obrolan.
- <code>{query}</code>: Semua Pesan yang Dibalas.

<b>Contoh:</b>
<b>- Simpan filter menggunakan penyebutan.</b>
-> <code>/filter test Halo {mention} Ini Username Anda : {username} Dan Ini ID Anda : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>CATATAN:</b>
1. Jadikan saya admin saluran Anda jika itu pribadi.
2. Pastikan saluran Anda tidak mengandung file camrips, porno, dan palsu.
3. Teruskan pesan terakhir kepada saya dengan tanda kutip.
  Saya akan menambahkan semua file di saluran itu ke db saya."""

    CONNECTION_TXT = """Help: <b>Connections</b>

Bantuan: Koneksi

- Digunakan untuk menghubungkan bot ke PM untuk mengelola filter
- Ini membantu untuk menghindari spam dalam grup.

CATATAN:
1. Hanya admin yang dapat menambahkan koneksi.
2. Kirim / sambungkan untuk menghubungkan saya ke PM Anda

Perintah dan Penggunaan:
• /connect - menghubungkan chat tertentu ke PM Anda.
• /disconnect - memutuskan sambungan dari obrolan.
• /connections - daftar semua koneksi Anda."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Pilih jenis filter Di bawah ini:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Tempelkan beberapa teks atau dokumen di situs web!

<b>Perintah dan Penggunaan:</b>
• /paste [teks] - tempel teks yang diberikan pada Pasty
• /paste [balasan] - tempel teks balasan di Pasty

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Lakukan sesukamu dengan modul telegra.ph!

<b>Perintah dan Penggunaan:</b>
• /tgmedia atau /tgraph - unggah media yang didukung (dalam 5MB) ke telegraf.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    INFO_TXT = """Help: <b>Information</b>

Dapatkan informasi tentang sesuatu!

<b>Perintah dan Penggunaan:</b>
• /id - mendapatkan id dari pengguna tertentu.
• /info - mendapatkan informasi tentang pengguna.
• /json - mendapatkan detail json dari sebuah pesan.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Perintah dan Penggunaan:</b>
• /torrent atau /tor <nama film>: Dapatkan Tautan Torrent Anda Dari Berbagai Sumber.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Terjemahkan teks ke bahasa tertentu!

<b>Perintah dan Penggunaan:</b>
• /tr [kode bahasa][balas] - terjemahkan pesan balasan ke bahasa tertentu. intinya reply text yang ingin di translate.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• ccgnimex dapat menerjemahkan teks ke 200+ bahasa."""

    SEARCH_TXT = """Help: <b>ccgnimex</b>

Cari banyak hal tanpa meninggalkan telegram!

<b>Perintah dan Penggunaan:</b>
• /imdb - dapatkan informasi film dari sumber ccgnimex.
• /search - dapatkan informasi film dari berbagai sumber.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Alat pencarian lainnya dapat ditemukan di inline.
• Perintah-perintah itu bekerja pada pm dan grup."""

    PURGE_TXT = """Help: <b>Purge</b>

Perlu menghapus banyak pesan? Itulah gunanya pembersihan!

<b>Perintah dan Penggunaan:</b>
• /purge - menghapus semua pesan dari pesan yang dibalas, ke pesan saat ini.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada grup.
• Perintah ini hanya dapat digunakan oleh admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Beberapa orang perlu dilarang publik; spammer, gangguan, atau hanya troll.

Modul ini memungkinkan Anda melakukannya dengan mudah, dengan memaparkan beberapa tindakan umum, sehingga semua orang akan melihatnya!

<b>Perintah dan Penggunaan:</b>
• /ban - melarang pengguna.
• /tban - mencekal pengguna untuk sementara. Contoh nilai waktu: 4m = 4 menit, 3j = 3 jam, 6h = 6 hari, 5w = 5 minggu.
• /mute - mematikan suara pengguna.
• /tmute - menonaktifkan sementara pengguna. Contoh nilai waktu: 4m = 4 menit, 3j = 3 jam, 6h = 6 hari, 5w = 5 minggu.
• /unban atau /unmute - mengaktifkan suara pengguna & membatalkan larangan pengguna.

<b>Contoh:</b>
- Bungkam pengguna selama dua jam.
-> <code>/tmute @namapengguna 2j</code>

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada grup.
• Perintah ini hanya dapat digunakan oleh admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

Semua perintah terkait pin dapat ditemukan di sini; tetap perbarui obrolan Anda tentang berita terbaru dengan pesan yang disematkan sederhana!

<b>Perintah dan Penggunaan:</b>
• /pin: Menyematkan pesan yang Anda balas. Tambahkan 'keras' atau 'beri tahu' untuk mengirim pemberitahuan ke anggota grup.
• /unpin: Lepas pin pesan yang disematkan saat ini. Jika digunakan sebagai balasan, lepaskan pin dari pesan yang dibalas.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini hanya berfungsi grup.
• Perintah ini hanya dapat digunakan oleh admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>CATATAN:</b>
Modul ini hanya berfungsi untuk admin saya

<b>Perintah dan Penggunaan:</b>
• /logs - untuk mendapatkan kesalahan terbaru.
• /stats - untuk mendapatkan status file dalam db.
• /delete - untuk menghapus file tertentu dari db.
• /users - untuk mendapatkan daftar pengguna dan id saya.
• /chats - untuk mendapatkan daftar chat dan ID saya.
• /leave - untuk keluar dari obrolan.
• /disable - menonaktifkan obrolan.
• /ban_users - untuk melarang pengguna.
• /unban_users - untuk membatalkan pemblokiran pengguna.
• /channel - untuk mendapatkan daftar total saluran yang terhubung.
• /broadcast - untuk menyiarkan pesan ke semua pengguna."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

Masih Progress....."""

    MEMES_TXT = """Help: <b>Memes</b>

Beberapa meme dank untuk bersenang-senang atau apa pun!

<b>Perintah dan Penggunaan:</b>
• /throw or /dar - t𝗈 m𝖺𝗄𝖾 drat
• /roll atau /dice - melempar dadu
• /goal or /shoot - untuk membuat gol atau menembak
• /luck or /cownd - Putar Keberuntungan
• /menjalankan string

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Beberapa URL Lebih Pendek

<b>Perintah dan Penggunaan:</b>
• /short <code>(link)</code> - Saya akan mengirimkan link singkatnya.

<b>Contoh:</b>
<code>/short https://t.me/otakuindonew</code>

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    TTS_TXT = """Help: <b>Text to Speech</b>

Modul untuk mengonversi teks ke suara dengan dukungan bahasa.

<b>Perintah dan Penggunaan:</b>
• /tts - Membalas pesan teks apa pun dengan kode bahasa untuk dikonversi sebagai audio.

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    MUSIC_TXT = """Help: <b>Music</b>

Modul unduh musik, bagi mereka yang menyukai musik.

<b>Perintah dan Penggunaan:</b>
• /song atau /mp3 (nama lagu) - unduh lagu dari server yt.
• /video atau /mp4 (nama lagu) - unduh video dari server yt.

<b>Unduhan Thumbnail YouTube</b>
• /ytthumb (tautan youtube)
<b>Contoh:</b> <code>/ytthumb https://youtu.be/XXX</code>

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

Tidak Ada Yang Perlu Diketahui Lebih Jauh. Kirimi Saya Batas Kata Sandi Anda.
- Saya Akan Memberikan Kata Sandi Dari Batas Itu.

<b>Perintah dan Penggunaan:</b>
• /genpassword atau /genpw <code>20</code>

<b>CATATAN:</b>
• Hanya Digit yang Diperbolehkan
• Digit Maksimum yang Diizinkan Hingga 84
(Saya Tidak Dapat Membuat Kata Sandi Di Atas Panjang 84)
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

bot untuk membuat tautan untuk membagikan teks di telegram.

<b>Perintah dan Penggunaan:</b>
• /share (teks atau balas pesan)

<b>CATATAN:</b>
• ccgnimex harus memiliki hak istimewa admin.
• Perintah ini bekerja pada pm dan grup.
• Perintah ini dapat digunakan oleh semua anggota grup."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Menendang anggota incative dari grup. Tambahkan saya sebagai admin dengan izin larangan pengguna di grup.</b>

<b>Perintah dan Penggunaan:</b>
• /inkick - perintah dengan argumen yang diperlukan dan saya akan mengeluarkan anggota dari grup.
• /instatus - untuk memeriksa status terkini dari anggota obrolan dari grup.
• /inkick within_month long_time_ago - untuk menendang pengguna yang offline selama lebih dari 6-7 hari.
• /inkick long_time_ago - untuk menendang anggota yang offline selama lebih dari sebulan dan Akun yang Dihapus.
• /dkick - untuk menendang akun yang dihapus."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""

