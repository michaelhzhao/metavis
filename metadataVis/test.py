import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import DataTable, NumberFormatter, TableColumn, Button
from bokeh.plotting import show
from bokeh.layouts import column

df = []
for ii in range(1, 11):
    df.append({'x': ii, 'y': 1000 * np.random.rand()})
df = pd.DataFrame(df)

source = ColumnDataSource(data=df)

columns = [TableColumn(field='x', title='Col 1'), TableColumn(field='y', title='Col 2',formatter=NumberFormatter(format='$0,0.00',text_align='right'))]

dt = DataTable(source=source, columns=columns, width=500, height=200, row_headers=False)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var filetext = 'x,y\\n';
    
    for (i=0; i < data['x'].length; i++) {
        var currRow = [data['x'][i].toString(), data['y'][i].toString().concat('\\n')];
        var joined = currRow.join();
        filetext = filetext.concat(joined);
    }	
    
    var filename = 'data.csv';
    var blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' });
    
    //addresses IE
    if (navigator.msSaveBlob) {
        navigator.msSaveBlob(blob, filename);
    }
    
    else {
        var link = document.createElement("a");
        link = document.createElement('a')
        link.href = URL.createObjectURL(blob);
        link.download = filename
        link.target = "_blank";
        link.style.visibility = 'hidden';
        link.dispatchEvent(new MouseEvent('click'))
    }
""")

button = Button(label='Download', button_type='success', callback=callback)

show(column(dt, button))
