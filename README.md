# Python İle Otomatik SQL Enjeksiyonu Kontrol Aracı
SQL Injection Scanner, Python programlama dili kullanılarak geliştirilmiş bir otomatik SQL enjeksiyonu tarama aracıdır. Bu araç, web uygulamalarında SQL enjeksiyonu açıklarını kontrol etmek için kullanılır ve potansiyel güvenlik zafiyetlerini tespit etmenize yardımcı olur.

Kod, requests ve BeautifulSoup gibi popüler Python kütüphanelerini kullanır. İlk olarak, belirtilen URL'deki web sayfasını analiz eder ve içerisinde bulunan formları tespit eder. Daha sonra, her bir formun ayrıntılarını çıkarır ve formun hedef URL'sini belirler. Ardından, formdaki input alanlarının değerlerini değiştirerek SQL enjeksiyonu saldırılarını simüle eder.

Aracın çalışma prensibi şu şekildedir: Her bir form için, belirli bir SQL enjeksiyonu ifadesi (payload) eklenmiş bir payload verisi oluşturulur ve bu veri, formun methoduna göre POST veya GET isteği ile gönderilir. Yanıt analiz edilir ve içinde SQL enjeksiyonu açığına işaret eden belirli hataların bulunup bulunmadığı kontrol edilir. Eğer bir açık tespit edilirse, ilgili URL bildirilir.

CTF yarışmalarında hız kazandıran bir araç olarak işinize yarayabilir.

 SQL Injection Scanner'ı yetkisiz erişim elde etmek veya zarar vermek amacıyla kullanmayınız.  Aracı sadece kendi sistemlerinizde veya yetkilendirdiğiniz sistemlerde kullanarak, yasaları ihlal etmeden çalışınız.
