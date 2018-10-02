import os, subprocess

#--------------------------------------------------------------------

# Add CURRENT directory for fotoage
viddir_input = "/users/vids"

# Add NEW fps
fps = "24"

# Add NEW encoder
filety = "prores"

# Add NEW output path (w/ "/" at end)
otpath = "/Users/Drew/desktop/"

# Add NEW wrapper
wrap = ".mov"

# Add NEW output size (width) 
newsize = "700"

#--------------------------------------------------------------------

"""NOTE-THIS SCRIPT IS FOR ENCODING TO A NEW DIRECTORY
ADD INCREMENTED OUTPUT NAMES (_01) IF ADDING TO CURRENT DIRECTORY"""

os.chdir(str(viddir_input))
cwd = os.getcwd()
lst_i = []


os.chdir(str(viddir_input))

def boi():
	path = cwd
	non_dir = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
	lst_i.append 
	for vid in non_dir:
		if not vid.startswith('.'):
			lst_i.append(vid)
			onames = vid[0:len(vid)-4]
			final = "ffmpeg -i " + vid + " -r " + fps + " -c:v " + filety + " -profile:v 0 " + "-vf scale=" + newsize + ":-1 " + otpath + onames + wrap
			#subprocess.call(final, shell=True)
			print final


boi()


