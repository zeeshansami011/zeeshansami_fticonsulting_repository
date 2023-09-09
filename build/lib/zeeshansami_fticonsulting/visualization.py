# Barchart Carshare Data

import plotly.data as data
import plotly.express as px

# Data Handling
def load_carshare_data():
    return data.carshare()

# Visualization Functions
def barchart_carsharedata():
    dataframe = load_carshare_data()
    fig = px.histogram(dataframe, x="peak_hour", nbins=24, title="Car Count by Peak Hour")
    fig.show()


# Barchart ElectionData

# Import necessary libraries
import plotly.data as data
import plotly.express as px
import pandas as pd

# Load the election data
def load_election_data():
    return data.election()

# Reshape the data using melt
def melt_election_data(election_data):
    return pd.melt(election_data, id_vars=['district'], value_vars=['Coderre', 'Bergeron', 'Joly'], 
                   var_name='candidate', value_name='votes')

# Visualization Function
def barchart_electiondata(dataframe):
    fig = px.bar(dataframe, x='district', y='votes', color='candidate', title="Votes by District and Candidate", 
                 height=600, width=1200, barmode='group')
    fig.update_layout(xaxis_tickangle=-45)
    return fig

if __name__ == "__main__":
    election_data = load_election_data()
    melted_data = melt_election_data(election_data)
    
    # Visualize
    fig = barchart_electiondata(melted_data)
    fig.show()
    
 # Box and Whisker Plots Carshare Dataset
 
 # visualization.py

import plotly.data as data
import plotly.express as px

def load_carshare_data():
    """Load the carshare dataset from plotly."""
    return data.carshare()

def boxandwhiskerplot_carsharedata(dataframe):
    """Plot car count by peak hour."""
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    fig = px.box(df, y='counts', title='Car Count by Peak Hour')
    return fig

# Box and Whisker Plots Electiondata Dataset
    
# visualization.py

import plotly.data as data
import plotly.express as px

# Load the election data
election_data = data.election()

def boxandwhiskerplot_electiondata(candidate_name):
    """Generate a boxplot for votes distribution by district for a specific candidate."""
    df = election_data[['district', candidate_name]]
    df.columns = ['district', 'votes']
    fig = px.box(df, y='votes', title=f'Votes Distribution by District for {candidate_name}')
    return fig
    
# Dot Plots Carshare Dataset

# visualization.py

import plotly.data as data
import plotly.express as px

def load_carshare_data():
    """Load carshare dataset from plotly."""
    return data.carshare()

def dotplots_carsharedata(dataframe):
    """Generate a scatter plot showing car count by peak hour."""
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    fig = px.scatter(df, x='peak_hour', y='counts', title='Car Count by Peak Hour')
    fig.update_traces(marker=dict(size=15,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    return fig

# Dot Plots Electiondata Dataset
# visualization.py

import plotly.data as data
import plotly.express as px

# Load the election data
election_data = data.election()

def dotplots_electiondata(candidate_name):
    """Generate a scatter plot for votes distribution by district for a specific candidate."""
    df = election_data[['district', candidate_name]]
    df.columns = ['district', 'votes']
    fig = px.scatter(df, x='votes', y='district', title=f'Votes by District for {candidate_name}')
    fig.update_traces(marker=dict(size=15,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
    return fig

# Heatmaps Carshare Dataset
# visualization.py

import plotly.data as data
import plotly.express as px

def load_carshare_data():
    """Load carshare dataset from plotly."""
    return data.carshare()

def heatmaps_carsharedata(dataframe):
    """Generate a heatmap showing car count by peak hour."""
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    fig = px.imshow(df, labels=dict(x="Peak Hour", y="Counts"), title='Car Count by Peak Hour')
    return fig

# Heatmaps Electiondata Dataset
# visualization.py

import plotly.data as data
import plotly.express as px

# Load the election data
election_data = data.election()

def heatmaps_electiondata(candidate_name):
    """Generate a heatmap for votes distribution by district for a specific candidate."""
    df = election_data[['district', candidate_name]]
    df.columns = ['district', 'votes']
    fig = px.imshow(df.pivot_table(values='votes', index='district'),
                    title=f'Votes by District for {candidate_name}')
    return fig

# Radar Spider Chart carsharedata Dataset
# visualization.py

import plotly.data as data
import plotly.express as px

def load_carshare_data():
    """Load carshare dataset from plotly."""
    return data.carshare()

def radarspiderchart_carsharedata(dataframe):
    """Generate a radar/spider chart showing car count by peak hour."""
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    fig = px.line_polar(df, r='counts', theta='peak_hour', line_close=True)
    fig.update_traces(fill='toself')
    fig.update_layout(
        title="Car Count by Peak Hour",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, df['counts'].max()]
            ))
    )
    return fig

# Radar Spider Chart electiondata Dataset    
    # visualization.py

import plotly.data as data
import plotly.graph_objects as go

# Load the election data
election_data = data.election()

def radarspiderchart_electiondata(candidate_name):
    """Generate a radar/spider chart for votes distribution by district for a specific candidate."""
    districts = election_data['district'].tolist()
    votes = election_data[candidate_name].tolist()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=votes,
        theta=districts,
        fill='toself',
        name=candidate_name,
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(votes)+10]
            )),
        showlegend=False,
        title=f"Votes by District for {candidate_name}"
    )
    
    return fig
# Treemaps carsharedata Dataset 
# visualization.py

import plotly.data as data
import plotly.express as px

# Load the carshare data
def load_carshare_data():
    return data.carshare()

def treemaps_carsharedata(dataframe):
    """Generate a treemap for car counts by peak hour."""
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    fig = px.treemap(df, path=['peak_hour'], values='counts',
                     title='Car Count by Peak Hour')
    return fig

# Treemaps electiondata Dataset
# visualization.py

import plotly.data as data
import plotly.express as px

# Load the election data
def load_election_data():
    return data.election()

def treemaps_electiondata(candidate_name):
    """Generate a treemap for votes by district for a specific candidate."""
    df = load_election_data()[['district', candidate_name]]
    df.columns = ['district', 'votes']
    fig = px.treemap(df, path=['district'], values='votes',
                     title=f'Votes by District for {candidate_name}')
    return fig


# waterfall Charts Carsharedata Dataset
# visualization.py

import plotly.data as data
import plotly.graph_objects as go

# Load the carshare data
def load_carshare_data():
    return data.carshare()

def waterfallcharts_carsharedata():
    """Generate a waterfall chart for car counts by peak hour."""
    dataframe = load_carshare_data()
    df = dataframe.groupby('peak_hour').size().reset_index(name='counts')
    
    fig = go.Figure(go.Waterfall(
        name = "20", 
        orientation = "v",
        measure = ["relative"]*len(df['peak_hour']),
        x = df['peak_hour'],
        textposition = "outside",
        text = df['counts'],
        y = df['counts'],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
        title="Car Count by Peak Hour",
    )
    return fig


# waterfall Charts Electiondata Dataset   
# visualization.py

import plotly.data as data
import plotly.graph_objects as go

# Load the election data
def load_election_data():
    return data.election()

def waterfallcharts_electiondata(candidate_name):
    """Generate a waterfall chart for votes by district for a given candidate."""
    election_data = load_election_data()
    districts = election_data['district'].tolist()
    votes = election_data[candidate_name].tolist()
    
    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative"]*len(districts),
        x = districts,
        textposition = "outside",
        text = votes,
        y = votes,
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    fig.update_layout(title=f"Votes by District for {candidate_name}")
    return fig

