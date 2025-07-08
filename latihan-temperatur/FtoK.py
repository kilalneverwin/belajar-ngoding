def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

# Contoh penggunaan
fahrenheit_input = float(input("Masukkan suhu dalam Fahrenheit: "))
kelvin_output = fahrenheit_to_kelvin(fahrenheit_input)
print("Hasil konversi ke Kelvin:", kelvin_output)

kelvin_input = float(input("Masukkan suhu dalam Kelvin: "))
fahrenheit_output = kelvin_to_fahrenheit(kelvin_input)
print("Hasil konversi ke Fahrenheit:", fahrenheit_output)
