import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap

st.set_page_config(
    page_title="HK Competitor Heatmap",
    page_icon="🧘🏻‍♀️",
    )

#creating a title for the app
st.title("Heatmap of HK's Yoga Market")

# Create a base map centered around Kuala Lumpur
m = folium.Map(location=[22.302711, 114.177216], zoom_start=12)

# Your list of latitudes and longitudes
data = {
  "Pure Group - Yoga": [
    (22.2767088, 114.1682706),
    (22.2876928, 114.212492),
    (22.2831831, 114.1556444),
    (22.2821988, 114.1839874),
    (22.2787869, 114.1824394),
    (22.3189021, 114.1687515),
    (22.3247465, 114.1731786),
    (22.2954015, 114.172262),
    (22.2350322, 114.1980799),
    (22.3126322, 114.2253942),
    (22.2780477, 114.1654178)
  ],
  "TriAngel Yoga": [
    (22.2768089, 114.1814348),
    (22.3026987, 114.1725416),
    (22.3112696, 114.2225645),
    (22.3677743, 114.1157649),
    (22.3895625, 114.2094383)
  ],
  "Miga Studio": [
    (22.3385861, 114.1991489),
    (22.339083434395754, 114.1479518268551)
  ],
  "Yoga Senses": [
    (22.3106414, 114.2260401),
    (22.3370334, 114.1505753)
  ],
  "Flex Studio": [
    (22.2805175, 114.155957),
    (22.2483994, 114.1688561)
  ],
  "Raj Yoga Studio": [
    (22.2870183, 114.148489)
  ],
  "One Yoga Studio": [
    (22.2752738, 114.1714249),
    (22.2825151, 114.1559351),
    (22.2921964, 114.1996991)
  ],
  "Ikigai HK": [
    (22.2807062, 114.1567481),
    (22.2779309, 114.1826668)
  ],
  "The Yoga Room": [
    (22.2852936, 114.150751)
  ],
  "Flowga Studio": [
    (22.2809283, 114.1552982)
  ]
}


regions = {
    'Causeway Bay': [
        (22.2821988, 114.1839874),
        (22.2787869, 114.1824394),
        (22.2768089, 114.1814348),
        (22.2779309, 114.1826668)
        ],
    'Central': [
        (22.2831831, 114.1556444),
        (22.2805175, 114.155957),
        (22.2870183, 114.148489),
        (22.2825151, 114.1559351),
        (22.2807062, 114.1567481),
        (22.2852936, 114.150751),
        (22.2809283, 114.1552982)
        ],
    'Kwun Tong': [
        (22.3126322, 114.2253942),
        (22.3112696, 114.2225645),
        (22.3106414, 114.2260401)
        ],
    'Wan Chai': [
        (22.2767088, 114.1682706),
        (22.2752738, 114.1714249),
        (22.2780477, 114.1654178)
        ],
    'North Point': [
        (22.2876928, 114.212492),
        (22.2921964, 114.1996991)
        ],
    'Tsim Sha Tsui': [
        (22.2954015, 114.172262),
        (22.3026987, 114.1725416)
        ],
    'Mong Kok': [
        (22.3189021, 114.1687515),
        (22.3247465, 114.1731786)
        ],
    'Lai Chi  Kok': [
        (22.339083434395754, 114.1479518268551),
        (22.3370334, 114.1505753)
        ],
    'Repulse Bay': [
        (22.2350322, 114.1980799)
        ],
    'Tsuen Wan': [
        (22.3677743, 114.1157649)
        ],
    'Shimen': [
        (22.3895625, 114.2094383)
        ],
    'San Po Kong': [
        (22.3385861, 114.1991489)
        ],
    'Wong Chuk Hang': [
        (22.2483994, 114.1688561)
        ]
}


#Function to find the region of a studio
def find_region(lat, lon, regions):
    for region, coords in regions.items():
        if (lat, lon) in coords:
            return region
    return None

# Function to find all studios for a given latitude and longitude
def find_studios(lat, lon, data, formatted_studios):
    matching_studios = set()  # Use a set to avoid duplicates
    
    for studio, coords in data.items():
        if (lat, lon) in coords:
            # Add the studio name as it is, no star for duplicates
            matching_studios.add(formatted_studios.get(studio, studio))

    return list(matching_studios)  # Convert the set back to a list

