import scrapy


class KanjiN5Spider(scrapy.Spider):
    name = "kanji-n5"
    start_urls = [
        "https://www.bahasajepangbersama.com/2015/10/daftar-huruf-kanji-untuk-jlpt-level-n4.html",
    ]

    def parse(self, response):
        # Mengambil data dari tabel
        data = response.css("table tr td::text").getall()

        kanji = []
        onyomi = []
        kunyomi = []
        arti = []

        for i in range(len(data)):
            if i % 4 == 0:
                kanji.append(data[i])
            elif i % 4 == 1:
                onyomi.append(data[i])
            elif i % 4 == 2:
                kunyomi.append(data[i])
            elif i % 4 == 3:
                arti.append(data[i])

        # Menggabungkan data
        for k, o, ku, a in zip(kanji, onyomi, kunyomi, arti):
            yield {"Kanji": k, "Onyomi": o, "Kunyomi": ku, "Arti": a}
