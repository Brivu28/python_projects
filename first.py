import json

def listt(video):
    for index, vid in enumerate(video, start=1):
        print(f"{index}. Name: {vid['Name']}, Time: {vid['Time']}")

def addV(video):
    name = input("Enter The Name: ")
    time = input("Enter The Time: ")
    video.append({"Name": name, "Time": time})
    save(video)

def upt(video):
    listt(video)
    index = int(input("Enter The Index Of The video"))
    if (index >=1 and index <= len(video)-1):
        name = input("Enter The Name")
        time = input("Enter The Time")
        video[index - 1]['Name'] = name
        video[index - 1]['Time'] = time
        save(video)

def delt(video):
    list(video)
    index = int(input("Enter The Index Of The video"))
    del video[index -1]
    save(video)
    

def loadData():
    try:
        with open('youtube.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

def save(video):
    with open('youtube.txt', 'w') as f:
        json.dump(video, f)

def main():
    video = loadData()
    while True:
        print("\nYouTube Manager")
        print("1. List All YouTube Videos")
        print("2. Add A YouTube Video")
        print("3. Update A YouTube Video")
        print("4. Delete A Video")
        print("5. Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            listt(video)
        elif choice == '2':
            addV(video)
        elif choice == '3':
            upt(video)
        elif choice == '4':
            delt(video)
        elif choice == '5':
            save(video)
            break
        else:
            print("Invalid choice, please select from the menu.")

if __name__ == "__main__":
    main()
