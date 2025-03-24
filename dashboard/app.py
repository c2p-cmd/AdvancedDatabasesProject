import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import dotenv
import os

# Configure MySQL connection
print(f"Loading environment variables from .env file... {dotenv.load_dotenv(".env")}")
db_connection_str = os.getenv("DB_CONNECTION")
if db_connection_str is None:
    raise ValueError(
        "DB_CONNECTION environment variable not set. Please create a .env file and refer to the .env.example file for guidance."
    )
engine = create_engine(db_connection_str)

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Gaming Database Analytics"

# Define the layout with tabs for organization
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "Video Game Store Database Analytics",
                        className="text-center my-4",
                    ),
                    width=12,
                )
            ]
        ),
        dbc.Tabs(
            [
                # Tab 1: Game Analytics
                dbc.Tab(
                    label="Game Analytics",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H3("Game Popularity", className="mt-3"),
                                        dcc.Graph(id="popular-games"),
                                        html.H3("Price Distribution", className="mt-3"),
                                        dcc.Graph(id="price-distribution"),
                                        html.H3("Games by Genre", className="mt-3"),
                                        dcc.Graph(id="genre-distribution"),
                                    ],
                                    width=12,
                                )
                            ]
                        )
                    ],
                ),
                # Tab 2: Gamer Analytics
                dbc.Tab(
                    label="Gamer Analytics",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H3("Top Spenders", className="mt-3"),
                                        dcc.Graph(id="top-spenders"),
                                        html.H3("Most Active Gamers", className="mt-3"),
                                        dcc.Graph(id="active-gamers"),
                                        html.H3(
                                            "Email Domain Analysis", className="mt-3"
                                        ),
                                        dcc.Graph(id="email-analysis"),
                                    ],
                                    width=12,
                                )
                            ]
                        )
                    ],
                ),
                # Tab 3: Publisher Analytics
                dbc.Tab(
                    label="Publisher Analytics",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H3(
                                            "Publishers by Game Count", className="mt-3"
                                        ),
                                        dcc.Graph(id="publisher-games"),
                                        html.H3("Publisher Revenue", className="mt-3"),
                                        dcc.Graph(id="publisher-revenue"),
                                        html.H3(
                                            "Publishers by Country", className="mt-3"
                                        ),
                                        dcc.Graph(id="publisher-countries"),
                                    ],
                                    width=12,
                                )
                            ]
                        )
                    ],
                ),
                # Tab 4: Raw Data & Procedures
                dbc.Tab(
                    label="Raw Data & Procedures",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H3(
                                            "Database Queries and Procedures",
                                            className="mt-3",
                                        ),
                                        dbc.Select(
                                            id="query-selector",
                                            options=[
                                                # Analytics queries
                                                {
                                                    "label": "Top 5 Most Popular Games",
                                                    "value": "popular_games",
                                                },
                                                {
                                                    "label": "Gamers With Most Purchases",
                                                    "value": "most_purchases",
                                                },
                                                {
                                                    "label": "Gamers With Highest Spending",
                                                    "value": "highest_spending",
                                                },
                                                {
                                                    "label": "Gamers With No Purchases",
                                                    "value": "no_purchases",
                                                },
                                                {
                                                    "label": "Games Not Purchased",
                                                    "value": "not_purchased",
                                                },
                                                {
                                                    "label": "Most Expensive Games",
                                                    "value": "expensive_games",
                                                },
                                                {
                                                    "label": "Cheapest Games",
                                                    "value": "cheapest_games",
                                                },
                                                {
                                                    "label": "Publishers By Game Count",
                                                    "value": "publisher_games",
                                                },
                                                # Stored procedures
                                                {
                                                    "label": "Show All Gamers With Purchases",
                                                    "value": "proc_gamers_purchases",
                                                },
                                                {
                                                    "label": "Show Purchased Games",
                                                    "value": "proc_purchased_games",
                                                },
                                            ],
                                            value="popular_games",
                                            className="mb-3",
                                        ),
                                        # Individual gamer library lookup
                                        html.H4(
                                            "Look Up Gamer's Library", className="mt-4"
                                        ),
                                        dbc.InputGroup(
                                            [
                                                dbc.Input(
                                                    id="gamer-tag-input",
                                                    placeholder="Enter gamer tag...",
                                                    type="text",
                                                ),
                                                dbc.Button(
                                                    "Show Library",
                                                    id="show-library-button",
                                                    color="primary",
                                                ),
                                            ],
                                            className="mb-3",
                                        ),
                                        # Results container
                                        html.Div(id="query-results", className="mt-3"),
                                    ],
                                    width=12,
                                )
                            ]
                        )
                    ],
                ),
                # Tab 5: Gamer Comparison
                dbc.Tab(
                    label="Gamer Comparison",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H3(
                                            "Compare Gmail vs iCloud Users",
                                            className="mt-3",
                                        ),
                                        dcc.Graph(id="email-comparison"),
                                        html.H5(
                                            "Purchase Patterns by Email Domain",
                                            className="mt-3",
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Graph(id="email-spending"),
                                                    width=6,
                                                ),
                                                dbc.Col(
                                                    dcc.Graph(id="email-genres"),
                                                    width=6,
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=12,
                                )
                            ]
                        )
                    ],
                ),
            ]
        ),
    ],
    fluid=True,
)


