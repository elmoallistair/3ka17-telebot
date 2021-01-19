from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from random import seed
import bot
import response

def create_button(msg):
    command = response.msg_to_command(msg)
    template = {    
        "/start"         : [("Bantuan",None)],
        "/help"          : [("Tampilkan daftar perintah  🤖",None),
                            ("Berikan saran fitur","https://t.me/elmoallistair")],
        "/jadwal_kuliah" : [("Tampilkan tugas minggu ini  📚", None),
                            ("Simpan sebagai PDF  ⬇️", None)],
        # "/jadwal_ujian"  : [("Simpan sebagai PDF  ⬇️", None)],
        "/kalender"      : [("Simpan sebagai PDF  ⬇️", None),
                            ("Tambahkan ke Google Calendar  🗓", "https://calendar.google.com/calendar/u/0/r/eventedit?location=Indonesia")],
        "/tugas"         : [("Tampilkan semua tugas 📚", None),
                            ("Buat pengingat  ⏱", None)],
        "/berita"        : [("Kunjungi BAAK 🌐", "baak.gunadarma.ac.id/")],
        "/seminar"       : [("Kunjungi Seminar UG 🌐", "seminar.gunadarma.ac.id/")],
        "/website"       : [("BAAK", "https://baak.gunadarma.ac.id/"), # need revision (add to db)
                            ("V-CLASS", "https://v-class.gunadarma.ac.id/"),
                            ("Praktikum", "https://praktikum.gunadarma.ac.id/"),
                            ("VM LePKom", "https://kursusvmlepkom.gunadarma.ac.id/"),
                            ("Student Site", "https://studentsite.gunadarma.ac.id/"),
                            ("StaffSite", "https://staffsite.gunadarma.ac.id/")],
    }

    keyboard = []
    if command == "/perintah":
        kb = [
            [KeyboardButton("Bantuan")],
            [KeyboardButton("Tampilkan jadwal kuliah")],
            [KeyboardButton("Tampilkan jadwal ujian")],
            [KeyboardButton("Kalender Akademik")],
            [KeyboardButton("Tampilkan tugas aktif")],
            [KeyboardButton("Seminar Terbaru")],
            [KeyboardButton("Daftar Website")]
        ]
        kb_markup = ReplyKeyboardMarkup(kb, resize_keyboard=True)
        return kb_markup

    if command in template.keys():
        for i, (text,url) in enumerate(template[command]):
            keyboard.append([InlineKeyboardButton(text=text, callback_data=f"{command}_callback_{i}", url=url)])
        return InlineKeyboardMarkup(keyboard)
    return None