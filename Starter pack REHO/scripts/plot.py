from wrapper_amplpy.plotting import plotting, sankey
import pandas as pd

results = pd.read_pickle('results/example_7a.pickle')

plotting.plot_performance(results, plot='costs', indexed_on='Scn_ID', label='FR_long', auto_open=True)
plotting.plot_performance(results, plot='gwp', indexed_on='Scn_ID', label='FR_long', auto_open=True)

for sc in results:
     source, target, value, label_, color_ = sankey.df_sankey(results[sc][0], label='FR_long', color='ColorPastel')
     sankey.plot_sankey(source, target, value, label_, color_)

units_to_plot = ['ElectricalHeater', 'HeatPump', 'PV', 'Battery']
for sc in results:
    plotting.plot_profiles(results[sc][0], units_to_plot, label='FR_long', resolution='weekly', plot_curtailment=True)


