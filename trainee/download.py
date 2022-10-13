import os
from pytube import YouTube

def open_site(line):
    if "https://" in line:
        os.system('start ' + line)      
    elif "www." in line:
        line = "https://" + line
        os.system("start " + line)
    else:
        line = "https://www." + line
        os.system("start " + line)


def download(link):
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download Successful !!")
    print(f"Title of your video - {yt.title}")

def main():
    print("Hi bro, you want to open the site or download the video? 'o' 'd', if you wanna exit press 'e'")
    choice = input()
    while choice != "e":
        if choice == "o":
            print("What the site do you want to open?")
            line = input()
            open_site(line)
            print("| Opening... |")
        elif choice == "d":
            print("What the video you want to download?")
            try:
                link = str(input("Enter Your Link: "))
                download(link)               
            except:
                print("!!! It's wrong, try another time !!!")
        else:
            print("You made mistake, try one more time!")
        choice = input("What we goona do?\n")
        if choice == "e":
            print("Goodbuy, bro :(")

        

if __name__ == "__main__":
    main()
