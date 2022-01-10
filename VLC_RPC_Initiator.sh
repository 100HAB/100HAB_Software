raspivid -o - -t 0 -vf -w 1280 -h 720 -fps 20 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
