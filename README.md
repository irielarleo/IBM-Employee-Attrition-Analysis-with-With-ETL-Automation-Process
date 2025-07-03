# Milestone 3

## Repository Outline
1. description.md - Penjelasan gambaran umum project.
2. P2M3_iriel_aureleo_conceptual.txt - Text file yang menjawab Conceptual Problem.
3. P2M3_Iriel_Aureleo_DAG_graph.jpg - File gambar yang memberikan gambaran alur pemrosesan data.
4. P2M3_Iriel_Aureleo_ddl.txt - File text yang berisi command Query yang digunakan pada saat memasukan data kedalam PostgreSQL.
5. P2M3_iriel_aureleo_GX.ipynb - Notebook yang melakukan validasi atas data yang akan digunakan menggunakan Great Expectations.
6. .env - File yang mengatur setting airflow.
7. airflow_ES.yaml - File yang digunakan untuk compose docker container.
8. images - Folder yang berisi 6 gambar visualisasi dan insightnya berserta gambar perkenalan dan kesimpulan.
9. dags
    1. P2M3_iriel_aureleo_DAG.py - Script python yang digunakan airflow dalam pemrosesan data.

## Problem Background
Tingginya tingkat turnover atau attrition karyawan menjadi salah satu tantangan besar yang dihadapi oleh banyak perusahaan global, termasuk di sektor teknologi dan manufaktur. Menurut laporan dari Work Institute (2022), rata-rata perusahaan kehilangan sekitar 1 dari 4 karyawannya setiap tahun, dan biaya penggantian satu karyawan bisa mencapai 30% dari gaji tahunan mereka.

Attrition yang tidak terkelola tidak hanya menurunkan produktivitas, tetapi juga menambah beban biaya untuk perekrutan, pelatihan, dan adaptasi budaya organisasi. Dalam konteks ini, penting bagi perusahaan untuk memahami faktor-faktor yang mendorong karyawan keluar dan bagaimana mencegahnya melalui pendekatan berbasis data.

Sebagai seorang Data Analyst yang bekerja di divisi Human Capital IBM. Project ini bertujuan untuk mengidentifikasi faktor-faktor penting yang berkaitan dengan attrition karyawan. Dengan menggunakan dataset internal IBM, project ini akan menganalisis variabel apa saja yang menyebabkan keputusan karyawan untuk tetap atau keluar dari perusahaan.

## Project Output
Project ini menghasilkan enam visualisasi utama lengkap dengan insight yang diperoleh dari analisis data attrition karyawan di IBM Indonesia. Setiap visualisasi dirancang untuk mengungkap pola-pola penting terkait faktor-faktor apa saja yang menyebabkan karyawan untuk tetap atau keluar dari perusahaan. Output ini bertujuan menjadi dasar pengambilan keputusan strategis bagi Divisi Human Capital dalam menyusun kebijakan retensi dan pengembangan SDM yang lebih efektif guna mendukung pertumbuhan perusahaan.

## Data
Sumber Data : https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset 

Jumlah Kolom : 35

Jumlah Baris : 1470