# Callback for the main charts in Game Analytics tab
@app.callback(
    [
        Output("popular-games", "figure"),
        Output("price-distribution", "figure"),
        Output("genre-distribution", "figure"),
    ],
    [Input("query-selector", "value")],
)
def update_game_analytics(_):
    # Most popular games chart
    popular_query = """
        SELECT v.title, v.genre, COUNT(gp.purchase_id) AS times_purchased
        FROM VideoGames v
        INNER JOIN Purchases gp ON v.game_id = gp.game_id
        GROUP BY v.title, v.genre
        ORDER BY times_purchased DESC
        LIMIT 10
    """
    popular_df = pd.read_sql(popular_query, engine)
    popular_fig = px.bar(
        popular_df,
        x="title",
        y="times_purchased",
        color="genre",
        title="Top 10 Most Popular Games",
        labels={"times_purchased": "Number of Purchases", "title": "Game Title"},
    )

    # Price distribution chart
    price_query = """
        SELECT v.price, COUNT(*) as game_count
        FROM VideoGames v
        GROUP BY v.price
        ORDER BY v.price
    """
    price_df = pd.read_sql(price_query, engine)
    price_fig = px.histogram(
        price_df,
        x="price",
        y="game_count",
        nbins=10,
        title="Game Price Distribution",
        labels={"price": "Price ($)", "game_count": "Number of Games"},
    )
    price_fig.add_vline(
        x=price_df["price"].mean(),
        line_dash="dash",
        line_color="red",
        annotation_text=f"Mean Price: {price_df["price"].mean():.2f}",
        annotation_position="top",
    )

    # Genre distribution chart
    genre_query = """
        SELECT v.genre, COUNT(*) as game_count
        FROM VideoGames v
        GROUP BY v.genre
    """
    genre_df = pd.read_sql(genre_query, engine)
    genre_fig = px.pie(
        genre_df, values="game_count", names="genre", title="Games by Genre", hole=0.3
    )

    return popular_fig, price_fig, genre_fig


