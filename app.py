# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt


st.set_page_config(page_title='Superstore Dashboard',
                   page_icon=':chart_with_upwards_trend:',
                   layout='wide')

# reading the data from Excel file
df = pd.read_excel("FD DATA.xlsx")
df1 = pd.read_excel("Infoware data.xlsx")
#df1 = pd.read_csv("Infoware data.csv")
# remove hidden spaces from column names
df1.columns = df1.columns.str.strip()
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
image = Image.open("FDLOGO.jfif")

col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image(image, width=100)
    st.markdown(
        "<p style='font-size:13px; "
        "color:gray'><b>Source:</b> CDSC, Francis Drummond & Co. Ltd | Latest available data</p>",
        unsafe_allow_html=True
    )
html_title = """
    <style>
    .title-text{
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    </style>
    </style>
    <center><h1 class= "title-text">
    Kenya Pipeline Company IPO - Insights from Francis Drummond & Co. Ltd Investor Data
    </h1></center>"""
st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

with col2:
    st.markdown(html_title, unsafe_allow_html=True)

# Clean Next of kin column
df1["N_K_Relationship"] = (
    df1["N_K_Relationship"]
    .astype(str)
    .str.strip()
    .str.upper()
)
df1["N_K_Relationship"] = df1["N_K_Relationship"].replace({
    "WIFE": "SPOUSE",
    "HUSBAND": "SPOUSE",
    "BROTHER": "SIBLING",
    "SISTER": "SIBLING",
    "GUARDIAN": "GUARDIAN"
})

# --- KPI Section ---

# Calculate KPIs
Accounts_created = df["ACCOUNT_OPENED"].sum() * 2
CDSC_Account_opened = df["CDS_ACCOUNT_OPENED"].sum()
Average_Investor_Age = df1["Age"].mean()
Youngest_Investor = df1["Age"].min()
Oldest_Investor = df1["Age"].max()
total_investors = len(df1)
city_counts = df1["City"].value_counts()
relationship_counts = df1["N_K_relationship"].value_counts()
top_city = city_counts.index[0]
top_city_count = city_counts.iloc[0]
accounts_today = 5
df1["Gender_clean"] = df1["Gender"].astype(str).str.strip().str.upper()
male_investors = df1[df1["Gender_clean"] == "M"].shape[0]
female_investors = df1[df1["Gender_clean"] == "F"].shape[0]
top_nok = df1["N_K_relationship"].mode()[0]
top_relationship_count = relationship_counts.iloc[0]
top_dividend = df1["dividend_Disposal"].mode()[0]
top_dividend_count = df1["dividend_Disposal"].value_counts().iloc[0]
print("These are the results")
print(df1["Gender_clean"].value_counts(dropna=False))

# Display KPIs in four columns
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.markdown(
        f"""
        <div style="font-size:18px; font-weight:bold; color:#3366FF">👨‍👩‍👧‍👦 Total Investors</div>
        <div style="font-size:26px; font-weight:900; color:black;">{total_investors:,.0f}</div>
        <div style="font-size:14px; color:gray;">Total number of investors who have participated in the IPO.</div>
        """,
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        f"""
        <div style="font-size:18px; font-weight:bold; color:#3366FF">🧑➕ Account Opened on PERAGO</div>
        <div style="font-size:26px; font-weight:900; color:black;">{Accounts_created:,.0f}</div>
        <div style="font-size:14px; 
        color:gray;">Number of investor accounts successfully opened through the PERAGO onboarding system</div>
        """,
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        f"""
        <div style="font-size:18px; font-weight:bold;color:#3366FF"> 🆔 CDS Account Number Created </div>
         <div style="font-size:26px; font-weight:900; color:#black;">{total_investors:,.0f}</div>
         <div style="font-size:14px; 
         color:gray;">Number of clients successfully assigned new CDS account numbers..</div>
        """,
        unsafe_allow_html=True
    )
