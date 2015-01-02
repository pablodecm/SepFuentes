c = get_config()

c.NbConvertApp.notebooks = ['SepFuentes.ipynb']
c.NbConvertApp.export_format = 'latex'

c.Exporter.template_file = 'citations'
