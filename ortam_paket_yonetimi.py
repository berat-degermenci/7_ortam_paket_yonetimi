"""
Environment (ortam)
    - Bir projenin çalışması için gerekli olan python sürümü, kütüphaneler, paketler gibi bileşenlerin bulunduğu çalışma alanıdır.
    - Bir proje için gerekli python araçlarından bulunduğu izole bir çalışma alanıdır

Neden Kullanılır:
    - farklı projelerde farklı paket sürümleri
    - Proje A:
        - numpy == 1.20
    - Proje B:
        - numpy == 1.26

Virtual Environment (Sanal Ortam)
    - kurulum: python -m venv venv
    - aktif hale getirmek için:  
        - windows:  .\venv\Scripts\activate
        - mac, linux: source venv/bin/activate

Paket yöneticisi (pip)
    - kütüphane = paket
        - numpy: sayısal işlemler
        - pandas: veri analizi
        - matploblit: görselleştirme
    - pythonda paketleri yönetmek için kullanılan araç = pip
        - paket kurabilir
        - silebilir
        - listeleyebilir

Paket kurma:
    - numpy: pip install numpy
    - pandas, matplotlib: pip install pandas matplotlib


requirements.txt
    - bir projenin ihtiyaç duyduğu tüm paketlerin listelendiği dosya
    - bir dosya sayesinde başka bir projeyi kolayca çalıştırabiliriz
    -  pip freeze > requiremnets.txt

    - kurulum:
        - pip install -r .\requirements.txt
"""