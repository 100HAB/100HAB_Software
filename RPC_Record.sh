#Run raspivid to record video for 5 minutes and pass it to ffmpeg to convert it to a mp4 file
raspivid -o - -t 300000 -hf -w 1280 -h 720 -fps 25 -b 2000000 | ffmpeg -i - -vcodec copy -acodec copy -f mp4 /home/pi/100HAB_Vids/`date +%Y%m%d%H%M%S`.mp4
