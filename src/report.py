
# Utility function
def convert_html_to_pdf(source_html, output_filename):
	from xhtml2pdf import pisa             # import python module

	# open output file for writing (truncated binary)
	result_file = open(output_filename, "w+b")

	# convert HTML to PDF
	pisa_status = pisa.CreatePDF(
			source_html,                # the HTML to convert
			dest=result_file)           # file handle to recieve result

	# close output file
	result_file.close()                 # close output file

	# return True on success and False on errors
	return pisa_status.err

def makePDF(name="name", nVertices="nVertices", nEdges="nEdges", maxValency="maxValency", avgValency="avgValency", curve="curve",diameter="not computed"):
	print(" * Building PDF report")

	import matplotlib.pyplot as plt
	from matplotlib.collections import EventCollection
	import io
	import base64

	# plot the data
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.plot(curve['x'], curve['y'], color='tab:red')

	xevents1 = EventCollection(curve['x'], color='tab:blue', linelength=0.5)
	yevents1 = EventCollection(curve['y'], color='tab:blue', linelength=0.5,orientation='vertical')

	# add the events to the axis
	ax.add_collection(xevents1)
	ax.add_collection(yevents1)


	if not diameter:
		diameter = "not computed"

	# set the limits
	ax.set_xlim([0, maxValency+1])
	ax.set_ylim([0, max(curve['y'])+5])

	ax.set_title('Distribution des degrés')
	plt.xlabel('Degré')
	plt.ylabel('Frequence d\'apparition (%)')

	# display the plot
	# plt.show()

	my_stringIObytes = io.BytesIO()
	plt.savefig(my_stringIObytes, format='jpg')
	my_stringIObytes.seek(0)
	my_base64_jpgData = base64.b64encode(my_stringIObytes.read())

	with open('template/index.html') as template:

		report_html = template.read().replace('\n', '').replace('\t', '').format(image=my_base64_jpgData, 
																				caption='Salut', width=600, height=400, 
																				name=name, nVertices=nVertices, nEdges=nEdges, 
																				maxValency=maxValency, avgValency=avgValency,diameter=diameter)

		convert_html_to_pdf(report_html, name + '-report.pdf')

		return "report-2.pdf"
