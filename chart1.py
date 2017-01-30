import pandas as pd
from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json

df = pd.read_csv('pokemontypenumbers.csv')
print(df)

from bokeh.plotting import figure, output_file, save

from bokeh.charts import Bar, output_file, show
from bokeh.layouts import row
from bokeh.charts import color, marker



bar = Bar(df, values='# of Pokemon', label=['Type'],
           agg='mean', title="Number of Pokemon per Type", plot_width=400)
d = Donut(df, label=['Type'], values='# of Pokemon',
          text_font_size='8pt', hover_text='# of Pokemon')


output_file("pokemontypechart.html")
show(row(bar, d))
