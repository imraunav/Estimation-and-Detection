from pyedflib import highlevel

signals, signal_headers, header = highlevel.read_edf('chb01_01.edf')
print(signal_headers[0]['sample_frequency']) # prints 256
print(header)
