# -*- coding: utf-8 -*-
"""


Quality Assurance-Quality Check (QA-QC) plotting for the FAAM Core Nevzorov vane
measuring liquid and total water content (LWC and TWC).


Layout (landscape):

  -------------------------------------------
  |                                         |
  | Timeseries of LWC_021      |
  |                                         |
  -------------------------------------------
  -------------------------------------------
  |                                         |
  | Timeseries of LWC_083    |
  |                                         |
  -------------------------------------------
  -------------------------------------------
  |                                         |
  | Timeseries of TWC   |
  |                                         |
  -------------------------------------------

@author: Poppy Townsend
"""


import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

from general import *
from utils import *
from style import *

# parameter names used in this script
VARIABLE_NAMES=['Time',
                'SEADAS',    ## raw readings (in counts) taken from the nevzorov LWC Collector Voltage output
                'CORCON_nv_lwc_icol',    ## raw readings (in counts) taken from the nevzorov LWC Collector Current output
                'CORCON_nv_lwc_vref',    ## raw readings (in counts) taken from the nevzorov LWC Reference Voltage output
                'CORCON_nv_lwc_iref',    ## raw readings (in counts) taken from the nevzorov LWC Reference Current output
                'CORCON_nv_twc_vcol',    ## raw readings (in counts) taken from the nevzorov TWC Collector Voltage output
                'CORCON_nv_twc_icol',    ## raw readings (in counts) taken from the nevzorov TWC Collector Current output
                'CORCON_nv_twc_vref',    ## raw readings (in counts) taken from the nevzorov TWC Reference Voltage output
                'CORCON_nv_twc_iref',    ## raw readings (in counts) taken from the nevzorov TWC Reference Current output
                'WOW_IND',               ## Weight on wheels indicator
                'NV_LWC_C',              ## Uncorrected liquid water content from the Nevzorov probe
                'NV_TWC_C']              ## Uncorrected total condensed water content from the Nevzorov probe.



# timeseries plot for total water content
def plot_lwc_rawcounts(ax, data):
    """
    plotting the rawcounts from the DLU for the Liquid Water Content probe
    of the Nevzorov vane

    """
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_lwc_vcol'][:,0].ravel(), '-', label = 'vcol')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_lwc_icol'][:,0].ravel(), '-', label = 'icol')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_lwc_vref'][:,0].ravel(), '-', label = 'vref')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_lwc_iref'][:,0].ravel(), '-', label = 'iref')
    ax.tick_params(labelbottom='off')
    ax.text(0.05, 0.98,' Liquid Water Content (LWC)', axes_title_style, transform=ax.transAxes)
    ax.set_ylabel('Raw counts (-)')
    ax.legend(loc='upper right')
    if ax.get_ylim()[0] < 0:
        ax.set_ylim((0, ax.get_ylim()[1]))
    return ax


def plot_twc_rawcounts(ax,data):
    """
    plotting the rawcounts from the DLU for the Total Water Content probe
    of the Nevzorov vane

    """
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_twc_vcol'][:,0].ravel(), '-', label = 'vcol')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_twc_icol'][:,0].ravel(), '-', label = 'icol')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_twc_vref'][:,0].ravel(), '-', label = 'vref')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(),
                 data['CORCON_nv_twc_iref'][:,0].ravel(), '-', label = 'iref')
    ax.tick_params(labelbottom='off')
    ax.text(0.05, 0.98,'Total Water Content (TWC)', axes_title_style, transform=ax.transAxes)
    ax.set_ylabel('Raw counts (-)')
    ax.legend(loc='upper right')
    if ax.get_ylim()[0] < 0:
        ax.set_ylim((0, ax.get_ylim()[1]))
    return ax


def plot_derived_nv(ax,data):
    """
    Plots the derived TWC and LWC from the Nevzorov vane

    """
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(), data['NV_LWC_C'][:,0].ravel(), '-', label = 'LWC')
    ax.plot_date(data['mpl_timestamp'][:,0].ravel(), data['NV_TWC_C'][:,0].ravel(), '-', label = 'TWC')

    hourloc=mpl.dates.HourLocator()
    xtickformat=mpl.dates.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(hourloc)
    ax.xaxis.set_major_formatter(xtickformat)
    ax.text(0.05, 0.98,'Derived', axes_title_style, transform=ax.transAxes)
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Water (g m-3)')
    ax.legend(loc='upper right')
    return ax


def main(ds):
    """
    Creates overview plot for nevzorov vane for a single flight

    """
    #Setup up axes layout: 3 axes in one column
    gs = gridspec.GridSpec(3, 1)
    fig = QaQc_Figure(landscape=True).setup()
    fig.add_subplot(gs[2,:])
    fig.add_subplot(gs[1,:], sharex=fig.get_axes()[0])
    fig.add_subplot(gs[0,:], sharex=fig.get_axes()[0])
    for ax in fig.get_axes():
        ax.callbacks.connect('xlim_changed', adjust_ylim)

    set_suptitle(fig, ds, 'QA-Nevzorov')

    data = get_data(ds, VARIABLE_NAMES)

    #Call the plotting methods below
    plot_twc_rawcounts(fig.get_axes()[2],data)
    plot_lwc_rawcounts(fig.get_axes()[1],data)
    plot_derived_nv(fig.get_axes()[0],data)

    #adds grey bar showing take-off/landing and only plots the flight
    ax = fig.get_axes()[0]
    zoom_to_flight_duration(ax, data)
    add_time_buffer(ax)

    for ax in fig.get_axes():
        add_takeoff(ax, data)
        add_landing(ax, data)
    fig.canvas.draw()
    return fig
