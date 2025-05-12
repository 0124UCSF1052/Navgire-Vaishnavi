import webbrowser
import random
from tabulate import tabulate


songsubject = {
    '1': {
        'name': 'Arijit Singh',
        'genre': {
            'Romantic': [
                {'name': 'Tum Hi Ho', 'url': 'https://www.youtube.com/watch?v=Umqb9KENgmk'},
                {'name': 'Raabta', 'url': 'https://youtu.be/zlt38OOqwDc?si=mKMX3ILu4HHzdwZi'},
                {'name': 'Agar Tum Saath Ho', 'url': 'https://youtu.be/xRb8hxwN5zc?si=1FJ3FMYLi21FnO3a'}
            ],
            'Sad': [
                {'name': 'Channa Mereya', 'url': 'https://youtu.be/284Ov7ysmfA?si=vO5hIo3x4TreyNey'},
                {'name': 'Tujhe Kitna Chahne Lage', 'url': 'https://youtu.be/AgX2II9si7w?si=kSbu5otHBlqZ-8fB'},
                {'name': 'Hamari Adhuri Kahani', 'url': 'https://youtu.be/f3FFOBrMmdg?si=Fnn86Le3tYUlPfIo'}
            ],
            'Happy': [
                {'name': 'Ilahi', 'url': 'https://youtu.be/fdubeMFwuGs?si=mSovzS43m8WxChyX'},
                {'name': 'Hairat', 'url': 'https://youtu.be/wqTQNs9sO6M?si=lQcBrgTX7luyJPp5'},
                {'name': 'Phir Se Ud Chala', 'url': 'https://youtu.be/-3gQ6HIkRys?si=R1SBQ5mfQMFeCeJY'}
            ]
        }
    },
    '2': {
        'name': 'Sunidhi Chauhan',
        'genre': {
            'Romantic': [
                {'name': 'Be Intehaan', 'url': 'https://youtu.be/nPhHtahBlyI?si=5LgJy12E2HId_AV0'},
                {'name': 'Bin Tere', 'url': 'https://youtu.be/JPZxMhZ4KDw?si=IGbFV4s3Plxp_Cyk'},
                {'name': 'Darkhast', 'url': 'https://youtu.be/LMnJp_dSdnw?si=xSCTTDjwi1VDezBP'}
            ],
            'Sad': [
                {'name': 'Bhage Re Mann', 'url': 'https://youtu.be/pkV4VbjIcCo?si=eEW5dd4CKqtKWVN_'},
                {'name': 'Yaariyan', 'url': 'https://youtu.be/_VKsl6E-ZSk?si=-7tab7xr7hvV6Ok4'},
                {'name': 'Aa Zara', 'url': 'https://youtu.be/Vy0Wy88sXuA?si=a0cjBKWi7wMExIyy'}
            ],
            'Happy': [
                {'name': 'Desi Girl', 'url': 'https://youtu.be/wDIrpvH8MzE?si=z_FvpBAUrbn1O0nH'},
                {'name': 'Chor Bazari', 'url': 'https://youtu.be/sDne5fEsxec?si=J72lklhXhrP32lfZ'},
                {'name': 'Dance Pe Chance', 'url': 'https://youtu.be/rap8SoUIPaw?si=h_E-5Fn8epgzuSXu'}
            ]
        }
    },
    '3': {
        'name': 'Shreya Ghoshal',
        'genre': {
            'Romantic': [
                {'name': 'Teri Ore', 'url': 'https://youtu.be/GLEx6bhPu7s?si=pJGGRfjxKmX1OfZl'},
                {'name': 'Saans', 'url': 'https://youtu.be/WLXkcfvc4Lk?si=j7JOS7_VflTQ8q7_'},
                {'name': 'Laal Ishq', 'url': 'https://youtu.be/TuJXwmHmwhQ?si=k4csTTeXbwWlBCEv'}
            ],
            'Sad': [
                {'name': 'Sun Raha Hai', 'url': 'https://youtu.be/inEu2qQuGZ8?si=bpZ1V6tVtixe7qBd'},
                {'name': 'Dola Re Dola', 'url': 'https://youtu.be/lzdB7JBrF-c?si=vz_m7Jt7uSZTOywl'},
                {'name': 'Yeh Ishq Hai', 'url': 'https://youtu.be/dXpG0kavjUo?si=lRizReIw8DU5aWC8'}
            ],
            'Happy': [
                {'name': 'Barso Re', 'url': 'https://youtu.be/asw-wTDzGUQ?si=sNhKYwlDK0srW2gy'},
                {'name': 'Pal', 'url': 'https://youtu.be/w8LcxY43N5Y?si=sUAKdlKVH6HM42ej'},
                {'name': 'Radha', 'url': 'https://youtu.be/52deq20h6Q4?si=eIYQWVqKAEpJWGK3'}
            ]
        }
    },
    '4': {
        'name': 'Armaan Malik',
        'genre': {
            'Romantic': [
                {'name': 'Bol Do Na Zara', 'url': 'https://youtu.be/EpEraRui1pc?si=4S2tnsF2KLbtNyRG'},
                {'name': 'Pehla Pyaar', 'url': 'https://youtu.be/B7SkAq_94J8?si=H4-CHC0aHs3M1yLy'},
                {'name': 'Jab Tak', 'url': 'https://youtu.be/K-Ts-NFR62o?si=I6IKXCdPHmW_7kr2'}
            ],
            'Sad': [
                {'name': 'Wajah Tum Ho', 'url': 'https://youtu.be/__ZvXBf1rmw?si=Paykcstp172M1viM'},
                {'name': 'Kaun Tujhe', 'url': 'https://youtu.be/atVof3pjT-I?si=iyPfKfHNrYp48jK6'},
                {'name': 'Main Rahoon Ya Na Rahoon', 'url': 'https://youtu.be/Dp6lbdoprZ0?si=ykc7F4ie35NNkwEI'}
            ],
            'Happy': [
                {'name': 'Sab Tera', 'url': 'https://youtu.be/WRQHV3kDcyo?si=3HBnwp3UyKrfpcln'},
                {'name': 'Control', 'url': 'https://youtu.be/ABG0gQ9czvk?si=7kpSddptbdxPbiAJ'},
                {'name': 'Next 2 Me', 'url': 'https://youtu.be/NXgLhgIpU-Y?si=uMdU0pu5hv7meetg'}
            ]
        }
    }
}

