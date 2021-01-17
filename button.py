from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from random import seed
import bot

def create_button(command):
    template = {    
        "/start"         : [("Tampilkan daftar perintah  🤖",None),
                            ("Bantuan",None)],
        "/help"          : [("Tampilkan daftar perintah  🤖",None)],
        "/perintah"      : [("Berikan saran fitur","mailto:work.elmoallistair@gmail.com?subject=BotFeature")],
        "/jadwal_kuliah" : [("Tampilkan tugas minggu ini  📚", None),
                            ("Simpan sebagai PDF  ⬇️", None)],
        "/jadwal_ujian"  : [("Simpan sebagai PDF  ⬇️", None),
                            ("Buat pengingat  ⏱",None)],
        "/kalender"      : [("Simpan sebagai PDF  ⬇️",None),
                            ("Tambahkan ke Google Calendar  🗓", None)],
        "/tugas"         : [("Tampilkan semua tugas",None),
                            ("Buat pengingat  ⏱",None)],
        "/berita"        : [("Kunjungi BAAK", "baak.gunadarma.ac.id/")],
        "/seminar"       : [("Kunjungi Seminar UG", "seminar.gunadarma.ac.id/")],
        "/website"       : [("Website UG", "https://gunadarma.ac.id/"),
                            ("BAAK", "https://baak.gunadarma.ac.id/"),
                            ("V-CLASS", "https://v-class.gunadarma.ac.id/"),
                            ("Praktikum", "https://praktikum.gunadarma.ac.id/"),
                            ("VM LePKom", "https://kursusvmlepkom.gunadarma.ac.id/"),
                            ("Library", "https://library.gunadarma.ac.id/"),
                            ("Student Site", "https://studentsite.gunadarma.ac.id/"),
                            ("StaffSite", "https://staffsite.gunadarma.ac.id/"),
                            ("SAP", "https://sap.gunadarma.ac.id/"),
                            ("E-Journal", "https://ejournal.gunadarma.ac.id/")]
    }

    if command in template.keys():
        keyboard = []
        if command == "/website":
            data = template[command]
            for i, content in enumerate(data[::2]):
                text1, text2 = data[i][0], data[i+1][0]
                url1, url2 = data[i][1], data[i+1][1]
                print(text1,url1)
                print(text2,url2)

                keyboard.append([
                    InlineKeyboardButton(text=text1, callback_data=f"website_callback_{i}", url=url1),
                    InlineKeyboardButton(text=text2, callback_data=f"website_callback_{i+1}", url=url2)
                    ])
            return InlineKeyboardMarkup(keyboard)
        for i, (text,url) in enumerate(template[command]):
            keyboard.append([InlineKeyboardButton(text=text, callback_data=f"{command}_callback_{i}", url=url)])
        return InlineKeyboardMarkup(keyboard)
    return None

def callback_query_handler(update, context):
    cqd = update.callback_query.data
    print(cqd)
    pass # TBD
