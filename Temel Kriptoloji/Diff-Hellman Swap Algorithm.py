# 1. Genel Sayılar: Herkesin bildiği p ve g değerleri
# p: Büyük bir asal sayı olmalı (örnek için küçük bir sayı seçildi)
p = 23
# g: p'nin bir primitif kökü olmalı
g = 5

print("--- Adım 1: Genel Sayılar ---")
print("Herkesin bildiği asal sayı (p): {}".format(p))
print("Herkesin bildiği primitif kök (g): {}\n".format(g))


# 2. Gizli Sayı Seçimi: Ali ve Veli kendi gizli sayılarını seçer
# Ali'nin gizli sayısı (bu sayı asla paylaşılmaz)
a = 4
# Veli'nin gizli sayısı (bu sayı asla paylaşılmaz)
b = 3

print("--- Adım 2: Gizli Sayıların Seçimi ---")
print("Ali'nin gizli sayısı (a): {}".format(a))
print("Veli'nin gizli sayısı (b): {}\n".format(b))


# 3. Genel Anahtar Oluşturma: Her taraf kendi genel anahtarını oluşturur ve diğerine gönderir
# Ali, A = g^a mod p formülüyle kendi genel anahtarını hesaplar.
# pow(taban, us, mod)
# Not: Python'da (g**a) % p yerine pow(g, a, p) kullanmak büyük sayılar için daha verimlidir.

A = pow(g, a, p)

# Veli, B = g^b mod p formülüyle kendi genel anahtarını hesaplar.
B = pow(g, b, p)

print("--- Adım 3: Genel Anahtarların Oluşturulması ve Paylaşılması ---")
print("Ali'nin hesapladığı genel anahtar (A): {} ^ {} mod {} = {}".format(g, a, p, A))
print("Veli'nin hesapladığı genel anahtar (B): {} ^ {} mod {} = {}".format(g, b, p, B))
print("-> Ali, A={} değerini Veli'ye gönderir.".format(A))
print("-> Veli, B={} değerini Ali'ye gönderir.\n".format(B))


# 4. Ortak Gizli Anahtar Oluşturma: Her taraf, gelen genel anahtarı kendi gizli sayısıyla işler
# Ali, Veli'den aldığı B değerini kullanarak ortak gizli anahtarı (s) hesaplar: s = B^a mod p
s_ali_hesabi = pow(B, a, p)

# Veli, Ali'den aldığı A değerini kullanarak ortak gizli anahtarı (s) hesaplar: s = A^b mod p
s_veli_hesabi = pow(A, b, p)

print("--- Adım 4: Ortak Gizli Anahtarın Hesaplanması ---")
print("Ali'nin hesapladığı ortak anahtar (s): B^a mod p => {} ^ {} mod {} = {}".format(B, a, p, s_ali_hesabi))
print("Veli'nin hesapladığı ortak anahtar (s): A^b mod p => {} ^ {} mod {} = {}\n".format(A, b, p, s_veli_hesabi))


# 5. Sonuç: Her iki taraf da aynı gizli sayıya ulaşır
print("--- Adım 5: Sonuç ---")
if s_ali_hesabi == s_veli_hesabi:
    print("BAŞARILI! Her iki taraf da aynı ortak gizli anahtara ulaştı: {}".format(s_ali_hesabi))
    print("Bu anahtar artık güvenli olmayan kanal üzerinden simetrik şifreleme yapmak için kullanılabilir.")
else:
    print("HATA! Hesaplanan anahtarlar birbiriyle eşleşmiyor.")