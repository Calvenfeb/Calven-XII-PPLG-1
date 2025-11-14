# nested = bersarang
# di dalam if / elif / else ada conditional

# CERITA HOROR

print("Malam itu XII PPLG 1 sepi banget, cuma kamu dan suara kipas yang kedengaran mau pensiun.")
print("Di atas meja, ada kerupuk pocong yang masih utuh.")
print("1. Makan kerupuknya")
print("2. Cuekin aja")
choice = int(input("= "))

if choice == 1:
    print("Kamu gigit kerupuknya...")
    print("Tiba-tiba kerupuk itu jerit: 'JANGAAAN!!'")
    print("Dari pojok kelas, muncul pocong yang mukanya kayak abis begadang 3 hari.")
    print("1. Say hi 'halo bang'")
    print("2. Kabur sambil bawa kursi")
    choice = int(input("= "))
    if choice == 1:
        print("Pocongnya bengong, terus malah ngajak selfie.")
        print("Kamu viral di TikTok.")
        print("GOOD END")
    elif choice == 2:
        print("Kamu kabur tapi kepleset sisa es teh.")
        print("Pocongnya ketawa sampe ikatannya mau lepas.")
        print("BAD END")
    else:
        print("Kamu diem aja kayak patung manaquin.")
        print("Pocongnya kesel dan ngelempar spidol.")
        print("BAD END")

elif choice == 2:
    print("Kamu cuek dan duduk santai.")
    print("Kerupuk itu gerak sendiri... nyamperin kamu.")
    print("1. Tendang kerupuknya")
    print("2. pura-pura mati")
    choice = int(input("= "))
    if choice == 1:
        print("Kamu tendang, kerupuknya mental ke tembok.")
        print("Tiba-tiba berubah jadi hantu emak-emak galak.")
        print("NORMAL END")
    elif choice == 2:
        print("Kamu pura-pura mati, tapi malah ketiduran beneran.")
        print("Pas bangun, udah jam 7 pagi dan kelas rame.")
        print("Kamu selamat.")
        print("GOOD END")
    else:
        print("Kamu bingung mau apa.")
        print("Kerupuknya naik ke pundakmu dan bisik: 'ikut aku…'")
        print("BAD END")

else:
    print("Pilihan tidak ada dalam dunia perkerupukan.")
    print("Kerupuknya marah dan berubah jadi bos final.")
    print("BAD END")
