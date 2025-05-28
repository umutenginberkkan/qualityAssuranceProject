# ?? OrangeHRM UI Test Automation (Selenium + Python + PyTest)

Bu proje, [OrangeHRM Demo Uygulamas?](https://opensource-demo.orangehrmlive.com/) uzerinde temel kullan?c? arayuzu testlerini otomatikle?tirir.  
Testler `pytest` ile yaz?lm??t?r ve `Selenium WebDriver` kullan?r.

---

## ?? Ba?larken

### Gereksinimler

- Python 3.8 veya uzeri
- Google Chrome
- ChromeDriver (taray?c? surumune uyumlu)
- pip (Python paket yoneticisi)

### Kurulum

```bash
git clone https://github.com/umutenginberkkan/qualityAssuranceProject.git
cd orangehrm-automation
pip install -r requirements.txt
```

---

## ?? Testleri Cal??t?rma

Tum testleri cal??t?rmak icin terminalde ?u komutu yaz?n:

```bash
pytest test_orangehrm.py
```

> Taray?c? varsay?lan olarak `headless` (gorunmez) cal???r. Taray?c?n?n ac?lmas?n? isterseniz test dosyas?ndaki `--headless` sat?r?n? kald?r?n.

---

## ? Test Kapsam?

**test_valid_login**  
¡÷ Do?ru kullan?c? ad? ve ?ifre ile ba?ar?l? giri? yap?labiliyor mu?

**test_invalid_login**  
¡÷ Hatal? bilgilerle giri? yap?ld???nda ¡§Invalid credentials¡¨ uyar?s? gosteriliyor mu?

**test_empty_fields**  
¡÷ E-posta veya ?ifre alan? bo? b?rak?ld???nda gerekli uyar?lar c?k?yor mu?

**test_logout**  
¡÷ Ba?ar?l? giri? sonras? kullan?c? sistemden duzgun bir ?ekilde c?k?? yapabiliyor mu?

**test_admin_page_navigation**  
¡÷ Kullan?c? ¡§Admin¡¨ menusune t?klad???nda do?ru sayfaya yonlendiriliyor mu? (`admin/viewSystemUsers`)

