# ImageDetect

Bu repository, DeepFace kütüphanesini kullanarak yüz analizi ve doğrulama için bir grafik arayüzü (GUI) uygulamasını içerir. Uygulama, grafik arayüzü için tkinter kütüphanesini kullanır ve görüntü analizi ve veritabanı etkileşimi için DeepFace, PIL ve diğer Python kütüphanelerini kullanır. Kullanıcıların iki resim seçmelerine izin verir ve yüz analizi yaparak resimlerin aynı kişiye mi yoksa farklı kişilere mi ait olduğunu kontrol eder. Sonuçlar GUI'de görüntülenir ve bilgiler bir PostgreSQL veritabanına kaydedilebilir.

## Gereksinimler

- Python 3.x
- tkinter
- deepface
- PIL
- opencv-python
- matplotlib
- cmake
- dlib
- pandas
- tensorflow
- tqdm
- gdown
- psycopg2

Gereksinim duyulan paketleri aşağıdaki komutla pip ile yükleyebilirsiniz:

```bash
pip install deepface opencv-python matplotlib cmake dlib pandas tensorflow tqdm gdown psycopg2
```
##Kullanım
Depoyu yerel makinenize klonlayın.
Depo dizinine gidin.
##Uygulamayı Çalıştırma
Yüz analizi ve doğrulama arayüzünü çalıştırmak için aşağıdaki komutu kullanın:
```
bash
Copy code
python app.py
```
Kullanıcı Arayüzü
GUI penceresi, birinci ve ikinci resmi seçmek için iki düğme ile açılacaktır.
"Birinci Fotoğrafı Seçin" düğmesine tıklayarak bilgisayarınızdan ilk resmi seçin.
"İkinci Fotoğrafı Seçin" düğmesine tıklayarak bilgisayarınızdan ikinci resmi seçin.
Her iki resmi de seçtikten sonra, "Analiz Et" düğmesine tıklayarak yüz analizi ve doğrulama işlemini yapın.
Analiz sonuçları GUI'de gösterilecek, resimlerin aynı kişiye mi yoksa farklı kişilere mi ait olduğu görüntülenecektir. 
Her resim için cinsiyet, yaş ve baskın duygu gibi ek bilgiler de görüntülenecektir.
Sonuçlar ayrıca bir PostgreSQL veritabanına kaydedilecektir. Veritabanı bağlantı bilgilerini, connect_to_database fonksiyonunda düzenleyebilirsiniz.

Not:Seçilen resimlerin, doğru analiz için tespit edilebilir yüzler içermesi gerekmektedir.
Uygulama, yüz analizi ve doğrulama için DeepFace kütüphanesini kullanmaktadır. Bu uygulamada kullanılan analiz ve doğrulama yöntemleri hakkında daha fazla bilgi için DeepFace belgelerine başvurabilirsiniz.
Kodu keşfetmeye ve ihtiyaçlarınıza göre düzenlemeye çekinmeyin. Herhangi bir sorunuz veya sorununuz olursa lütfen çekinmeden iletişime geçin. İyi yüz analizleri ve doğrulamaları dileriz!


