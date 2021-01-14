# read file names from a text file called files_to_move.txt
# check if file exists in src_loc
# if so move file to tgt_loc

import pathlib, os, shutil

def if_src_file_exists(srcdir, file):
	path = os.path.join(srcdir, file)
	return os.path.isfile(path)

def mv_file(doc, src, tgt):
	from_path = os.path.join(src, doc)
	to_path = os.path.join(tgt, doc)

	shutil.move(from_path, to_path)


def main():
	files = [file.strip() for file in open('files_to_move.txt').readlines()]
	print(files)

	src_loc = os.path.expanduser('~/Downloads')
	tgt_loc = os.path.expanduser('~/Documents/languages/italki_docs')

	for file in files:
		if if_src_file_exists(src_loc, file):
			mv_file(file, src_loc, tgt_loc)			

main()
