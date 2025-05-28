# 🧪 OrangeHRM UI Test Automation (Selenium + Python + PyTest)

Bu proje, [OrangeHRM Demo Uygulaması](https://opensource-demo.orangehrmlive.com/) üzerinde temel kullanıcı arayüzü testlerini otomatikleştirir.  
Testler `pytest` ile yazılmıştır ve `Selenium WebDriver` kullanır.

---

## 🚀 Başlarken

### Gereksinimler

- Python 3.8 veya üzeri
- Google Chrome
- ChromeDriver (tarayıcı sürümüne uyumlu)
- pip (Python paket yöneticisi)

### Kurulum

```bash
git clone https://github.com/umutenginberkkan/qualityAssuranceProject.git
cd orangehrm-automation
pip install -r requirements.txt
```

---

## 🧪 Testleri Çalıştırma

Tüm testleri çalıştırmak için terminalde şu komutu yazın:

```bash
pytest test_orangehrm.py
```

> Tarayıcı varsayılan olarak `headless` (görünmez) çalışır. Tarayıcının açılmasını isterseniz test dosyasındaki `--headless` satırını kaldırın.

---

## ✅ Test Kapsamı

**test_valid_login**  
→ Doğru kullanıcı adı ve şifre ile başarılı giriş yapılabiliyor mu?

**test_invalid_login**  
→ Hatalı bilgilerle giriş yapıldığında “Invalid credentials” uyarısı gösteriliyor mu?

**test_empty_fields**  
→ E-posta veya şifre alanı boş bırakıldığında gerekli uyarılar çıkıyor mu?

**test_logout**  
→ Başarılı giriş sonrası kullanıcı sistemden düzgün bir şekilde çıkış yapabiliyor mu?

**test_admin_page_navigation**  
→ Kullanıcı “Admin” menüsüne tıkladığında doğru sayfaya yönlendiriliyor mu? (`admin/viewSystemUsers`)

