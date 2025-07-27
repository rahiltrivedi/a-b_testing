# dashboard.py
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from statsmodels.stats.proportion import proportions_ztest

# Load your dataset
df = pd.read_csv("ab_test_data.csv")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "A/B Test Dashboard"

# Layout
app.layout = html.Div([
    html.H1("📊 A/B Testing Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("🔍 Select Group(s):"),
        dcc.Checklist(
            id='group-select',
            options=[
                {'label': 'Group A', 'value': 'A'},
                {'label': 'Group B', 'value': 'B'}
            ],
            value=['A', 'B'],
            inline=True
        )
    ], style={'padding': '20px'}),

    html.Div(id='summary-output', style={'padding': '20px', 'fontSize': '16px'}),

    dcc.Graph(id='conversion-bar')
])

# Callback to update dashboard
@app.callback(
    Output('conversion-bar', 'figure'),
    Output('summary-output', 'children'),
    Input('group-select', 'value')
)
def update_dashboard(selected_groups):
    if not selected_groups:
        return {}, "⚠️ Please select at least one group."

    # Filter data
    filtered = df[df['group'].isin(selected_groups)]

    # Group sizes
    group_counts = filtered['group'].value_counts()

    # Conversion rate
    conversion = filtered.groupby('group')['converted'].mean().reset_index()
    conversion['converted'] *= 100  # convert to %

    # Hypothesis test if both A and B present
    if set(['A', 'B']).issubset(set(group_counts.index)):
        successes = df.groupby('group')['converted'].sum()
        nobs = df['group'].value_counts().sort_index()
        z_stat, p_val = proportions_ztest(successes, nobs)
        stats_text = f"🧪 Z-statistic: {z_stat:.3f} | P-value: {p_val:.4f}"
        conclusion = "✅ Statistically significant" if p_val < 0.05 else "❌ Not statistically significant"
    else:
        stats_text = "ℹ️ Z-test only runs when both Group A and B are selected."
        conclusion = ""

    # Summary text
    summary = [
        html.P(f"👥 Total Users: {len(filtered)}"),
        html.P(f"🅰️ Group A Users: {group_counts.get('A', 0)}"),
        html.P(f"🅱️ Group B Users: {group_counts.get('B', 0)}"),
        html.P("📊 Conversion Rates:"),
        html.P(conversion.to_string(index=False)),
        html.P(stats_text),
        html.P(conclusion)
    ]

    # Conversion bar chart
    fig = px.bar(
        conversion,
        x='group',
        y='converted',
        text_auto='.2f',
        labels={'converted': 'Conversion Rate (%)', 'group': 'Group'},
        title='Conversion Rate by Group'
    )
    fig.update_layout(yaxis_range=[0, 100])

    return fig, summary

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