with kpi4:
    st.markdown(
        f"""
        <div style="font-size:18px; font-weight:bold;color:#3366FF"> 🔄 Average Investor Age</div>
         <div style="font-size:26px; font-weight:900; color:#black;">{Average_Investor_Age:,.0f}</div>
         <div style="font-size:14px; color:gray;">Mean age of all investors onboarded during the IPO period.</div>
        """,
        unsafe_allow_html=True
    )

kpi5, kpi6, kpi7, kpi8 = st.columns(4)
with kpi5:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF"> 🧒 Youngest Investor </div>
         <div style="font-size:26px; font-weight:900; color:#black;">{Youngest_Investor:,.0f}</div>
         <div style="font-size:14px;
          color:gray;">Age of the youngest investor registered through CDS account openings.</div>
        """,
        unsafe_allow_html=True
    )
with kpi6:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">👴 Oldest Investor</div>
         <div style="font-size:26px; font-weight:900; color:#black;">{Oldest_Investor:,.0f}</div>
         <div style="font-size:14px; color:gray;">Age of the Oldest investor recorded </div>
        """,
        unsafe_allow_html=True
    )

with kpi7:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">🎯 Top Investor City</div>
         <div style="font-size:23px; font-weight:800; color:#black;">{top_city} - {top_city_count}</div>
         <div style="font-size:14px; color:gray;">City with the highest number of investors.</div>
        """,
        unsafe_allow_html=True
    )
with kpi8:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">⚡ Daily Account Openings</div>
         <div style="font-size:26px; font-weight:800; color:#black;">{accounts_today}</div>
         <div style="font-size:14px; color:gray;">Number of CDS accounts opened by investors today</div>
        """,
        unsafe_allow_html=True
    )

kpi9, kpi10, kpi11, kpi12 = st.columns(4)
with kpi9:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">👨 Male Investors</div>
         <div style="font-size:26px; font-weight:800; color:#black;">{male_investors:,.0f}</div>
         <div style="font-size:14px; color:gray;">Total number of male investors participating in the KPC IPO.</div>
        """,
        unsafe_allow_html=True
    )
with kpi10:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">👩 Female Investors</div>
         <div style="font-size:26px; font-weight:800; color:#black;">{female_investors:,.0f}</div>
         <div style="font-size:14px; color:gray;">Total number of female investors participating in the KPC IPO.</div>
        """,
        unsafe_allow_html=True
    )
