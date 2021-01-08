from django.shortcuts import render, redirect
from .models import DataPasien
from .forms import PasienForms
# Flash messages
from django.contrib import messages
# Create your views here.
def index(request):
    data_pasien = DataPasien.objects.all()
    context     = {
        'page_title':'Home',
        'action':'Tabel Data Pasien',
        'data_pasien':data_pasien,
    }
    return render(request,'index.html',context)

def create(request):
    forms       = PasienForms(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect('dataPasien:index')

    context     = {
        'page_title':'Create',
        'action':'Tambah Data Pasien',
        'forms':forms,
    }
    return render(request,'create.html',context)

def update(request,update_id):
    pasien_update   = DataPasien.objects.get(id=update_id)
    Data      = {
        'nama':pasien_update.nama,
        'alamat':pasien_update.alamat,
        'kota':pasien_update.kota,
        'no_telepon':pasien_update.no_telepon,
    }
    forms           = PasienForms(request.POST or None, initial=Data, instance=pasien_update)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return redirect('dataPasien:index')

    context     = {
        'page_title':'Create',
        'action':'Perbaharuin Data Pasien',
        'forms':forms,
    }
    return render(request,'update.html',context)

def delete(request,delete_id):
    pasien_delete   = DataPasien.objects.get(id=delete_id)
    if request.POST.get('hapus') == 'Hapus':
        messages.success(request, f'Data Pasien {pasien_delete.nama} Berhasil Dihapus Dari Database')
        pasien_delete.delete()
        return redirect('dataPasien:index')
    elif request.POST.get('batal') == 'Batal':
        messages.success(request, f'Data Pasien {pasien_delete.nama} Tidak Dihapus Dari Database')
        return redirect('dataPasien:index')

    context     = {
        'page_title':'Delete',
        'action':'Hapus Data Pasien',
        'data':pasien_delete,
    }
    return render(request,'delete.html',context)
