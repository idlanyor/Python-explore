import matplotlib.pyplot as plt
import pandas as pd

# Data
# Panda excel
data = pd.read_excel("./karangreja.xlsx", sheet_name="Total")
# Data
kelurahan = data["Kelurahan"].tolist()
tidak_sekolah = [49, 63, 74, 80, 29, 27, 20]
tidak_sekola = data[1:0]
for i in tidak_sekola:
    print(tidak_sekola[i])
belum_tamat_sd = [15, 32, 26, 53, 15, 17, 24]
tamat_sd = [1940, 1465, 1670, 1958, 1156, 980, 791]
sltp = [470, 381, 404, 486, 367, 324, 295]
slta = [174, 172, 215, 317, 208, 334, 131]
diploma_i_ii = [2, 2, 2, 1, 6, 4, 4]
akademi_diploma_iii = [2, 4, 4, 11, 7, 10, 4]
diploma_iv_strata_i = [38, 14, 20, 51, 29, 47, 22]
strata_ii = [1, 2, 2, 1, 0, 1, 0]


# Plot
plt.figure(figsize=(12, 8))

plt.bar(kelurahan, tidak_sekolah, label="Tidak/ Belum Sekolah")
plt.bar(
    kelurahan, belum_tamat_sd, bottom=tidak_sekolah, label="Belum Tamat SD/ Sederajat"
)
plt.bar(
    kelurahan,
    tamat_sd,
    bottom=[tidak_sekolah[i] + belum_tamat_sd[i] for i in range(len(tidak_sekolah))],
    label="Tamat SD/ Sederajat",
)
plt.bar(
    kelurahan,
    sltp,
    bottom=[
        tidak_sekolah[i] + belum_tamat_sd[i] + tamat_sd[i]
        for i in range(len(tidak_sekolah))
    ],
    label="SLTP/ Sederajat",
)
plt.bar(
    kelurahan,
    slta,
    bottom=[
        tidak_sekolah[i] + belum_tamat_sd[i] + tamat_sd[i] + sltp[i]
        for i in range(len(tidak_sekolah))
    ],
    label="SLTA/ Sederajat",
)
plt.bar(
    kelurahan,
    diploma_i_ii,
    bottom=[
        tidak_sekolah[i] + belum_tamat_sd[i] + tamat_sd[i] + sltp[i] + slta[i]
        for i in range(len(tidak_sekolah))
    ],
    label="Diploma I/II",
)
plt.bar(
    kelurahan,
    akademi_diploma_iii,
    bottom=[
        tidak_sekolah[i]
        + belum_tamat_sd[i]
        + tamat_sd[i]
        + sltp[i]
        + slta[i]
        + diploma_i_ii[i]
        for i in range(len(tidak_sekolah))
    ],
    label="Akademi/ Diploma III/ Sarjana Muda",
)
plt.bar(
    kelurahan,
    diploma_iv_strata_i,
    bottom=[
        tidak_sekolah[i]
        + belum_tamat_sd[i]
        + tamat_sd[i]
        + sltp[i]
        + slta[i]
        + diploma_i_ii[i]
        + akademi_diploma_iii[i]
        for i in range(len(tidak_sekolah))
    ],
    label="Diploma IV/ Strata I",
)
plt.bar(
    kelurahan,
    strata_ii,
    bottom=[
        tidak_sekolah[i]
        + belum_tamat_sd[i]
        + tamat_sd[i]
        + sltp[i]
        + slta[i]
        + diploma_i_ii[i]
        + akademi_diploma_iii[i]
        + diploma_iv_strata_i[i]
        for i in range(len(tidak_sekolah))
    ],
    label="Strata II",
)

plt.xlabel("Kelurahan")
plt.ylabel("Jumlah")
plt.title("Data Pendidikan Terakhir se-Kecamatan Karangreja")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