with kpi11:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">👨‍👩‍👧 Most Common Next of Kin Relationship</div>
         <div style="font-size:23px; font-weight:800; color:#black;">{top_nok} - {top_relationship_count}</div>
         <div style="font-size:14px; 
         color:gray;">The relationship type most frequently listed as next of kin by investors.</div>
        """,
        unsafe_allow_html=True
    )
with kpi12:
    st.markdown(
        f"""
       <div style="font-size:18px; font-weight:bold;color:#3366FF">💵 Most Preferred Dividend Disposal</div>
         <div style="font-size:22px; font-weight:800; color:#black;">{top_dividend} - {top_dividend_count}</div>
         <div style="font-size:14px; 
         color:gray;">The relationship type most frequently listed as next of kin by investors.</div>
        """,
        unsafe_allow_html=True
    )
col3, col4, col5 = st.columns(3)
# --- Donut Chart: Investors by Region ---
with col3:
    region_counts = (
        df1.dropna(subset=["Region"])
        .groupby("Region")
        .size()
        .reset_index(name="Total")
    )
    fig_donut = px.pie(
        region_counts,
        names="Region",
        values="Total",
        hole=0.3,
        title="Investors by Region"
    )
    fig_donut.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_donut.update_layout(
        showlegend=True,
        title_x=0
    )

    st.plotly_chart(fig_donut, use_container_width=True)

with col4:
    gender_counts = (
        df1.dropna(subset=["Gender"])
        .groupby("Gender")
        .size()
        .reset_index(name="Total")
    )

    fig_gender = px.pie(
        gender_counts,
        names="Gender",
        values="Total",
        hole=0.4,
        title="Investors by Gender",
        color_discrete_map={
            "Male": "#1f77b4",
            "Female": "#e377c2"
        }
    )

    fig_gender.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_gender.update_layout(
        showlegend=True,
        title_x=0
    )

    st.plotly_chart(fig_gender, use_container_width=True)

with col5:
    city_counts = (
        df1.dropna(subset=["City"])
        .groupby("City")
        .size()
        .reset_index(name="Total")
        .sort_values("Total", ascending=False)
        .head(5)
    )

    fig_city = px.pie(
        city_counts,
        names="City",
        values="Total",
        hole=0.4,
        title="Top 5 Cities by Number of Investors "
    )

    fig_city.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    fig_city.update_layout(
        showlegend=True,
        title_x=0
    )

    st.plotly_chart(fig_city, use_container_width=True)

col6, col7, col8 = st.columns(3)
with col6:
    df1_total = df1.groupby("Region").size().reset_index(name="Total")
    fig = px.bar(
        df1_total,
        x="Region",
        y="Total",
        text="Total",
        title="Number of Investors by Region",
        hover_data=["Total"],
        template="gridon",
        height=500,
        color_discrete_sequence=["#3884ff"]
    )
    fig.update_layout(
        yaxis_title="Number of Investors"
    )
    st.plotly_chart(fig, use_container_width=True)

with col7:
    fig_age = px.histogram(
        df1,
        x="Age",
        nbins=15,
        title="Age Distribution of Investors",
        text_auto=True,
        template="ggplot2",
        height=500,
        color_discrete_sequence=["#3884ff"]
    )

    avg_age = df1["Age"].mean()

    fig_age.add_vline(
        x=avg_age,
        line_dash="dash",
        line_color="black",
        line_width=3,
        annotation_text=f"Avg Age: {round(avg_age, 1)}",
        annotation_position="top right"
    )

    fig_age.update_layout(
        bargap=0,
        xaxis_title="Age",
        yaxis_title="Number of Investors"
    )

    st.plotly_chart(fig_age, use_container_width=True)
with col8:
    # Count next-of-kin relationships
    nk_counts = df1["N_K_relationship"].value_counts().reset_index()
    nk_counts.columns = ["Relationship", "Total"]

    # Show only top 5 relationships 
    nk_counts = nk_counts.head(5)

    # Create horizontal bar chart
    fig_nk = px.bar(
        nk_counts,
        x="Total",
        y="Relationship",
        orientation="h",
        text="Total",
        title="Next of Kin Relationship Distribution",
        template="plotly_white",
        height=500,
        color_discrete_sequence=["#3884ff"]
    )

    # make text appear inside bars 
    fig_nk.update_traces(textposition="inside")

    st.plotly_chart(fig_nk, use_container_width=True)

col9, col10, col11 = st.columns([0.3, 0.8, 0.3])

with col10:
    import geopandas as gpd
    import pandas as pd
    from matplotlib.colors import LinearSegmentedColormap

    # -------------------------------
    # Clean the IPO region counts
    # -------------------------------
    region_counts = (
        df1.loc[df1["Region"].notna() & (df1["Region"] != "NA")]
        .assign(
            Region=lambda x: x["Region"].replace({
                "Rift_valley": "Rift Valley",
                "Mt_kenya": "Mt Kenya",
                "Luo_nyanza": "Luo Nyanza"
            })
        )
        .groupby("Region", as_index=False)
        .size()
        .rename(columns={"size": "Customers"})
    )

    # -------------------------------
    # Load Kenya counties
    # -------------------------------
    @st.cache_data
    def load_kenya_counties():
        url = "https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_KEN_shp.zip"
        kenya = gpd.read_file(url, layer="gadm41_KEN_1")
        kenya = kenya[["NAME_1", "geometry"]].rename(columns={"NAME_1": "County"})
        return kenya


    kenya_counties = load_kenya_counties()

    # -------------------------------
    # County → Region mapping
    # -------------------------------
    region_lookup = pd.DataFrame({
        "County": ["Nairobi", "Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita Taveta",
                   "Machakos", "Kitui", "Makueni", "Kisii", "Nyamira", "Kisumu", "Siaya", "Homa Bay", "Migori",
                   "Kakamega", "Vihiga", "Bungoma", "Busia", "Trans Nzoia",
                   "Nyeri", "Kirinyaga", "Murang'a", "Kiambu", "Nyandarua", "Meru", "Embu", "Tharaka-Nithi", "Laikipia",
                   "Nakuru", "Uasin Gishu", "Nandi", "Baringo", "Elgeyo-Marakwet", "West Pokot", "Turkana",
                   "Samburu", "Narok", "Kajiado", "Kericho", "Bomet"],

        "Region": ["Nairobi",
                   "Coast", "Coast", "Coast", "Coast", "Coast", "Coast",
                   "Ukambani", "Ukambani", "Ukambani",
                   "Kisii", "Kisii",
                   "Luo Nyanza", "Luo Nyanza", "Luo Nyanza", "Luo Nyanza",
                   "Western", "Western", "Western", "Western", "Western",
                   "Mt Kenya", "Mt Kenya", "Mt Kenya", "Mt Kenya", "Mt Kenya", "Mt Kenya", "Mt Kenya", "Mt Kenya",
                   "Mt Kenya",
                   "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley",
                   "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley", "Rift Valley"]
    })

    # -------------------------------
    # Merge counties → regions
    # -------------------------------
    kenya_regions = kenya_counties.merge(region_lookup, on="County", how="left")
    kenya_regions = kenya_regions[kenya_regions["Region"].notna()]
    kenya_regions = kenya_regions.dissolve(by="Region", as_index=False)

    # -------------------------------
    # Join IPO counts
    # -------------------------------
    map_data = kenya_regions.merge(region_counts, on="Region", how="left")
    map_data["Customers"] = map_data["Customers"].fillna(0)

    map_data["centroid"] = map_data.geometry.centroid

    # -------------------------------
    # Custom blue colormap
    # -------------------------------
    custom_cmap = LinearSegmentedColormap.from_list(
        "ipo_blue",
        ["#e6f0ff", "#3884ff", "#003a8f"]
    )

    # -------------------------------
    # Plot
    # -------------------------------
    fig, ax = plt.subplots(figsize=(6, 6))

    kenya_counties.plot(ax=ax, color="lightgrey", edgecolor="white", linewidth=0.3)

    map_data.plot(
        column="Customers",
        ax=ax,
        cmap=custom_cmap,
        edgecolor="white",
        linewidth=0.5,
        legend=True,
        legend_kwds={"label": "Number of Investors", "shrink": 0.6}
    )

    for _, row in map_data.iterrows():
        ax.text(
            row["centroid"].x,
            row["centroid"].y,
            f"{row['Region']}\n{int(row['Customers'])}",
            ha="center",
            va="center",
            fontsize=6
        )
        ax.set_title(
            "Distribution of KPC IPO Subscribers by Region",
            fontsize=5,
            fontweight="bold"
        )
    ax.axis("off")

    # Keep centered inside the column
    st.pyplot(fig)


bins = [0, 18, 25, 35, 45, 60, 120]
labels = ["Under 18", "18–25", "26–35", "36–45", "46–60", "60+"]

df1["Age_Group"] = pd.cut(df1["Age"], bins=bins, labels=labels)
print(df1[["Age", "Age_Group"]].head(20))
print(list(df1.columns))
cols = df1.columns.tolist()

cols.remove("Age_Group")
cols.insert(cols.index("Age") + 1, "Age_Group")

df1 = df1[cols]
df1.to_csv("FD_DATA_updated.csv", index=False)
print("sucessful")
