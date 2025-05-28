#  OrangeHRM UI Test Automation (Selenium + Python + PyTest)

Bu proje, [OrangeHRM Demo UygulamasÄ±](https://opensource-demo.orangehrmlive.com/) Ã¼zerinde temel kullanÄ±cÄ± arayÃ¼zÃ¼ testlerini otomatikle?tirir.  
Testler `pytest` ile yazÄ±lmÄ±?tÄ±r ve `Selenium WebDriver` kullanÄ±r.

---

##  Ba?larken

### ?“¦ Gereksinimler

- Python 3.8 veya Ã¼stÃ¼
- Google Chrome
- ChromeDriver (tarayÄ±cÄ± sÃ¼rÃ¼mÃ¼ne uyumlu)
- pip (Python paket yÃ¶neticisi)

### ?”§ Kurulum

```bash
git clone https://github.com/umutenginberkkan/qualityAssuranceProject.git
cd orangehrm-automation
pip install -r requirements.txt```


## ?? Testleri Cal??t?rma

Tum testleri cal??t?rmak icin terminalde ?u komutu yaz?n:

```bash
pytest test_orangehrm.py```

## Test Kapsam?

test_valid_login
¡÷ Do?ru kullan?c? ad? ve ?ifre ile ba?ar?l? giri? yap?labiliyor mu?

test_invalid_login
¡÷ Hatal? bilgilerle giri? yap?ld???nda ¡§Invalid credentials¡¨ uyar?s? gosteriliyor mu?

test_empty_fields
¡÷ E-posta veya ?ifre alan? bo? b?rak?ld???nda gerekli uyar?lar c?k?yor mu?

test_logout
¡÷ Ba?ar?l? giri? sonras? kullan?c? sistemden duzgun bir ?ekilde c?k?? yapabiliyor mu?

test_admin_page_navigation
¡÷ Kullan?c? ¡§Admin¡¨ menusune t?klad???nda do?ru sayfaya yonlendiriliyor mu? (admin/viewSystemUsers)
