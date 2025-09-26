from postprocessor import PostProcessor
from ytdownloader import YTDWrapper
from mediaformats import valid_formats
from datetime import datetime

ydl = YTDWrapper()
pp = PostProcessor()


def ydl_disp_opt():
    opts = [
        "[1] Audio Only",
        "[2] Video Only",
        "[3] Merged",
    ]

    print()
    for line in opts:
        print(line)
    print()


def ydl_select_opt(choice):
    if choice in [1, 2, 3]:
        return choice
    return False


def pp_disp_opt():
    opts = [
        "[1] Compress",
        "[2] Cut",
        "[3] Convert",
        "[4] Quit",
    ]

    print()
    for line in opts:
        print(line)
    print()


def pp_select_opt(choice):
    if choice in [1, 2, 3, 4]:
        return choice
    return False


def check_urls(pass_url):
    valid_domains = ["youtube.com", "youtu.be", "music.youtube.com"]
    if any(domain in pass_url for domain in valid_domains):
        return pass_url
    return False


def main():
    while True:
        download_url = input("Enter the URL: ").strip()
        download_url = check_urls(download_url)

        if not download_url:
            print("Invalid: Not a YouTube link")
            continue
        break

    while True:
        ydl_disp_opt()

        try:
            select_ydl = int(input("Enter download option: "))
            select_ydl = ydl_select_opt(select_ydl)  # returns int | bool
        except ValueError:
            print("Invalid: Must choose a number")
            continue

        if not select_ydl:
            continue
        break

    ydl_opts = {
        1: ydl.audio_only,
        2: ydl.video_only,
        3: ydl.merged,
    }

    ydl_opts[select_ydl]()
    file_path = ydl.start_downloader(download_url)

    if not file_path:  # if YouTube error
        return

    while True:
        pp_disp_opt()

        try:
            select_pp = int(input("Enter processing action: "))
            select_pp = pp_select_opt(select_pp)
        except ValueError:
            print("Invalid: Must choose a number")
            continue

        if not select_pp:
            continue
        break

    if select_pp == 1:  # comp
        while True:
            try:
                target_fs = int(input("Enter target size: "))
            except ValueError:
                print("Invalid: Must enter an int | float")
                continue
            break

        pp.get_source_duration(file_path)
        pp.compress(file_path, target_fs)
    elif select_pp == 2:  # cut
        while True:
            start_sec = input("Enter start time [HH:MM:SS.MS]: ")
            end_sec = input("Enter end time [HH:MM:SS.MS]: ")

            try:
                start_time = datetime.strptime(start_sec, "%H:%M:%S.%f")
                end_time = datetime.strptime(end_sec, "%H:%M:%S.%f")

                if end_time <= start_time:
                    print("Invalid: End must be greater than start")
                    continue
            except ValueError:
                print("Invalid: Format must be HH:MM:SS.MS (e.g, 00:12:34.567)")
                continue
            break

        pp.timeline_cut(file_path, start_sec, end_sec)
    elif select_pp == 3:  # convert
        while True:
            convert_to = input("Enter format: ").strip().lower()
            if convert_to not in valid_formats:
                print("Invalid: Not a format")
                continue
            break

        pp.convert(file_path, convert_to)
    elif select_pp == 4:  # exit
        pass


if __name__ == "__main__":
    main()
