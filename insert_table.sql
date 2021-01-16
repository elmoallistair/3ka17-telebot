CREATE TABLE perintah (
    perintah VARCHAR(25) PRIMARY KEY,
    deskripsi VARCHAR(50) NOT NULL
);

INSERT INTO perintah VALUES
    ("/start",         "Memulai BOT"),
    ("/perintah",      "Menampilkan daftar perintah"),
    ("/jadwal_kuliah", "Menampilkan jadwal perkuliahan"),
    ("/jadwal_ujian",  "Menampilkan jadwal ujian"),
    ("/tugas",         "Menampilkan daftar tugas"),
    ("/kalender",      "Menampilkan kalender akademik"),
    ("/berita",        "Menampilkan berita terbaru"),
    ("/seminar",       "Menampilkan seminar terbaru"),
    ("/direktori",     "Direktori Universitas Gunadarma");

CREATE TABLE jadwal_kuliah (
    hari VARCHAR(10) NOT NULL,
    waktu VARCHAR(10),
    ruang VARCHAR(5),
    mata_kuliah VARCHAR(40) NOT NULL,
    dosen VARCHAR(30) NOT NULL
);

INSERT INTO jadwal_kuliah VALUES
    ("Senin",  "3/4",    "E333",  "Bahasa Indonesia 2",                "SRI WAHYUNI"),
    ("Senin",  "5/6",    "E333",  "Metode Penelitian",                 "SRI HERMAWATI"),
    ("Senin",  "7/8",    "E333",  "Sistem Berbasis Pengetahuan",       "TRISTYANTI YUSNITASARI"),
    ("Rabu",   "1/2/3",  "E245",  "Graf dan Analisis Algoritma",       "RIFKI KOSASIH"),
    ("Rabu",   "4/5/6",  "E245",  "Interaksi Manusia dan Komputer",    "FEBRIANI"),
    ("Rabu",   "8/9/10", "E122",  "Pemrog. Berorientasi Objek",        "FITRIANINGSIH"),
    ("Jumat",  NULL,     NULL,    "Grafik Komp. dan Pengolahan Citra", "TEAM TEACHING"),
    ("Sabtu",  "5/6/7",  "G229",  "Sistem Basis Data 1",               "SINDY NOVA"),
    ("Sabtu",  "8/9",    "G229",  "Peng. Teknologi Sistem Cerdas",     "JALINAS/ROGAYAH");

CREATE TABLE jadwal_ujian (
    jenis VARCHAR(3) NOT NULL,
    kode_matkul VARCHAR(15) NOT NULL,
    nama_matkul VARCHAR(40) NOT NULL,
    media VARCHAR(10),
    tanggal DATE NOT NULL,
    waktu_mulai VARCHAR(10) NOT NULL,
    waktu_selesai VARCHAR(10) NOT NULL
);

CREATE TABLE kalender (
    tanggal DATE NOT NULL,
    kegiatan VARCHAR(50) NOT NULL
);

INSERT INTO kalender VALUES 
    ("2020-09-28", "Perkuliahan sebelum Ujian Tengah Semester (UTS)"),
    ("2020-10-01", "Pendistribusian FRS ke mahasiswa melalui situs baak.gunadarma.ac.id"),
    ("2020-10-08", "Kegiatan Pengisian dan Pengambilan KRS - Kelas 2 dan 4"),
    ("2020-10-19", "Kegiatan Pengisian dan Pengambilan KRS - Kelas 1 dan Non Kelas"),
    ("2020-11-16", "Batas akhir pengambilan KRS"),
    ("2020-11-27", "Batas akhir pengurusan cuti akademik"),
    ("2020-12-07", "Ujian Tengah Semester (UTS)"),
    ("2020-12-24", "Libur Hari Natal dan Tahun Baru"),
    ("2021-01-04", "Perkuliahan setelah UTS"),
    ("2021-02-01", "Ujian Utama"),
    ("2021-02-08", "Ujian Akhir Semester (UAS)");

CREATE TABLE tugas (
    media VARCHAR(10) NOT NULL,
    mata_kuliah VARCHAR(40) NOT NULL,
    nama_tugas VARCHAR(40) NOT NULL,
    tanggal_mulai DATE,
    tanggal_akhir DATE
);