# Callback for the Gamer Analytics tab
@app.callback(
    [
        Output("top-spenders", "figure"),
        Output("active-gamers", "figure"),
        Output("email-analysis", "figure"),
    ],
    [Input("query-selector", "value")],
)
def update_gamer_analytics(_):
    # Top spenders chart
    spenders_query = """
        SELECT g.gamer_tag, SUM(p.price_paid) AS total_spent
        FROM Gamers g
        INNER JOIN Purchases p ON g.gamer_tag = p.gamer_tag
        GROUP BY g.gamer_tag
        ORDER BY total_spent DESC
        LIMIT 10
    """
    spenders_df = pd.read_sql(spenders_query, engine)
    spenders_fig = px.bar(
        spenders_df,
        x="gamer_tag",
        y="total_spent",
        title="Top 10 Spenders",
        labels={"total_spent": "Total Spent ($)", "gamer_tag": "Gamer"},
    )

    # Most active gamers chart
    active_query = """
        SELECT g.gamer_tag, COUNT(p.purchase_id) AS purchase_count
        FROM Gamers g
        INNER JOIN Purchases p ON g.gamer_tag = p.gamer_tag
        GROUP BY g.gamer_tag
        ORDER BY purchase_count DESC
        LIMIT 10
    """
    active_df = pd.read_sql(active_query, engine)
    active_fig = px.bar(
        active_df,
        x="gamer_tag",
        y="purchase_count",
        title="Most Active Gamers",
        labels={"purchase_count": "Number of Purchases", "gamer_tag": "Gamer"},
    )

    # Email domain analysis
    email_query = """
        SELECT 
            SUBSTRING_INDEX(g.email, '@', -1) AS email_domain,
            COUNT(g.gamer_tag) AS user_count
        FROM 
            Gamers g
        GROUP BY 
            email_domain
        ORDER BY 
            user_count DESC
    """
    email_df = pd.read_sql(email_query, engine)
    email_fig = px.pie(
        email_df,
        values="user_count",
        names="email_domain",
        title="Gamers by Email Domain",
        hole=0.3,
    )

    return spenders_fig, active_fig, email_fig


# Callback for Publisher Analytics
@app.callback(
    [
        Output("publisher-games", "figure"),
        Output("publisher-revenue", "figure"),
        Output("publisher-countries", "figure"),
    ],
    [Input("query-selector", "value")],
)
def update_publisher_analytics(_):
    # Publishers by game count
    pub_games_query = """
        SELECT gp.name, COUNT(v.game_id) AS games_published
        FROM GamePublishers gp
        INNER JOIN VideoGames v ON gp.publisher_id = v.publisher_id
        GROUP BY gp.name
        ORDER BY games_published DESC
    """
    pub_games_df = pd.read_sql(pub_games_query, engine)
    pub_games_fig = px.pie(
        pub_games_df,
        names="name",
        values="games_published",
        title="Publishers by Number of Games",
        labels={"games_published": "Games Published", "name": "Publisher"},
    )

    # Publisher revenue (estimated from purchases)
    pub_revenue_query = """
        SELECT 
            gp.name, 
            SUM(p.price_paid) AS total_revenue
        FROM 
            GamePublishers gp
        INNER JOIN 
            VideoGames v ON gp.publisher_id = v.publisher_id
        INNER JOIN 
            Purchases p ON v.game_id = p.game_id
        GROUP BY 
            gp.name
        ORDER BY 
            total_revenue DESC
    """
    pub_revenue_df = pd.read_sql(pub_revenue_query, engine)
    pub_revenue_fig = px.bar(
        pub_revenue_df,
        x="name",
        y="total_revenue",
        title="Publisher Revenue from Purchases",
        labels={"total_revenue": "Revenue ($)", "name": "Publisher"},
    )

    # Publishers by country
    pub_country_query = """
        SELECT 
            gp.country, 
            COUNT(*) AS publisher_count
        FROM 
            GamePublishers gp
        GROUP BY 
            gp.country
        ORDER BY 
            publisher_count DESC
    """
    pub_country_df = pd.read_sql(pub_country_query, engine)
    pub_country_fig = px.pie(
        pub_country_df,
        values="publisher_count",
        names="country",
        title="Publishers by Country",
        hole=0.3,
    )

    return pub_games_fig, pub_revenue_fig, pub_country_fig


