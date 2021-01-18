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
            <b>Selamat datang di 3KA17 BOT</b>  👋\n
            Lihat daftar perintah /perintah
            Tampilkan bantuan /help 
            """,
        "/help":
            """
            <b>Bantuan</b> ❔\n
            Bot ini merupakan media pengaksesan informasi untuk menunjang pembelajaran untuk kelas 3KA17.

            Lihat daftar perintah: /perintah
            Kirim pertanyaan dan saran ke @elmoallistair\n
            Lihat source code BOT ini:
            https://github.com/elmoallistair/3ka17-telebot

            Keterangan: sebagian besar button masih belum berfungsi.
            """,
        "/perintah"      : "<b>Daftar perintah </b>  🤖\n",
        "/jadwal_kuliah" : "<b>Jadwal Perkuliahan PTA 2020/2021 - 3KA17</b>\n",
        "/jadwal_ujian"  : "<b>Jadwal Ujian PTA 2020/2021 - 3KA17</b>\n",
        "/kalender"      : "<b>Kalender Akademik PTA 2020/2021</b>\n",
        "/tugas"         : "<b>Daftar Tugas Terbaru</b>  📚\n",
        "/berita"        : "<b>Daftar Berita terbaru</b>  📬\n",
        "/seminar"       : "<b>Daftar Seminar terbaru</b>\n\n🔴  Status: <b>ERROR</b> \n\nWebsite https://seminar.gunadarma.ac.id/ sedang tidak bisa diakses.",
        "/website"       : "<b>Direktori Universitas Gunadarma  🌐</b>\n"
    }

    if command in response.keys():
        return response[command]
    return None

def listing_data(command, data):
    pretty_data = ""
    if command == "/perintah":
        for content in data:
            command = content[0]
            description = content[1]
            pretty_data += f"\n- {description} {command}"
        pretty_data += '\n\n\n💡 <b>Tips</b>: Anda juga dapat mengirimkan pesan dengan keyword tertentu seperti "<i>Tampilkan daftar tugas terbaru</i>"!'
    elif command == "/jadwal_kuliah":
        start_week = dt.datetime.today() - dt.timedelta(days=dt.datetime.today().weekday() % 7)
        pretty_data = f"\n🔄  Update terakhir : {start_week.strftime('%d %b %Y')}\n"
        temp_day = "Minggu"
        for content in data:
            same_day = content[0] == temp_day
            day_head = f"\n<b>{content[0]}</b>\n"
            day_content = f"<pre>- {content[1]} {' '*(7-len(content[1]))}{'  '.join(content[2:4])}</pre>\n"
            temp_content = ""
            if same_day:
                temp_content += day_content
            else:
                temp_content += day_head + day_content
            pretty_data += temp_content.replace("None ", "? ")
            temp_day = content[0]
    elif command == "/jadwal_ujian":
        pass # tbd, no data
    elif command == "/kalender":
        for content in data:
            date_str = content[0]
            event = content[1] 
            date_dt = dt.date(*(int(s) for s in date_str.split('-')))
            date = date_dt.strftime('%d %b %Y')
            pretty_data += f"\n<code>🗓 [{date}]</code>  <b>{event}</b>"
    elif command == "/tugas":
        pretty_data += "\n🟢  <b>Status: Tugas aktif</b>\n\n"
        for content in data:
            media = content[0]
            matkul = content[1]
            name = content[2]
            date_str = content[4]
            date_dt = dt.date(*(int(s) for s in date_str.split('-')))
            date = date_dt.strftime('%d %b %Y')
            curr_date = dt.date.today()
            if date_dt > curr_date:
                pretty_data += f"📝  <b>{matkul}</b><pre>[{date}] {media} {name}</pre>\n\n"
    elif command == "/berita":
        for content in data[:-6:-1]:
            date_str = content[1]
            title = content[2]
            url = content[3]
            date_dt = dt.date(*(int(s) for s in date_str.split('-')))
            date = date_dt.strftime('%d %b %Y')
            pretty_data += f"\n✉  [{date}]  <b><a href='{url}'>{title}</a></b>"
    elif command == "/seminar"[:-5:-1]: 
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
        data = "\n\n🔴  Status: <b>Belum ada data</b>"
    
    return data

def msg_to_command(msg): # need  improvement
    keywords = {
        "/start"        : ["mulai", "aktifkan", "bot", "start"],
        "/help"         : ["bantuan", "help", "penggunaan", "cara pakai"],
        "/perintah"     : ["perintah", "command", "instruksi"],
        "/jadwal_kuliah": ["kuliah", "jadwal", "mata kuliah", "pelajaran"],
        "/jadwal_ujian" : ["ujian", "uts", "uu", "uas"],
        "/kalender"     : ["acara", "kalender", "kalendar", "event", "kegiatan"],
        "/tugas"        : ["tugas", "pr", "v-class"],
        "/berita"       : ["berita", "news"],
        "/seminar"      : ["seminar", "event"],
        "/website"      : ["direktori", "web", "website"]
    }
    if msg in keywords.keys():
        return msg

    list_msg = msg.lower().split()

    all_keys = []
    for value in keywords.values():
        all_keys.extend(value)

    for msg_key in list_msg:
        for key,value in keywords.items():
            if msg_key in value:
                return key

    return None

def create_reply(msg):
    command = msg_to_command(msg.lower())
    if command:
        template = get_template(command)
        if template:
            if command in ["/start", "/help", "/seminar", "/website"]:
                reply = template
            else: 
                reply = f"{template} {append_data(command)}"
        return textwrap.dedent(reply)
    return "Command tidak dikenali. /perintah"

def callback_create_reply(callback):
    reply = "test" #TBD

    return textwrap.dedent(reply)
