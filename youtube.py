#/usr/bin/python3
# YouTube to MP3/MP4
from requests import Session
from sys import argv

if len(argv)<3: exit(f"YouTube to MP3/MP4\nVersion 1.0\n\nExamples:\n  Download a video as MP3: python {argv[0]} https://youtu.be/dQw4w9WgXcQ mp3\n  Download a video as MP4: python {argv[0]} https://youtu.be/dQw4w9WgXcQ mp4\n  Search a video & download it as MP3: python {argv[0]} 'Rick Astley' mp3")

# Download location, must end in "/"
location = "./"

# Colors
green = "\u001b[32;1m"
red = "\u001b[31;1m"
reset = "\u001b[0m"

# System config
main_url = "https://www.y2mate.com/mates/analyzeV2/"
hand = Session()
hand.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0", "Referer": "https://www.y2mate.com/"})
payload = {"k_query":argv[1],"k_page":"Youtube","hl":"en","q_auto":"1"}

# Search & parse arguments
try:
    method = exit(f"{red}ERROR:{reset} Wrong usage") if argv[2] not in ["mp3", "mp4"] else argv[2]
    r = hand.post(main_url + "ajax", data=payload)
    () if '"mess":' not in r.text else () if len(r.json()['mess'])<1 else exit(f"{red}ERROR:{reset} {r.json()['mess']}") if "Sorry" not in r.json()['mess'] else exit(f"{red}ERROR:{reset} Video not found"), exit(f"{red}ERROR:{reset} Wrong URL") if "UNKNOWN_VIDEO" in r.text else ()
    if r.json()['page']=="search":
      ids, titles = [r.json()['vitems'][_]['v'] for _ in range(len(r.json()['vitems']))], [r.json()['vitems'][_]['t'] for _ in range(len(r.json()['vitems']))]
      for id, title in zip(ids, titles): print(f"[{green}{ids.index(id)}{reset}]", title)
      payload['k_query'] = "https://youtu.be/" + str(ids[int(input("\nChoose a video with a number: "))])
      r = hand.post(main_url + "ajax", data=payload)
    print("Converting video, please wait...")
except KeyboardInterrupt: exit()
except ValueError: exit(f"{red}ERROR:{reset} Wrong format")
except IndexError: exit(f"{red}ERROR:{reset} Wrong usage")

# Parse response data
title, size, res = r.json()['title'].replace('/','_').replace('"','_').replace("'","_").replace('\\','_'), r.json()['links'][method][str(list(r.json()['links'][method].keys())[0])]['size'], hand.post(main_url.replace('analyze','convert') + "index", data={"vid": r.json()['vid'], "k": r.json()['links'][method][list(r.json()['links'][method].keys())[0]]['k']})

# Download
print(f"Downloading {green}{title}.{method.lower()}{reset}, size: {green}{size}{reset}")
with hand.get(res.json()['dlink'], stream=True) as resp:
    if resp.status_code!=200: exit("Something wrong happened, try again.")
    with open(f"{location if location[-1]=='/' else location + '/'}{title}.{method}","wb") as f:
      for chunk in resp.iter_content(chunk_size=8192): f.write(chunk)
      f.close()

print("Done!")