INSERT INTO tugas VALUES 
    ("V-CLASS", "Metode Penelitian",               "Minggu 11",            "2020-01-04", "2020-01-09"),
    ("V-CLASS", "Peng. Teknologi Sistem Cerdas",   "Minggu 11",            "2020-01-05", "2020-01-12"),
    ("V-CLASS", "Pemrog. Berorientasi Object",     "Tes GUI",              "2020-01-06", "2020-01-12"),
    ("LABSI",   "Interaksi Manusia dan Komputer",  "M4 Ujian",             "2020-01-06", "2020-01-09"),
    ("V-CLASS", "Interaksi Manusia dan Komputer",  "Topik 4",              "2020-01-06", "2020-01-12"),
    ("V-CLASS", "Sistem Basis Data 1",             "Minggu 11",            "2020-01-09", "2020-01-16"),
    ("G-MEET",  "Interaksi Manusia dan Komputer",  "Presentasi Prototype", NULL,         "2020-01-20");

CREATE TABLE berita (
    id INT PRIMARY KEY,
    tanggal DATE NOT NULL,
    judul VARCHAR(100) NOT NULL,
    url VARCHAR(50) NOT NULL
);

INSERT INTO berita VALUES
    (474, "2020-11-28", "Pemberitahuan Pengalihan Media Pembelajaran TT",      "https://baak.gunadarma.ac.id/berita/474"),
    (475, "2020-12-08", "Pengumuman Pelaksanaan UTS Team Teaching",            "https://baak.gunadarma.ac.id/berita/475"),
    (476, "2020-12-16", "Pengambilan SK Cuti PTA 2020/2021",                   "https://baak.gunadarma.ac.id/berita/476"),
    (477, "2020-12-21", "Perubahan Jadwal UTS Pop Culture & Teknologi Sensor", "https://baak.gunadarma.ac.id/berita/477"),
    (478, "2020-12-30", "Pengumuman Perkuliahan Team Teaching Setelah UTS",    "https://baak.gunadarma.ac.id/berita/478"),
    (479, "2021-01-04", "Pengumuman Libur Layanan Administrasi Akademik",      "https://baak.gunadarma.ac.id/berita/479");

CREATE TABLE seminar (
    tanggal DATE NOT NULL,
    judul VARCHAR(100) NOT NULL,
    url VARCHAR(100) NOT NULL
);

INSERT INTO seminar VALUES 
    ("2020-11-10", "OmniSci Indonesia Summit 2020 – Big Data, AI dan Data Analytics",                 "https://seminar.gunadarma.ac.id/omnisci-indonesia-summit-2020-big-data-ai-data-analytics/"),
    ("2020-10-09", "Eksklusif Bersama UG 'Covid-19 dan Bioinformatika: Peluang Invensi dan Inovasi'", "https://seminar.gunadarma.ac.id/eksklusif-bersama-ug-covid-19-bioinformatika-peluang-invensi-dan-inovasi"),
    ("2020-09-18", "Diseminasi Daring KLA 2020 Cross Culture in Architecture",                        "https://seminar.gunadarma.ac.id/diseminasi-daring-kla-2020-cross-culture-in-architecture-uzbekistan-tashkent-samarkand-bukhara");

CREATE TABLE direktori (
    id VARCHAR(15) PRIMARY KEY,
    nama VARCHAR(50) NOT NULL,
    url VARCHAR(50) NOT NULL
);

INSERT INTO direktori VALUES
    ("baak",       "Biro Administarasi Akademik dan Kemahasiswaan", "http://baak.gunadarma.ac.id/"),
    ("v-class",    "Virtual Class Universitas Gunadarma",           "http://v-class.gunadarma.ac.id/"),
    ("library",    "Perpustakaan Pusat Universitas Gunadarma.",     "http://library.gunadarma.ac.id/"),
    ("bapsi",      "Biro Administarasi Akademik dan Kemahasiswaan", "http://bapsi.gunadarma.ac.id/"),
    ("pusatstudi", "Pusat Studi Universitas Gunadarma",             "http://pusatstudi.gunadarma.ac.id/"),
    ("sap",        "Satuan Acara Perkuliahan",                      "http://sap.gunadarma.ac.id/"),
    ("e-journal",  "Jurnal Elektronik Universitas Gunadarma",       "http://ejournal.gunadarma.ac.id/"),
    ("bajamtu",    "Badan Penjamin Mutu Universitas Gunadarma",     "http://spma.gunadarma.ac.id/"),
    ("repository", "Repository Universitas Gunadarma",              "http://repository.gunadarma.ac.id/"),
    ("lpug",       "Lembaga Pengembangan Universitas Gunadarma",    "http://lpug.gunadarma.ac.id/"),
    ("lemlit",     "Lembaga Penelitian Universitas Gunadarma",      "http://penelitian.gunadarma.ac.id/");

