from urllib import request

print("\t\t +PDF File downloader+")
pdffilelink = input("research-paper: ")
pdffile = 'http://www.ijsrp.org/+pdffilelink'

def downloadfile(pdf_url):
	resp = request.urlopen(pdf_url)
	pdf = resp.read()
	pdf_str = str(pdf)
	lines = pdf_str.split("\\n")
	dest_url = r'dowloadedfile.pdf'
	fx = open(dest_url, 'w')
	for line in lines:
		fx.write(line + "\n")
	fx.close()

if __name__ == '__main__':
	downloadfile(pdffile)
	print("Download Completed")