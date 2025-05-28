#  OrangeHRM UI Test Automation (Selenium + Python + PyTest)

Bu proje, [OrangeHRM Demo Uygulamas覺](https://opensource-demo.orangehrmlive.com/) 羹zerinde temel kullan覺c覺 aray羹z羹 testlerini otomatikle?tirir.  
Testler `pytest` ile yaz覺lm覺?t覺r ve `Selenium WebDriver` kullan覺r.

---

##  Ba?larken

###  Gereksinimler

- Python 3.8 veya 羹st羹
- Google Chrome
- ChromeDriver (taray覺c覺 s羹r羹m羹ne uyumlu)
- pip (Python paket y繹neticisi)

###  Kurulum

```bash
git clone https://github.com/umutenginberkkan/qualityAssuranceProject.git
cd orangehrm-automation
pip install -r requirements.txt


##  Testleri Cal??t?rma

Tum testleri cal??t?rmak icin terminalde ?u komutu yaz?n:

```bash
pytest test_orangehrm.py

## Test Kapsam?

test_valid_login
→ Do?ru kullan?c? ad? ve ?ifre ile ba?ar?l? giri? yap?labiliyor mu?

test_invalid_login
→ Hatal? bilgilerle giri? yap?ld???nda “Invalid credentials” uyar?s? gosteriliyor mu?

test_empty_fields
→ E-posta veya ?ifre alan? bo? b?rak?ld???nda gerekli uyar?lar c?k?yor mu?

test_logout
→ Ba?ar?l? giri? sonras? kullan?c? sistemden duzgun bir ?ekilde c?k?? yapabiliyor mu?

test_admin_page_navigation
→ Kullan?c? “Admin” menusune t?klad???nda do?ru sayfaya yonlendiriliyor mu? (admin/viewSystemUsers)
