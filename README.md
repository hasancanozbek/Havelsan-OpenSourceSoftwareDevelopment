1. Aşama :
   - Basit bir Flask uygulaması yazıldı. Bu API için temel get ve post istekleri tanımlandı.
  
2. Aşama :
   - Açık kaynak hazır api servisine (dünya üzerindeki gerçek zamanlı depremler) belirli parametreler ile istek atıldı ve çıktı json formatında ekrana bastırıldı.
  
3. Aşama
   - Yazılan ilk API'ye nginx ve gunicorn servisleri eklendi. Böylelikle API bir servis haline getirildi ve load balancer içeren bir yapıya evrildi.
     
4. Aşama
   - Yazılan ilk flask uygulamasına docker desteği getirildi. Docker Compose ile proje ayağa kaldırıldı.
