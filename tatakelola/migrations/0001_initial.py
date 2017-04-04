# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-31 04:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_proyek', models.CharField(max_length=128)),
                ('latest_step', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('opd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arsitektur_informasi', models.FileField(upload_to='')),
                ('kategori_aplikasi', models.CharField(choices=[('PP', 'Pelayanan Publik'), ('MI', 'Manajemen Internal')], max_length=32)),
                ('infrastruktur_komunkasi', models.FileField(upload_to='')),
                ('infrastruktur_penyimpanan_data', models.FileField(upload_to='')),
                ('organisasi_manajemen_realisasi', models.FileField(upload_to='')),
                ('organisasi_manajemen_operasi', models.FileField(upload_to='')),
                ('organisasi_manajemen_pemeliharaan', models.FileField(upload_to='')),
                ('estimasi_waktu', models.IntegerField(help_text='dalam bulan')),
                ('proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek')),
            ],
        ),
        migrations.CreateModel(
            name='Step2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mekanisme_penganggaran', models.CharField(choices=[('O', 'Pengeluaran Operasi'), ('C', 'Pengeluaran Modal')], max_length=32)),
                ('umur_ekonomis', models.IntegerField(help_text='dalam bulan')),
                ('ketersediaan_anggaran', models.FileField(upload_to='')),
                ('tingkat_kecepatan_keusangan', models.TextField()),
                ('nilai_startegis_tik', models.TextField()),
                ('karakteristik_proyek', models.TextField()),
                ('urgensi', models.TextField()),
                ('ketersediaan_pemasok', models.TextField()),
                ('ketersediaan_sumber_daya', models.TextField()),
                ('capital_budgeting', models.TextField()),
                ('visi', models.TextField()),
                ('misi', models.TextField()),
                ('proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek')),
            ],
        ),
        migrations.CreateModel(
            name='Step3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifikasi_pemeliharaan_alternatif_sistem', models.TextField()),
                ('realisasi_software_aplikasi', models.TextField()),
                ('realisasi_inrastruktur_teknologi', models.TextField()),
                ('realisasi_pengelolaan_data', models.TextField()),
                ('proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek')),
            ],
        ),
        migrations.CreateModel(
            name='Step4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manajemen_tingkat_layanan', models.TextField()),
                ('keamanan_keberlangsungan_sistem', models.TextField()),
                ('manajemen_software_aplikasi', models.TextField()),
                ('manajemen_infratruktur', models.TextField()),
                ('manajemen_data', models.TextField()),
                ('manajemen_pihak_ketiga', models.TextField()),
                ('proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek')),
            ],
        ),
        migrations.CreateModel(
            name='Step5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemeliharaan_software_aplikasi', models.TextField()),
                ('pemeliharaan_infrastruktur_teknologi', models.TextField()),
                ('pemeliharaan_data', models.TextField()),
                ('siklus_hidup_likuidasi_sdit', models.TextField()),
                ('proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatakelola.Proyek')),
            ],
        ),
    ]