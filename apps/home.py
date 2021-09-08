import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div(
    [
        html.Div([dcc.Link("Go to GVA Sector", href="/gva-sectors")]),
        html.Div([dcc.Link("Go to GVA Time Series", href="/gva-time-series")]),
        html.Div(
            [dcc.Link("Go to Agg. National Accounts", href="/agg_national_accounts")]
        ),
        html.Div(
            [dcc.Link("Go to Agg. Economic Activities", href="/agg-eco-activities")]
        ),
        html.Div([dcc.Link("Go to NVA Sector", href="/nv_eco")]),
        html.Div([dcc.Link("Go to CFC Sector", href="/cfc_sectors")]),
        html.Div([dcc.Link("Go to CFC Time Series", href="/cfc_time_series")]),
        html.Div([dcc.Link("Go to NV Time Series", href="/nv_time_series")]),
        html.Div([dcc.Link("Go to GCF Time Series", href="/gcf_time_series")]),
        html.Div([dcc.Link("Go to GCF Sector", href="/gcf_sectors")]),
        html.Div([dcc.Link("Go to Households Private consumption", href="/household")]),
        html.Div(
            [dcc.Link("Go to Disaggregated Crop Statements", href="/crop_wise_output")]
        ),
    ]
)