# Callback for Email Comparison tab
@app.callback(
    [
        Output("email-comparison", "figure"),
        Output("email-spending", "figure"),
        Output("email-genres", "figure"),
    ],
    [Input("query-selector", "value")],
)
def update_email_comparison(_):
    # Email domain user stats
    email_stats_query = """
        SELECT 
            SUBSTRING_INDEX(g.email, '@', -1) AS email_domain,
            COUNT(g.gamer_tag) AS user_count,
            AVG(TIMESTAMPDIFF(YEAR, g.birth_date, CURDATE())) AS avg_age
        FROM 
            Gamers g
        GROUP BY 
            email_domain
    """
    email_stats_df = pd.read_sql(email_stats_query, engine)
    email_stats_fig = px.bar(
        email_stats_df,
        x="email_domain",
        y=["user_count", "avg_age"],
        title="Email Domain User Statistics",
        text_auto=True,
        barmode="group",
        labels={"email_domain": "Email Domain", "value": "Value", "variable": "Metric"},
    )
    email_stats_fig.update_traces(texttemplate="%{y:.2s}", textposition="outside")

    # Email domain spending
    email_spending_query = """
        SELECT 
            SUBSTRING_INDEX(g.email, '@', -1) AS email_domain,
            AVG(subquery.total_spent) AS avg_spent_per_user
        FROM 
            Gamers g
        LEFT JOIN (
            SELECT 
                p.gamer_tag,
                SUM(p.price_paid) AS total_spent
            FROM 
                Purchases p
            GROUP BY 
                p.gamer_tag
        ) AS subquery ON g.gamer_tag = subquery.gamer_tag
        GROUP BY 
            email_domain
    """
    email_spending_df = pd.read_sql(email_spending_query, engine)
    email_spending_fig = px.bar(
        email_spending_df,
        x="email_domain",
        y="avg_spent_per_user",
        color="email_domain",
        title="Average Spending by Email Domain",
        labels={
            "avg_spent_per_user": "Avg $ Spent per User",
            "email_domain": "Email Domain",
        },
    )

    # Genre preferences by email domain
    email_genres_query = """
        SELECT 
            SUBSTRING_INDEX(g.email, '@', -1) AS email_domain,
            v.genre,
            COUNT(*) AS purchase_count
        FROM 
            Gamers g
        INNER JOIN 
            Purchases p ON g.gamer_tag = p.gamer_tag
        INNER JOIN 
            VideoGames v ON p.game_id = v.game_id
        GROUP BY 
            email_domain, v.genre
        ORDER BY 
            email_domain, purchase_count DESC
    """
    email_genres_df = pd.read_sql(email_genres_query, engine)
    email_genres_fig = px.bar(
        email_genres_df,
        x="genre",
        y="purchase_count",
        color="email_domain",
        title="Genre Preferences by Email Domain",
        barmode="group",
        labels={"purchase_count": "Number of Purchases", "genre": "Game Genre"},
    )

    return email_stats_fig, email_spending_fig, email_genres_fig


