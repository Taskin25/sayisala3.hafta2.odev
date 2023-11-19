# Exponential fonksiyonu
def exp(x):
    term = 1.0
    sum = 1.0

    for i in range(1, 10):
        term *= x / i
        sum += term

    return sum

# Fonksiyonu temsil eden method
def fonksiyon(x):
    return 4 * exp(-0.5 * x) - x

# Türevi hesaplayan method
def turev(x):
    return -2 * exp(-0.5 * x) - 1

# Newton-Raphson yöntemi
def newton_raphson(x0, epsilon, max_iter):
    iterasyon = 0
    x = x0

    while iterasyon < max_iter:
        f = fonksiyon(x)
        f_prime = turev(x)

        # İterasyon formülü
        x = x - f / f_prime

        # Epsilon değeri ile karşılaştırma
        if -epsilon < f < epsilon:
            break

        iterasyon += 1

    return x

# Başlangıç değeri, bağıl hata payı ve maksimum iterasyon sayısı
x0 = 2
epsilon = 1e-6
max_iter = 1000

# Newton-Raphson yöntemini uygula
kok = newton_raphson(x0, epsilon, max_iter)

# Sonuç olarak bulunan kökü yazdır
print("Bulunan kök:", kok)