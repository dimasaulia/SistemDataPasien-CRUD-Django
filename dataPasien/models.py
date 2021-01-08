from django.db import models

# Create your models here.
class DataPasien(models.Model):
    no_pasien   = models.CharField(max_length=7)
    nama        = models.CharField(max_length=30)
    alamat      = models.CharField(max_length=30)
    kota        = models.CharField(max_length=30)
    no_telepon  = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.id}-{self.nama}"

    def save(self):
        if self.no_pasien:
            pass
        else:
            jumlah_data         = DataPasien.objects.all().count()
            base_num            = 209413
            print("blmm")
            if int(jumlah_data) == 0:
                self.no_pasien      = int(jumlah_data) + base_num
            else:
                data_terakhir   = DataPasien.objects.latest('id')
                self.no_pasien  = int(data_terakhir.no_pasien) + 1

        super(DataPasien, self).save()