# Callback for raw query results
@app.callback(
    Output("query-results", "children"),
    [Input("query-selector", "value"), Input("show-library-button", "n_clicks")],
    [State("gamer-tag-input", "value")],
)
def display_query_results(selected_query, n_clicks, gamer_tag):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Handle gamer library lookup
    if trigger_id == "show-library-button" and gamer_tag:
        query = f"CALL ShowGamerLibrary('{gamer_tag}')"
        try:
            df = pd.read_sql(query, engine)
            if df.empty:
                return html.Div(
                    [
                        html.H5(f"Library for {gamer_tag}"),
                        html.P("No games found in library."),
                    ]
                )
            else:
                return html.Div(
                    [
                        html.H5(f"Library for {gamer_tag}"),
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            columns=[{"name": col, "id": col} for col in df.columns],
                            style_table={"overflowX": "auto"},
                            style_cell={"textAlign": "left", "padding": "8px"},
                            style_header={
                                "backgroundColor": "rgb(230, 230, 230)",
                                "fontWeight": "bold",
                            },
                            style_data_conditional=[
                                {
                                    "if": {"row_index": "odd"},
                                    "backgroundColor": "rgb(248, 248, 248)",
                                }
                            ],
                        ),
                    ]
                )
        except Exception as e:
            return html.Div([html.H5("Error"), html.P(f"An error occurred: {str(e)}")])

    # Handle regular queries
    if selected_query:
        queries = {
            "popular_games": """
                SELECT v.title, v.genre, COUNT(gp.purchase_id) AS times_purchased
                FROM VideoGames v
                INNER JOIN Purchases gp ON v.game_id = gp.game_id
                GROUP BY v.title, v.genre
                ORDER BY times_purchased DESC
                LIMIT 5
            """,
            "most_purchases": """
                SELECT g.gamer_tag, g.email, COUNT(gp.purchase_id) AS games_purchased
                FROM Gamers g
                INNER JOIN Purchases gp ON g.gamer_tag = gp.gamer_tag
                GROUP BY g.gamer_tag, g.email
                ORDER BY games_purchased DESC
            """,
            "highest_spending": """
                SELECT g.gamer_tag, g.email, SUM(gp.price_paid) AS total_spent
                FROM Gamers g
                INNER JOIN Purchases gp ON g.gamer_tag = gp.gamer_tag
                GROUP BY g.gamer_tag, g.email
                ORDER BY total_spent DESC
            """,
            "no_purchases": """
                SELECT g.gamer_tag, g.email
                FROM Gamers g
                LEFT JOIN Purchases p ON g.gamer_tag = p.gamer_tag
                WHERE p.purchase_id IS NULL
            """,
            "not_purchased": """
                SELECT v.title, v.genre, v.price
                FROM VideoGames v
                LEFT JOIN Purchases gp ON v.game_id = gp.game_id
                WHERE gp.purchase_id IS NULL
            """,
            "expensive_games": """
                SELECT v.title, v.genre, v.price
                FROM VideoGames v
                ORDER BY v.price DESC
                LIMIT 5
            """,
            "cheapest_games": """
                SELECT v.title, v.genre, v.price
                FROM VideoGames v
                ORDER BY v.price
                LIMIT 5
            """,
            "publisher_games": """
                SELECT gp.name, gp.country, COUNT(v.game_id) AS games_published
                FROM GamePublishers gp
                INNER JOIN VideoGames v ON gp.publisher_id = v.publisher_id
                GROUP BY gp.name, gp.country
                ORDER BY games_published DESC
            """,
            "proc_gamers_purchases": "CALL ShowGamersWithPurchases()",
            "proc_purchased_games": "CALL ShowPurchasedGames()",
        }

        query_titles = {
            "popular_games": "Top 5 Most Popular Games",
            "most_purchases": "Gamers With Most Purchases",
            "highest_spending": "Gamers With Highest Spending",
            "no_purchases": "Gamers With No Purchases",
            "not_purchased": "Games Not Purchased",
            "expensive_games": "Most Expensive Games",
            "cheapest_games": "Cheapest Games",
            "publisher_games": "Publishers By Game Count",
            "proc_gamers_purchases": "All Gamers With Their Purchase Statistics",
            "proc_purchased_games": "Games That Have Been Purchased",
        }

        if selected_query in queries:
            try:
                df = pd.read_sql(queries[selected_query], engine)
                return html.Div(
                    [
                        html.H5(query_titles.get(selected_query, "Query Results")),
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            columns=[{"name": col, "id": col} for col in df.columns],
                            style_table={"overflowX": "auto"},
                            style_cell={"textAlign": "left", "padding": "8px"},
                            style_header={
                                "backgroundColor": "rgb(230, 230, 230)",
                                "fontWeight": "bold",
                            },
                            style_data_conditional=[
                                {
                                    "if": {"row_index": "odd"},
                                    "backgroundColor": "rgb(248, 248, 248)",
                                }
                            ],
                        ),
                    ]
                )
            except Exception as e:
                return html.Div(
                    [html.H5("Error"), html.P(f"An error occurred: {str(e)}")]
                )

    return html.Div("Select a query to see results")


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