# Function to format regions and studios in columns
def format_columns(regions_studios):
    # Create HTML table with no borders
    table_html = "<table style='width: 100%; border: 0;'><tr style='border: 0;'>"
    count = 0
    total_regions = len(regions_studios)
    remaining_regions = total_regions % 3

    for r, studios in regions_studios.items():
        if studios:  # Only consider regions with studios
            # Check if it's the last row and not a multiple of 3
            if count >= total_regions - remaining_regions and remaining_regions != 0:
                if remaining_regions == 1 and count % 3 == 0:  # If only one region, add padding on both sides
                    table_html += "<td style='border: 0;'></td>"
                elif remaining_regions == 2 and count % 3 == 0:  # If two regions, and it's the first one, just add it
                    pass
                elif remaining_regions == 2 and count % 3 == 1:  # If two regions, and it's the second one, add padding to the left first
                    table_html += "<td style='border: 0;'></td>"
            
            column_html = f"<td style='padding: 8px; width: 33%; border: 0; vertical-align: top;'><b>{r}:</b><br>"
            column_html += '<br>'.join(studios)
            column_html += "</td>"
            table_html += column_html
            
            count += 1

            if count % 3 == 0 and count != total_regions:
                table_html += "</tr><tr style='border: 0;'>"
            elif remaining_regions == 1 and count == total_regions:  # If only one region, add padding on the right after displaying it
                table_html += "<td style='border: 0;'></td>"
    
    table_html += "</tr></table>"
    return table_html

def create_streetview(lat,lon):
    return f"http://maps.google.com/maps?q=&layer=c&cbll={lat},{lon}&cbp=12,0,0,0,0)"


# Radio button for Studios vs. Regions
selection_type = st.radio("Select by:", ["Studios", "Regions"])

# Initialize a dictionary to store region-wise studio lists with counts
region_studio_mapping = {region: {} for region in regions}

# Update the mapping based on data
for studio, coords in data.items():
    for coord in coords:
        region = find_region(coord[0], coord[1], regions)
        if region:
            if studio not in region_studio_mapping[region]:
                region_studio_mapping[region][studio] = 0
            region_studio_mapping[region][studio] += 1

# Now, let's create a new mapping that formats the studio names with stars if needed
formatted_region_studio_mapping = {}
for region, studios in region_studio_mapping.items():
    formatted_studios = {}
    for studio, count in studios.items():
        formatted_studios[studio] = f"{studio}*" if count > 1 else studio
    formatted_region_studio_mapping[region] = formatted_studios

if selection_type == "Studios":
    select_all = st.checkbox("Select all Studios")
    if select_all:
        selections = list(data.keys())
    else:
        selections = st.multiselect("Which Yoga Studio do you want to see?", list(data.keys()))

    # Combine data from all selected studios into a single list and add markers with popups
    combined_data = []
    regions_studios = {region: [] for region in regions}  #Initialize empty list for each region
    for s in selections:
        combined_data.extend(data[s])
        for point in data[s]:
            region = find_region(point[0], point[1], regions)
            streetview_url = create_streetview(point[0], point[1])
            popup_text = f"""
            <div style="width: 200px;">
                <b>{s}</b><br><br>
                <i>Region: {region}</i><br><br>
                <a href='{streetview_url}' target='_blank'>Open in Street View</a>
            </div>
            """
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=popup_text
            ).add_to(m)

else:
    # Implementing the "Select All" checkbox for regions
    select_all = st.checkbox("Select all Regions")
    if select_all:
        selections = list(regions.keys())
    else:
        selections = st.multiselect("Which Region do you want to see?", list(regions.keys()))

    # Combine data from all selected regions into a single list and add markers with popups
    combined_data = []
    for r in selections:
        combined_data.extend(regions[r])
        for point in regions[r]:
            studios = find_studios(point[0], point[1], data, formatted_region_studio_mapping[r])
            studios_text = ', '.join(studios)
            streetview_url = create_streetview(point[0], point[1])
            popup_text = f"""
            <div style="width: 200px;">
                <b>{studios_text}</b><br><br>
                <i>Region: {r}</i><br><br>
                <a href='{streetview_url}' target='_blank'>Open in Street View</a>
            </div>
            """
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=popup_text
            ).add_to(m)



# Add a single heatmap to the base map using the combined data
HeatMap(combined_data).add_to(m)

# Save the map to an HTML file
st_folium(m,height=600,  width=700)

# Use formatted_region_studio_mapping for displaying in Streamlit
if selection_type == "Studios":
    regions_studios = {}
    for r, coords in regions.items():
        # Use the formatted names with stars for duplicate studios
        studios_in_region = [s for s in selections if s.strip('*') in formatted_region_studio_mapping[r]]
        if studios_in_region:
            regions_studios[r] = studios_in_region

    if regions_studios:
        st.write("**Selected Studios in Their Respective Regions:**")
        st.markdown(format_columns(regions_studios), unsafe_allow_html=True)


else:
    regions_studios = {}
    for r in selections:
        # Use the formatted names with stars
        studios_in_region = formatted_region_studio_mapping[r]
        if studios_in_region:
            regions_studios[r] = studios_in_region

    if regions_studios:
        st.write("**Studios in Selected Regions:**")
        st.markdown(format_columns(regions_studios), unsafe_allow_html=True)