myplay = []

def find_song_url_by_name(artist, genre, song_name):
    for song in songsubject[artist]['genre'][genre]:
        if song['name'].lower() == song_name.lower():
            return song['url']
    return None

def view_songs():
    table = []
    for singer in songsubject.values():
        for genre, songs in singer['genre'].items():
            for song in songs:
                table.append([singer['name'], genre, song['name'], song['url']])
    print(tabulate(table, headers=["Artist", "Genre", "Song Name", "YouTube Link"], tablefmt="fancy_grid"))

def update_songs():
    print("\nAvailable Artists:")
    for sid, info in songsubject.items():
        print(f"- {info['name']}")
    artist = input("Enter artist name to update songs: ").strip().title()
    for sid, info in songsubject.items():
        if info['name'] == artist:
            print("Available genres:", ", ".join(info['genre'].keys()))
            genre = input("Enter genre: ").strip().capitalize()
            if genre in info['genre']:
                print("\nExisting Songs:")
                for idx, s in enumerate(info['genre'][genre]):
                    print(f"{idx+1}. {s['name']}")
                print("\n1. Add song\n2. Delete song\n")
                choice = input("Enter choice: ")
                if choice == '1':
                    name = input("Enter song name to add (must already exist in list): ")
                    url = find_song_url_by_name(sid, genre, name)
                    if url:
                        new_song = {'name': name, 'url': url}
                        info['genre'][genre].append(new_song)
                        myplay.append(new_song)
                        print("✅ Song added to your playlist.")
                    else:
                        print("❌ Song not found in existing list.")
                elif choice == '2':
                    idx = int(input("Enter song number to delete: ")) - 1
                    removed_song = info['genre'][genre].pop(idx)
                    myplay[:] = [s for s in myplay if s['name'] != removed_song['name']]
                    print("🗑 Song deleted from both list and playlist.")
               
                return
    print("❌ Artist or genre not found.")


def create_playlist():
    while True:
        print("\nArtists:")
        for sid, val in songsubject.items():
            print(f"- {val['name']}")
        artist_input = input("Enter artist name: ").strip().title()
        
        
        artist_id = None
        for sid, val in songsubject.items():
            if val['name'] == artist_input:
                artist_id = sid
                break

        if not artist_id:
            print("❌ Artist not found.")
            continue

        while True:
            genres = list(songsubject[artist_id]['genre'].keys())
            print("Available genres:", ", ".join(genres))
            genre = input("Enter genre: ").strip().capitalize()

            if genre not in songsubject[artist_id]['genre']:
                print("❌ Genre not found.")
                continue

            songs = songsubject[artist_id]['genre'][genre]
            for idx, song in enumerate(songs):
                print(f"{idx+1}. {song['name']}")
            
            try:
                snum = int(input("Choose song number to add to playlist: ")) - 1
                if 0 <= snum < len(songs):
                    song = songs[snum]
                    if song not in myplay:
                        myplay.append(song)
                        print(f"🎧 Added '{song['name']}' to playlist.")
                    else:
                        print("⚠ Song already in playlist.")
                else:
                    print("❌ Invalid song number.")
            except ValueError:
                print("❌ Please enter a valid number.")

            
            cont = input("Do you want to add more? (y/n): ").lower()
            if cont != 'y':
                show_playlist()
                return

            
            change_genre = input("Do you want to change genre? (y/n): ").lower()
            if change_genre == 'y':
                continue  
            
        
            change_artist = input("Do you want to change artist? (y/n): ").lower()
            if change_artist == 'y':
                break  
            else:
                continue  


def show_playlist():
    if not myplay:
        print("\n🎵 Playlist is empty.")
    else:
        print("\n🎶 Your Playlist:")
        table = [[idx + 1, song['name'], song['url']] for idx, song in enumerate(myplay)]
        print(tabulate(table, headers=["#", "Song Name", "YouTube Link"], tablefmt="fancy_grid"))

def play_playlist():
    if not myplay:
        print("\n🎵 Playlist is empty.")
        return
    
    print("\nPlay songs in:")
    print("1. Sequence")
    print("2. Shuffle")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        print("\n🎧 Playing songs in order...")
        for song in myplay:
            print(f"▶ Now playing: {song['name']}")
            webbrowser.open(song['url'])
    elif choice == '2':
        print("\n Shuffling playlist and playing...")
        shuffled = myplay[:]
        random.shuffle(shuffled)
        for song in shuffled:
            print(f"▶ Now playing: {song['name']}")
            webbrowser.open(song['url'])
    else:
        print("❌ Invalid choice.")

# Main menu loop
while True:
    print("\nMENU:")
    print("1. View all songs")
    print("2. Update song list")
    print("3. Create playlist")
    print("4. Show created playlist")
    print("5. Play playlist")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_songs()
    elif choice == '2':
        update_songs()
    elif choice == '3':
        create_playlist()
    elif choice == '4':
        show_playlist()
    elif choice == '5':
        play_playlist()
    elif choice == '6':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice.")