from googlesearch import search
import wikipedia as wp
import pyttsx3 as pt
import segno
from pytube import YouTube

def googleSearch(query, result_num=5):
    try: 
        by_user = input("Your Query: ")
        total_results = int(input("How many results do you want: "))
    except ValueError:
        print("Enter a valid entry")
        return

    for urls in search(query=by_user, lang="en", pause=2.0, start=0, stop=total_results):
        print(urls)

def wikiPedia(query, lang, limits=12):
    by_user = input("Search Here: ")
    set_limits = int(input("How many sentences would you expect: "))
    lst = ["en", "ur", "ja"]
    print(lst)
    set_lang = int(input("Choose language: "))
    if set_lang < 0 or set_lang >= len(lst):
        print("Enter a valid entry")
        return

    wp.set_lang(lst[set_lang])
    pedia = wp.search(query=by_user)
    summary = wp.summary(pedia, sentences=set_limits)
    print(summary)

def qrCode(data, fname):
    user_data = input("Enter data: ")
    user_file = input("Enter file name: ")
    qr = segno.make(data)
    qr.save(fname + ".png", border=5, scale=10, dark="purple", light="black")
    qr.show()

def youTube(url, show_info):
    user_url = input("Enter URL: ")
    yt = YouTube(user_url)
    video_info = {
        "Description": yt.description,
        "Views": yt.views,
        "Title": yt.title,
        "Length": yt.length,
        "Rating": yt.rating
    }
    show_info = input("Want to check info? (Y/N): ")
    if show_info.upper() == "Y":
        print(video_info)
    elif show_info.upper() == "N":
        print("Thanks for visiting")
    else:
        print("Enter a valid entry")

    stream = yt.streams.filter(only_video=True).first()
    stream.download()
    print("Download complete!")

def media():
    media_site = ["YouTube", "Wikipedia", "Google search", "QRCode"]

    for index, site in enumerate(media_site):
        print(f"{index}: {site}")

    choice = int(input("Which one do you want: "))

    if choice < 0 or choice >= len(media_site):
        engine = pt.init()
        engine.say("Please enter a valid entry!")
        engine.runAndWait()
        return

    if choice == 0:
        youTube(None, None)
    elif choice == 1:
        wikiPedia(None, None, None)
    elif choice == 2:
        googleSearch(None)
    elif choice == 3:
        qrCode(None, None)
    else:
        engine = pt.init()
        engine.say("Please enter a valid entry!")
        engine.runAndWait()

media()
