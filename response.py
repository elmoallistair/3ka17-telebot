import sqlite3
import textwrap
import datetime as dt
import calendar

def create_connection(db="database.db"):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn

def get_template(command):
    response = {
        "/start": 
            """
            *Selamat datang di 3KA17 BOT*\n
            BOT ini dibuat untuk memenuhi tugas mata kuliah Interaksi Manusia dan Komputer. 
            Kirim saran untuk BOT ini ke @elmoallistair.\n
            Lihat daftar perintah yang tersedia /perintah
            """,
        "/perintah"      : "<b>Daftar perintah</b>\n",
        "/jadwal_kuliah" : "<b>Jadwal Perkuliahan PTA 2020/2021 - 3KA17</b>\n",
        "/jadwal_ujian"  : "<b>Jadwal Ujian PTA 2020/2021 - 3KA17</b>\n",
        "/kalender"      : "<b>Kalender Akademik PTA 2020/2021</b>\n",
        "/tugas"         : "<b>Daftar Tugas Terbaru</b>\n",
        "/berita"        : "<b>Daftar Berita terbaru</b>\n",
        "/seminar"       : "<b>Daftar Seminar terbaru</b>\n",
        "/direktori"     : "<b>Direktori Universitas Gunadarma</b>\n"
    }

    if command in response.keys():
        return response[command]
    return None

def listing_data(command, data):
    if command == "/perintah": 
        pretty_data = "".join([f"\n- {col[1]}   {col[0]}" for col in data])
    elif command == "/jadwal_kuliah":
        start_week = dt.datetime.today() - dt.timedelta(days=dt.datetime.today().weekday() % 7)
        pretty_data = f"\n(Update terakhir : {start_week.strftime('%d %b %Y')})\n"
        temp_day = "Minggu"
        for content in data:
            same_day = content[0] == temp_day
            day_head = f"\n<b>{content[0]}</b>\n"
            day_content = f"<pre>- {content[1]} {' '*(7-len(content[1]))}{'  '.join(content[2:])}</pre>\n"
            temp_content = ""
            if same_day:
                temp_content += day_content
            else:
                temp_content += day_head + day_content
            pretty_data += temp_content.replace("None ", "? ")
            temp_day = content[0]
    elif command == "/jadwal_ujian": 
        pretty_data = "" # TBD
    elif command == "/kalender":
        pretty_data = ""
        for content in data:
            date_str = content[0]
            event = content[1] 
            date_dt = dt.date(*(int(s) for s in date_str.split('-')))
            date = date_dt.strftime('%d%b %Y')
            pretty_data += f"<pre>🗓[{date}]</pre><b>{event}</b>\n\n"
    elif command == "/tugas":
        pretty_data = ""
        for content in data:
            media = content[0]
            matkul = content[1]
            name = content[2]
            date = content[4]
            if date != "None":
                date_dt = dt.date(*(int(s) for s in date.split('-')))
                date = date_dt.strftime('%d%b %Y')
            pretty_data += f"<pre>[{date}] {media} {name}</pre>\n{matkul}\n\n"
    elif command == "/berita": 
        pretty_data = ""
    elif command == "/seminar": 
        pretty_data = "".join([f"\n- <a href='{col[1]}'>{col[2]}</a>" for col in data])
    elif command == "/direktori": 
        pretty_data = "".join([f"\n- <a href='{col[1]}'>{col[2]}</a>" for col in data])

    return pretty_data

def append_data(command):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + command[1:])
    rows = cur.fetchall()

    if rows:
        data = []
        for row in rows:
            conv = lambda i : i or "None"
            line = [conv(i) for i in map(str, row)]
            data.append(line)
        data = listing_data(command, data)
    else:
        data = "\n\nBelum ada data"
    
    return data

def create_button(command):
    template = {    
        "/jadwal_kuliah" : ["Tampilkan tugas minggu ini",
                            "Simpan sebagai PDF/PNG",
                            "Buat Pengingat"],
        "/jadwal_ujian"  : ["Tampilkan tugas minggu ini",
                            "Simpan sebagai PDF/PNG",
                            "Buat Pengingat"],
        "/kalender"      : ["Simpan sebagai PDF",
                            "Simpan sebagai PNG",
                            "Tambahkan ke Google Calendar"],
        "/tugas"         : ["Tampilkan tugas minggu ini",
                            "Simpan sebagai PDF/PNG",
                            "Buat Pengingat"],
        "/berita"        : ["Kunjungi BAAK"],
        "/seminar"       : ["Kunjungi Seminar UG"],
        "/direktori"     : ["Kunjungi Website"]
    }

    keyboard = [
        [InlineKeyboardButton("Button 1", callback_data='callback_1')],
        [InlineKeyboardButton("Button 2", callback_data='callback_2')]
    ]
    return InlineKeyboardMarkup(keyboard)

def create_reply(command):
    template = get_template(command)
    if template:
        if command == "/start":
            reply = template
        else: 
            reply = f"{template} {append_data(command)}"
    else:
        reply = "Command tidak dikenali. /perintah"

    return textwrap.dedent(reply)