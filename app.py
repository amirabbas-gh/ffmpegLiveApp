from config import hls, rtmps
import subprocess

ffmpeg_commands = []

for rtmp in rtmps:
    streamUrl = f'{rtmp["url"]}/{rtmp["key"]}'
    if rtmp['vertical']:
        streamCommend = f'ffmpeg -re -i "{hls}" \
-strict -2 -c:v libx264 -vf "transpose=1" -c:a aac -map 0:0 -map 0:1 -ar 44100 -ab 128k -ac 2 \
-flags +global_header -bsf:a aac_adtstoasc -bufsize 1000k \
-f flv "{streamUrl}"'
    else:
        streamCommend = f'ffmpeg -re -i "{hls}" \
    -strict -2 -c:v copy -c:a aac -map 0:0 -map 0:1 -ar 44100 -ab 128k -ac 2 \
    -flags +global_header -bsf:a aac_adtstoasc -bufsize 1000k \
    -f flv "{streamUrl}"'
    ffmpeg_commands.append(streamCommend)
    
# Create a list to store the subprocesses
processes = []

# Run each ffmpeg command in a separate subprocess
for command in ffmpeg_commands:
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

# Wait for all subprocesses to finish
for process in processes:
    process.wait()

print("All ffmpeg commands have completed.")