**Deskripsi Kolom**
| No | Kolom                    | Tipe Data | Deskripsi Singkat                                |
| -- | ------------------------ | --------- | ------------------------------------------------ |
| 1  | Age                      | Numerik   | Usia karyawan                                    |
| 2  | Attrition                | Kategorik | Status keluar atau bertahan di perusahaan        |
| 3  | BusinessTravel           | Kategorik | Frekuensi perjalanan dinas                       |
| 4  | DailyRate                | Numerik   | Tarif kerja harian                               |
| 5  | Department               | Kategorik | Departemen tempat bekerja                        |
| 6  | DistanceFromHome         | Numerik   | Jarak rumah ke kantor (km)                       |
| 7  | Education                | Kategorik | Tingkat pendidikan (1=Di bawah kuliah, 5=Doktor) |
| 8  | EducationField           | Kategorik | Bidang studi pendidikan                          |
| 9  | EmployeeCount            | Numerik   | Selalu bernilai 1 (tidak berguna untuk analisis) |
| 10 | EmployeeNumber           | Numerik   | ID unik karyawan                                 |
| 11 | EnvironmentSatisfaction  | Kategorik | Kepuasan terhadap lingkungan kerja (1–4)         |
| 12 | Gender                   | Kategorik | Jenis kelamin                                    |
| 13 | HourlyRate               | Numerik   | Tarif kerja per jam                              |
| 14 | JobInvolvement           | Kategorik | Tingkat keterlibatan kerja (1–4)                 |
| 15 | JobLevel                 | Kategorik | Level jabatan (1–5)                              |
| 16 | JobRole                  | Kategorik | Peran/jabatan dalam organisasi                   |
| 17 | JobSatisfaction          | Kategorik | Kepuasan terhadap pekerjaan (1–4)                |
| 18 | MaritalStatus            | Kategorik | Status pernikahan                                |
| 19 | MonthlyIncome            | Numerik   | Pendapatan bulanan                               |
| 20 | MonthlyRate              | Numerik   | Tarif kerja per bulan                            |
| 21 | NumCompaniesWorked       | Numerik   | Jumlah perusahaan sebelumnya                     |
| 22 | Over18                   | Kategorik | Apakah usia > 18 tahun (semua “Yes”)             |
| 23 | OverTime                 | Kategorik | Apakah bekerja lembur                            |
| 24 | PercentSalaryHike        | Numerik   | Persentase kenaikan gaji terakhir                |
| 25 | PerformanceRating        | Kategorik | Penilaian kinerja (1–4)                          |
| 26 | RelationshipSatisfaction | Kategorik | Kepuasan hubungan antar rekan kerja (1–4)        |
| 27 | StandardHours            | Numerik   | Jam kerja standar (semua sama)                   |
| 28 | StockOptionLevel         | Kategorik | Level opsi saham (0=Basic, 3=Elite)              |
| 29 | TotalWorkingYears        | Numerik   | Total tahun pengalaman kerja                     |
| 30 | TrainingTimesLastYear    | Numerik   | Frekuensi pelatihan tahun lalu                   |
| 31 | WorkLifeBalance          | Kategorik | Work-life balance (1=Buruk, 4=Terbaik)           |
| 32 | YearsAtCompany           | Numerik   | Lama bekerja di perusahaan saat ini (tahun)      |
| 33 | YearsInCurrentRole       | Numerik   | Lama bekerja di jabatan saat ini                 |
| 34 | YearsSinceLastPromotion  | Numerik   | Tahun sejak promosi terakhir                     |
| 35 | YearsWithCurrManager     | Numerik   | Lama bekerja dengan manajer saat ini             |


## Method
Project ini diselesaikan menggunakan Docker untuk menjalankan Elasticsearch, Kibana, airflow, dan postgreSQL.

## Stacks
Bahasa Pemrograman: Python

Library:
1. pandas
2. great_expectations


Tools/Source Lain:
1. Docker

## Reference
Dataset : 
[IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

Justifikasi :
- [Hasil Riset: 91% Karyawan Startup Ingin Resign](https://finance.detik.com/berita-ekonomi-bisnis/d-6441899/hasil-riset-91-karyawan-startup-ingin-resign#:~:text=Di%20tengah%20tingginya%20keterbukaan%20karyawan%20untuk%20meninggalkan,perekrut%20juga%20memiliki%20tantangan%20dalam%20mempertahankan%20karyawan. )
- [5 Ways to Manage High Turnover : In industries where employees come and go frequently, HR professionals take a comprehensive approach to stem the tide. ](https://www.shrm.org/topics-tools/news/hr-magazine/5-ways-to-manage-high-turnover?utm_source=chatgpt.com)
- [Mengelola Employee Life Cycle: Manfaat serta Tahapannya](https://www.talenta.co/blog/employee-life-cycle/#:~:text=Employee%20life%20cycle%20sendiri%20meng,direkrut%20hingga%20mereka%20meninggalkan%20perusahaan.)
- [Work-Life Balance: Janji atau Budaya Nyata di Perusahaan Anda?](https://www.relasidiri.com/articles/work-life-balance-janji-atau-budaya-nyata-di-perusahaan-anda#:~:text=Menurut%20Harvard%20Business%20Review%2C%20perusahaan%20dengan%20work%2Dlife,perusahaan%20menerapkan%20kebijakan%20work%2Dlife%20balance%20yang%20jelas.)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)v
