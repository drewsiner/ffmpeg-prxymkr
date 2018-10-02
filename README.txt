2018-10-02 FFMPEG-proxymkr notes:

- Currently uses vid[0:len(vid)-4] to rename output files with new wrapper. Could cause issues with files whose source wrapper is larger or smaller than 3 characters

- Currently relies on subprocess to call ffmpeg with bash=True

- Defaults to prores422 proxy. For prores422 HQ change profile:v from “0” to “3”. For prores4444 change “prores” to “prores_ks” and profile:v from “0” to “5”